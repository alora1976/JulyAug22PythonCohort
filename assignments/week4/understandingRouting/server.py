from flask import Flask

app = Flask(__name__)
    
@app.route('/')         
def hello_world():
    return 'Hello World!'
@app.route('/<dojo>')

def dojo():
    return 'Dojo!'

#create a route that responds with 'hi' and whatever name is passed into the url
@app.route('/<name>')
def hi(name):
    return 'Hi ' + name + '!'

#create a route with a given word that is repeated as many times as is passed into the url and 
# ensure word is a string
@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return (word * num)

#Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again."
@app.route('/<path:path>')
def error(path):
    return 'Sorry! No response. Try again.'





if __name__=="__main__":   
    app.run(debug=True)   

