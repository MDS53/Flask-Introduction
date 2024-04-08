#Flask URL routing
"""
    Here in each url we have specific names like /home,/index,/profile,etc...
    in order to get like that we need to create a specific url for (/anyname)the url and this is called url routing or Flask app routing
"""
from flask import Flask 

app=Flask(__name__)

@app.route('/', methods=['GET'])# app.route() will helps to route to the url and "/" indicating the home page or bydefault page and whatever function we write below this route() that will be called implicitly
def welcome():
    return "<h1>Welcome to Flask</h1>" 

@app.route('/index', methods=['GET'])# app.route() will helps to route to the url and "/index" indicating the page or bydefault url(home url with local host and port 5000)ends with /index from default url or bydefault page and whatever function we write below this route() that will be called implicitly
def index():
    return "Welcome to Index page" 

#Here this will the entry point for flask app
if __name__=='__main__':
    app.run(debug=True) #debug ==true because no need of reloading the page it will automatically gets reloaded whenever we make any changes