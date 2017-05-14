from flask import Flask
from flask import render_template
from flask import request

import json
import simplejson as sjson
hackbuddyapp=Flask(__name__)

with open('user_credentials.json') as datafile:
  user_credentials=json.load(datafile)

@hackbuddyapp.route('/')
def default():
  return render_template("default.html")

@hackbuddyapp.route('/welcome', methods=['POST', 'GET'])
def welcome():
  return render_template("sign_in.html")
 
@hackbuddyapp.route('/signin', methods=['POST', 'GET'])
def signIn():
  print request.path
  print request.form
  print request.method
  if request.method=="POST":
    email=request.form["inputEmail"]
    password=request.form["inputPassword"]
    if email in user_credentials:
      if(user_credentials[email]["password"] == password):
        return render_template("survey.htmL", email=email)
    else:
      return "Please Signup"

@hackbuddyapp.route('/fillSurvey', methods=['POST'])
def fillSurvey():
  print request.path
  print request.form
  survey = {}
  if request.method=="POST":
    if request.form["email"] in user_credentials:
      email=request.form["email"]
      if "Name" in request.form:
        user_credentials[email]["Name"]=request.form["Name"]
      if "Phonenumber" in request.form:
        user_credentials[email]["Phonenumber"]=request.form["Phonenumber"]

      user_credentials[email]["Technologies"]= request.form.getlist("Technologies")
      user_credentials[email]["API"]=request.form.getlist("API")
      user_credentials[email]["Languages"] = request.form.getlist("Languages")
  with open('new_user_credentials.json', 'w') as datafile:
    json.dump(user_credentials, datafile)
  return "Updated the Database" 
  

@hackbuddyapp.route('/meet', methods=['POST'])
def meet():
  SPACE_EFFICIENCY = 0.2
  ISS_SOLAR_PANEL_ACREAGE=2500
  if request.method=="POST":
    current_distance=request.form["Distance"]
    current_time=request.form["Time"]

  solar_radiation=SPACE_EFFICIENCY*(getBetaAngle(current_time)) \
                  * getSolarRadianceAtISS(current_distance)* ISS_SOLAR_PANEL_ACREAGE
  return render_template('default.html', solar_radiation=solar_radiation)