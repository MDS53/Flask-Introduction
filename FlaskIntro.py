from flask import Flask
app=Flask(__name__) # Flask is a class and __name__ is a entry point of flask program

if __name__ == '__main__':
    app.run(debug=True)#Here bydefault it takes local host (runs on local url) and port = 5000
    