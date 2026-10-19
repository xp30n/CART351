from flask import Flask 
app = Flask(__name__) # everything that is in this folder is basically the project setup

# this is what we use to call the function | when a user types a slash, the function will start
@app.route("/") 
def index(): 
    return 'Hello CART351!'

@app.route("/about")
def about():
    return '<h1 style = "color:purple"> About Cart 351!</h1>'

@app.route("/user/<name>")
def user_profile(name):
    # we will use templates sooN!
    return f"<h2> This is <span style = 'color:blue'>{name}'s</span> profile page" 

# @app.route("/another/<dynamicVar>")
# def another_route(dynamicVar):
#     # we will use templates sooN
#     return f"<h2> the 100th letter of {dynamicVar} is {dynamicVar[99]}</h2>"


@app.route("/catlatin/<word>")
def cat_latin(word):
    if(word[-1].lower() != "y"):
        return f"{word}y"
    return f"{word[:-1]}iful"
    
app.run()