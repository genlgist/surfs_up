from typing_extensions import runtime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'


set Flask_app:app.py
Flask run

@app.route('/hello')
def hello_world():
   return "hello world"

import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite://Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)