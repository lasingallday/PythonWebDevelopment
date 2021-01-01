from datetime import datetime

from flask import Blueprint, render_template #, request

from .extensions import db
from .models import County, Stimulus, Member

main = Blueprint('main', __name__)

@main.route('/')
def index():

    return render_template('form.html')
