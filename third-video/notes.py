from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from fastapi.exceptions import RequestValidationError #*handle validation errors
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException #* the fastapi is actually built on starlette,so when we go to path like /dne/ its starlette that handle these errors



posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(  
        request=request,
        name="home.html",
        context={'posts': posts,'title': 'My FastAPI App'}
    )

@app.get("/posts/{post_id}", include_in_schema=False, name="post_page")
def post_page(post_id:int, request: Request):
    for post in posts:
        if post_id== post['id']:
            title=post['title'][:50]
            return templates.TemplateResponse(
                request=request,
                name='post.html',
                context={'post':post,'title':title}
            )
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')

@app.get("/api/posts/{post_id}")
def get_post(post_id:int):
    #* by writing post_id:int we are classifing that post_id is a intiger. if anything non integer pass through it then fastapi will automatically return a 422 code and error msg saying "Input should be a valid integer, unable to parse string as an integer"
    for post in posts:
        if post_id == post['id']:
            return post
#   raise HTTPException(status_code=404, detail='Post not found') #* raising httpexceception is the best way to handle errors in fastapi as simply  returning 'not_found' as string will give 200 ok status code.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found') #* using status let use also transmit the meaning of code with code.


#* there are majorlly two type of error handleing we have to first if path do not exist(using starlette) and if path parameter input type is wrong (request validation excepiton)
#* and in both 

## StarletteHTTPException Handler
@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (
        exception.detail
        if exception.detail #* this will handle if details of exception exits on starlette or not if it didnt find one then else will pass
        else "An error occurred. Please check your request and try again."
    )
    #*given below if statement is to seperate aip request from html. for api we give json error message and for html we show them error.html page
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code,
            content={"detail": message},
        )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": exception.status_code,
            "title": exception.status_code,
            "message": message,
        },
        status_code=exception.status_code, #* this is added to show error code in cli
    )
#*the given above starlette exception handler do not handle type validation errors like in post_id we pass a string intead of a integer





### RequestValidationError Handler
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):#* checks if typevalidation error is from api request 
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exception.errors()},
        )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid request. Please check your input and try again.",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )