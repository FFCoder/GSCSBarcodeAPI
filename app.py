from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/barcode")
def barcode():
    return "Test"