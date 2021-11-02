from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def showCreateNinjaPage():
    return render_template("add_ninja.html", dojos = Dojo.getAllDojos())

@app.route("/create/add_ninja",methods=["POST"])
def addNinjaToDojo():
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]

    }
    Ninja.addNinja(data)
    return redirect("/dojos")


