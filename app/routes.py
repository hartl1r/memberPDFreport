# app/routes.py

from flask import render_template, request, url_for
from flask_weasyprint import HTML, render_pdf
from app import app, db
from app.models import Member


@app.route("/")
def home():
    members = Member.query.limit(5).all()
    return render_template("home.html", members=members)

@app.route('/print.pdf')
def print_pdf():
    return render_pdf(url_for('home'))
