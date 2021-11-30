# Put your app in here.
form flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
    """ adds parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)

    return = str(result)

@app.route("/subtract")
def do_subtract():
    """ subtract parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = subtract(a,b)

    return = str(result)


@app.route("/divide")
def do_divide():
    """ divide parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = divide(a,b)

    return = str(result)   

@app.route("/multiply")
def do_multiply():
    """ multiply parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = multiply(a,b)

    return = str(result)    


    operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)