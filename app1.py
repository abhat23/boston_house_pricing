import pickle
from flask import Flask, request, app,jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)




