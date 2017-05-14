from flask import Flask
from flask import render_template
from flask import request

from watson_developer_cloud import ConversationV1
import json
import pyaudio
import speech_recognition as sr

import json
import simplejson as sjson

from Bot import speecher 

hackbuddyapp=Flask(__name__, static_url_path = "/static", static_folder="static")

backend_score = { "C++" :3, "Python":3, "Django":3}
frontend_score = { "Ruby on Rails" :3, "JS":3, "Bootstrap": 3, "CSS":3}

@hackbuddyapp.route('/')
def default():
  return render_template("index.html")

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

@hackbuddyapp.route('/Profile', methods=['POST'])
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

      if "Hackathons" in request.form:
        user_credentials[email]["AttendedOtherHackathons"]=request.form["Hackathons"]

      if "Teammates" in request.form:
        user_credentials[email]["Teammates"]=request.form["Teammates"]

      if "number" in request.form:
        user_credentials[email]["NumberofHackathons"]=request.form["number"]

      if "OtherHackathons" in request.form:
        user_credentials[email]["OtherHackathons"]=request.form["OtherHackathons"]

      user_credentials[email]["Technologies"]= request.form.getlist("Technologies")
      user_credentials[email]["API"]=request.form.getlist("API")
      user_credentials[email]["Languages"] = request.form.getlist("Languages")
     
      fs=0
      bs=0

      for skill in user_credentials[email]["Technologies"]:
        if skill in backend_score:
          bs=bs+ backend_score[skill]
        if skill in frontend_score:
          fs=fs+ frontend_score[skill]
      
      for skill in user_credentials[email]["API"]:
        if skill in backend_score:
          bs=bs+ backend_score[skill]
        if skill in frontend_score:
          fs=fs+ frontend_score[skill]

      for skill in user_credentials[email]["Languages"]:
        if skill in backend_score:
          bs=bs+ backend_score[skill]
        if skill in frontend_score:
          fs=fs+ frontend_score[skill]

      user_credentials[email]["Backend_score"] = bs
      user_credentials[email]["Frontend_score"] = fs

  with open('user_credentials.json', 'w') as datafile:
    json.dump(user_credentials, datafile)
  return render_template('Profile.html')
 
@hackbuddyapp.route('/chat',methods=['POST', 'GET'])
def chat():
  sp = speecher()
  if request.method == "GET" :
    msg=sp.voice()
    print msg

  return render_template('chat.html')

@hackbuddyapp.route('/speak')
def speak():
  if request.method=="POST":
    msg=voice()
  return msg
  return render_template('chat.html')


#def call():
#  client = nexmo.Client#(
#           key=API_KEY,
#           secret=API_SECRET,
#           application_id=APPLICATION_ID#,
#           private_key=PRIVATE_KEY
#    )

#    response = client.create_call({
#      'to': [{'type': 'phone', 'number': TO_NUMBER}],
#      'from': {'type': 'phone', 'number': FROM_NUMBER},
#      'answer_url': ['https://nexmo-community.github.io/ncco-examples/first_call_talk.json']
#    })


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
