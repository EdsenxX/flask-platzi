from flask import request, make_response, redirect, render_template,session, url_for, flash
import unittest

from app import create_app

app = create_app()

todos=["Comprar café","Solicitud de compra", "Entregar un video al productor"]

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


@app.errorhandler(500)
def error_server(error):
    return render_template("500.html", error=error)


@app.route("/")
def index():
    user_ip=request.remote_addr
    response = make_response(redirect("/hello"))
    #response.set_cookie("user_ip",user_ip)
    session['user_ip'] = user_ip
    return response


@app.route("/hello", methods=["GET"])
def hello():
    #user_ip = request.cookies.get("user_ip")
    user_ip = session.get("user_ip")
    username = session.get("username")
    context = {
        "user_ip":user_ip,
        "username": username,
        "todos":todos,
    }

    return render_template("hello.html", **context)
