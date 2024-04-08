from flask import Flask

app=Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to Flask brother Yogender"


@app.route('/sucess/<score>') # this will take score as input in url ends with /sucess/your_input (enter score) and in that page whatever the score given as input that will be returned 
def sucess(score):
    return "You got "+score+"score : Passed successfully bhai"

@app.route('/fail/<int:score2>') # Here we can specify score's datatype
def fail(score2):
    return "You got "+str(score2)+"score : Failed bhai"


if __name__=='__main__':
    app.run(debug=True)


#Note : NO function name should be same , if same it returns an error