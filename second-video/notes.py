from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



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

# @app.get("/", include_in_schema=False)
# def read_item(request: Request):
#     return templates.TemplateResponse(  
#         request=request,
#         name="home.html") #*name of file
#* given in return is the new way to write/pass tamplates in fastapi


#* if we have two of more routes on same function 
#* then we have to use name parameter in the route decorator to give a unique name to each route.
#* such that if a btn is href to # then it will not work because it will not know which route to go to. 
#* so we have to give a unique name to each route and then use that name in the href of the btn.
@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(  
        request=request,
        name="home.html",
        context={'posts': posts,'title': 'My FastAPI App'} #*this is to pass the data to the template. we can access this data in the template using jinja2 syntax. for example we can access the title of post 1 using {{ posts[0].title }}
    )