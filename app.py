import numpy as np
import pandas as pd
import sqlite3
import json

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, Column, Integer, String

from flask import Flask,jsonify, render_template, redirect


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///rat_race_a.sqlite")
cnx = sqlite3.connect('rat_race_a.sqlite',check_same_thread=False)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

class ed(Base):
    __tablename__ = 'cr12b_trials_info' 
    __table_args__ = {'extend_existing': True}
    trial_number = Column(Integer, primary_key=True)
    correct_side = Column(String(255))
    stim_number = Column(Integer)
    nonrandom= Column(Integer)
    outcome= Column(String(255))
    go_or_nogo= Column(String(255))
    block=Column(Integer)
    stim_name= Column(String(255))
    

# class madison(Base):
#     __tablename__ = 'cr17b_trials_info'
#     trial_number = Column(Integer, primary_key=True)
#     correct_side = Column(String(255))
#     stim_number = Column(Integer)
#     nonrandom= Column(Integer)
#     outcome= Column(String(255))
#     go_or_nogo= Column(String(255))
#     block=Column(Integer)
#     stim_name= Column(String(255))
#     extend_existing=True

# class lucy(Base):
#     __tablename__ = 'cr20b_trials_info'
#     trial_number = Column(Integer, primary_key=True)
#     correct_side = Column(String(255))
#     stim_number = Column(Integer)
#     nonrandom= Column(Integer)
#     outcome= Column(String(255))
#     go_or_nogo= Column(String(255))
#     block=Column(Integer)
#     stim_name= Column(String(255))
#     extend_existing=True


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    
    return render_template("index.html")

@app.route("/rat")
def show_rat():
    return render_template("pg1.html")

@app.route("/data")
def pick_rat():
    # rat_data = engine.execute(f'select * from cr12b_trials_info')
    session = Session(engine)
    results = session.query(ed.trial_number,ed.correct_side).all()
    rats = ['le_lc_go', 'ri_lc_no', 'lo_pc_go', 'hi_pc_no', 'le_hi_lc', 'ri_hi_lc', 'le_lo_lc', 'ri_lo_lc', 'le_hi_pc', 'ri_hi_pc', 'le_lo_pc', 'ri_lo_pc']
    trial =[]
    side = []
    hits_outcomes =[]
    wrongs_outcomes =[]
    for r in rats:
        hits = session.query(ed.outcome,ed.stim_name).filter(ed.stim_name == r, ed.outcome=='hit').all()
        errors = session.query(ed.outcome,ed.stim_name).filter(ed.stim_name == r, ed.outcome=='error').all()
        wrongs = session.query(ed.outcome,ed.stim_name).filter(ed.stim_name == r, ed.outcome=='wrong_port').all()
        hits_outcomes.append(len(hits)+len(errors))
        wrongs_outcomes.append(len(wrongs))
      

    for result in results:
        trial.append(result[0])
        side.append(result[1])

    data = [{
        "trial":trial,
        "side":side,
        "hits":hits_outcomes,
        "wrong":wrongs_outcomes
    }]






    return jsonify(data)


    # return render_template("pg1.html")


if __name__ == "__main__":
    app.run(debug=True)
