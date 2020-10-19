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
    

class madison(Base):
    __tablename__ = 'cr17b_trials_info'
    __table_args__ = {'extend_existing': True}
    trial_number = Column(Integer, primary_key=True)
    correct_side = Column(String(255))
    stim_number = Column(Integer)
    nonrandom= Column(Integer)
    outcome= Column(String(255))
    go_or_nogo= Column(String(255))
    block=Column(Integer)
    stim_name= Column(String(255))
    extend_existing=True

class lucy(Base):
    __tablename__ = 'cr20b_trials_info'
    __table_args__ = {'extend_existing': True}
    trial_number = Column(Integer, primary_key=True)
    correct_side = Column(String(255))
    stim_number = Column(Integer)
    nonrandom= Column(Integer)
    outcome= Column(String(255))
    go_or_nogo= Column(String(255))
    block=Column(Integer)
    stim_name= Column(String(255))
    extend_existing=True

class lauren(Base):
    __tablename__ = 'cr21ab_trials_info'
    __table_args__ = {'extend_existing': True}
    trial_number = Column(Integer, primary_key=True)
    correct_side = Column(String(255))
    stim_number = Column(Integer)
    nonrandom= Column(Integer)
    outcome= Column(String(255))
    go_or_nogo= Column(String(255))
    block=Column(Integer)
    stim_name= Column(String(255))

class josh(Base):
    __tablename__ = 'cr24a_trials_info'
    __table_args__ = {'extend_existing': True}
    trial_number = Column(Integer, primary_key=True)
    correct_side = Column(String(255))
    stim_number = Column(Integer)
    nonrandom= Column(Integer)
    outcome= Column(String(255))
    go_or_nogo= Column(String(255))
    block=Column(Integer)
    stim_name= Column(String(255))

class marco(Base):
    __tablename__ = 'yt6a_trials_info'
    __table_args__ = {'extend_existing': True}
    trial_number = Column(Integer, primary_key=True)
    correct_side = Column(String(255))
    stim_number = Column(Integer)
    nonrandom= Column(Integer)
    outcome= Column(String(255))
    go_or_nogo= Column(String(255))
    block=Column(Integer)
    stim_name= Column(String(255))


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

@app.route("/rat/<name>")
def show_rat(name):
    rat_name = str(name) 
    return render_template("pg1.html", r_name=rat_name)

@app.route("/data")
def pick_rat():
    
    session = Session(engine)
    
    rats = ["Ed","Madison","Lucy","Lauren","Josh","Marco"]
    stims = ['le_lc_go', 'ri_lc_no', 'lo_pc_go', 'hi_pc_no', 'le_hi_lc', 'ri_hi_lc', 'le_lo_lc', 'ri_lo_lc', 'le_hi_pc', 'ri_hi_pc', 'le_lo_pc', 'ri_lo_pc']
    
    rat_dict={}
    
    for rat in rats:
        hits_outcomes =[]
        wrongs_outcomes =[]  
        trial =[]
        side = []

        if rat=='Ed':
            for stim in stims:
                hits = session.query(ed.outcome,ed.stim_name).filter(ed.stim_name == stim, ed.outcome=='hit').all()
                errors = session.query(ed.outcome,ed.stim_name).filter(ed.stim_name == stim, ed.outcome=='error').all()
                wrongs = session.query(ed.outcome,ed.stim_name).filter(ed.stim_name == stim, ed.outcome=='wrong_port').all()
                hits_outcomes.append(len(hits)+len(errors))
                wrongs_outcomes.append(len(wrongs))

            results = session.query(ed.trial_number,ed.correct_side).all()
            for result in results:
                trial.append(result[0])
                side.append(result[1])
        elif rat=='Madison':
            for stim in stims:
                hits = session.query(madison.outcome,madison.stim_name).filter(madison.stim_name == stim, madison.outcome=='hit').all()
                errors = session.query(madison.outcome,madison.stim_name).filter(madison.stim_name == stim, madison.outcome=='error').all()
                wrongs = session.query(madison.outcome,madison.stim_name).filter(madison.stim_name == stim, madison.outcome=='wrong_port').all()
                hits_outcomes.append(len(hits)+len(errors))
                wrongs_outcomes.append(len(wrongs))

            results = session.query(madison.trial_number,madison.correct_side).all()
            for result in results:
                trial.append(result[0])
                side.append(result[1])
        elif rat=='Lucy':
                    for stim in stims:
                        hits = session.query(lucy.outcome,lucy.stim_name).filter(lucy.stim_name == stim, lucy.outcome=='hit').all()
                        errors = session.query(lucy.outcome,lucy.stim_name).filter(lucy.stim_name == stim, lucy.outcome=='error').all()
                        wrongs = session.query(lucy.outcome,lucy.stim_name).filter(lucy.stim_name == stim, lucy.outcome=='wrong_port').all()
                        hits_outcomes.append(len(hits)+len(errors))
                        wrongs_outcomes.append(len(wrongs))

                    results = session.query(lucy.trial_number,lucy.correct_side).all()
                    for result in results:
                        trial.append(result[0])
                        side.append(result[1])
        elif rat=='Lauren':
                    for stim in stims:
                        hits = session.query(lauren.outcome,lauren.stim_name).filter(lauren.stim_name == stim, lauren.outcome=='hit').all()
                        errors = session.query(lauren.outcome,lauren.stim_name).filter(lauren.stim_name == stim, lauren.outcome=='error').all()
                        wrongs = session.query(lauren.outcome,lauren.stim_name).filter(lauren.stim_name == stim, lauren.outcome=='wrong_port').all()
                        hits_outcomes.append(len(hits)+len(errors))
                        wrongs_outcomes.append(len(wrongs))

                    results = session.query(lauren.trial_number,lauren.correct_side).all()
                    for result in results:
                        trial.append(result[0])
                        side.append(result[1])
        elif rat=='Josh':
                    for stim in stims:
                        hits = session.query(josh.outcome,josh.stim_name).filter(josh.stim_name == stim, josh.outcome=='hit').all()
                        errors = session.query(josh.outcome,josh.stim_name).filter(josh.stim_name == stim, josh.outcome=='error').all()
                        wrongs = session.query(josh.outcome,josh.stim_name).filter(josh.stim_name == stim, josh.outcome=='wrong_port').all()
                        hits_outcomes.append(len(hits)+len(errors))
                        wrongs_outcomes.append(len(wrongs))

                    results = session.query(josh.trial_number,josh.correct_side).all()
                    for result in results:
                        trial.append(result[0])
                        side.append(result[1])
        elif rat=='Marco':
                    for stim in stims:
                        hits = session.query(marco.outcome,marco.stim_name).filter(marco.stim_name == stim, marco.outcome=='hit').all()
                        errors = session.query(marco.outcome,marco.stim_name).filter(marco.stim_name == stim, marco.outcome=='error').all()
                        wrongs = session.query(marco.outcome,marco.stim_name).filter(marco.stim_name == stim, marco.outcome=='wrong_port').all()
                        hits_outcomes.append(len(hits)+len(errors))
                        wrongs_outcomes.append(len(wrongs))

                    results = session.query(marco.trial_number,marco.correct_side).all()
                    for result in results:
                        trial.append(result[0])
                        side.append(result[1])

                

        
        rat_dict[rat.lower()]= {
            "trial":trial,
            "side":side,
            "hits":hits_outcomes,
            "wrong":wrongs_outcomes
        }
                 

    data = [rat_dict]


    return jsonify(data)

    


    


if __name__ == "__main__":
    app.run(debug=True)
