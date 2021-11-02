from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
import flask_app.controllers.ninjas

@app.route("/")
def index():
    return redirect("/dojos")

@app.route('/dojos')
def dojos():
    all_dojos = Dojo.getAllDojos()
    return render_template("dojos.html", dojos = all_dojos)

@app.route("/create", methods=["POST"])
def createDojo():
    data = {
        "name": request.form["name"]
    }
    data = Dojo.add_dojo(data)
    return redirect('/dojos')

@app.route("/dojos/<int:id>")
def showDojo(id):
    names = Dojo.getDojoName(id)
    name = names[0]["name"]
    all_ninjas = Ninja.getAllNinjas(id)
    return render_template("dojo.html", allNinjas = all_ninjas, dojoName = name)