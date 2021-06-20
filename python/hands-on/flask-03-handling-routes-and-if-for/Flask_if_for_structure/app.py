from flask import Flask

app = Flask(__name__)

@app.route('/')
def head():
    return "This is my first conditions experience"



@app.route('/first')
def first():
    return "1,2,3,4,5,6,7,8,9,10"




if __name__=="__main__":
    #app.run(host='0.0.0.0', port=80)
    app.run(debug=True)