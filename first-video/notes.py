# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello, world!"}  
# 
# //* given from 1 to 6 is most basic code to run fastapi server. we can run this code using uvicorn command in terminal. uvicorn filename:app --reload

# //* following are the different types of request methods that can be used in fastapi. we can use these methods to create different endpoints for our api.
# @app.get("/") 
# //* get request method is used to get data from the server.
# @app.get("/items/{item_id}") 
# //* get request method is used to get data from the server. we can use path parameters to get specific data from the server.
# @app.post("/items/") 
# //* post request method is used to send data to the server. we can use this method to create new data on the server.
# @app.delete("/items/{item_id}") 
# //* delete request method is used to delete data from the server.
# @app.put("/items/{item_id}") 
# //* put request method is used to update data on the server.
# @app.patch("/items/{item_id}") 
# //* patch request method is used to partially update data on the server.
# def read_item():
#     return {}

# //* as shown above we can stack multiple decorators on a single function to create multiple endpoints for our api.
# //*  we can also use different request methods for the same endpoint. for example we can use get and post request methods for the same endpoint.



############### html response in fastapi ###############

# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# @app.get("/posts", response_class=HTMLResponse)
# def read_item():

# @app.get("/posts", response_class=HTMLResponse, include_in_schema=False)    #//* this will hide the endpoint from the documentation page
# def read_item():
    
    
    # return """
    # <html>
    #     <head>
    #         <title>FastAPI HTML Response</title>
    #     </head>
    #     <body>
    #         <h1>Hello, world!</h1>
    #         <p>This is an HTML response from FastAPI.</p>
    #     </body>
    # </html>
    # """

    # or

    # return f"""
    # <html>
    #     <head>
    #         <title>FastAPI HTML Response</title>
    #     </head>
    #     <body>
    #         <h1>Hello, world!</h1>
    #         {js works here }
    #         <p>This is an HTML response from FastAPI.</p>
    #     </body>
    # </html>
    # """


