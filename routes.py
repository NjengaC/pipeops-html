from flask import render_template, flash, request, redirect, url_for, jsonify
from flask_login import login_user, login_required, logout_user, current_user
import json
import stripe
import secrets
from sqlalchemy.exc import IntegrityError
from flask import render_template
from geopy.distance import geodesic

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')


if __name__ == '__main__':
    app.run(debug=True)
