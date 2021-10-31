from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return render_template("dojos.html")