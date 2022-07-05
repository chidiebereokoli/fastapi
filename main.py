from fastapi import FastAPI

app = FastAPI() #FastAPI instance name

#This is a path operation, also called a "Route"



@app.get("/")
async def root():
    return {"message": "Welcome to my API!!!!!!!!!!!!!"}

@app.get("/")
def get_posts():
    return {"data": "This is our post"}

#AN API IS SIMPLY A BUNCH OF PATH OPERATIONS THAT ALLOWS USERS TO HIT DIFFERENT ENDPOINTS
#comprises of a function (path operation function):
    #async def root(): #async means we are running the function asynchronously, we don't need to do this now..
    #    return {"message": "Hello World"}
#and a decorator; @app.get("/"). With the decorator, we have to pass in the HTTP method that will be used to hit the path url that you want to be accessed. The decorator above turns the root() function to a path operation function so that someone who wants to use our API, can hit the endpoint "/".
#To use a decorator, we use the "@", with our fastapi instance name (app), and a HTTP method (get)
#fastApi automatically converts what is returned to a JSON.
#Path "/"  means the path after the specific domain name of our API. In our little case, our webserver is hosted on url http://127.0.0.1:8000 , so http://127.0.0.1:8000/ brings us to the same point still. This is the root path.

#Next, we need to start our server, which we do by running uvicorn main<filename>:app<fastapi_instance_name>
#we successfully start the server, and we see that the server is running on http://127.0.0.1:8000 (i.e. localhost on port 8000)
#ANYTIME WE MAKE A CHANGE, WE MUST RESTART OUR SERVER.
#To avoid having to manually restart our server anytime we change our code, instead of running "uvicorn main:app", we run "uvicorn main:app --reload". We should pass this "--reload" flag in  development environment, we do not need to do this is a production environment though, since we won't be changing code in a production environment.

#when a request comes in from a user's browser, it just goes through the server code, and once it hits an endpoint, it stops right there, without executing the rest of the server code. So, order matters, and we must remember this.
#we can use the web browser to send get HTTP methods to our server. But, when we need to send HTTP Put,Delete, POSt, there is no way to natively do this is in the browser, without building a FE application.  
# We will use the Postman App, to construct our own HTTP request, specifying method, url, headers, body, data, authorization headers (if any) etc.