from watson_developer_cloud import ConversationV1
import json
import pyaudio
import speech_recognition as sr

class speecher:
 
  def _init_(self):
    with open('user_credentials.json') as datafile:
      self.user_credentials=json.load(datafile)

    self.workspace_id = '40b89b2f-4e14-4bad-ba82-b5226d56937f'
    global m_conversation
    m_conversation = ConversationV1(
                   username='2f13b192-ad4f-43bc-bce6-a76b5f05c156',
                   password='NEPAtJbjkDHu',
                   version='2017-04-21'
    )

    self.context = {}
    self.output = {}
    self.b_sort={}
    self.backend_map = {} 
    for user in user_credentials:
      backend_map[user]=user_credentials[user]["Backend_score"]
    b_sort=sorted(backend_map.items(), key=lambda x: x[1], reverse=True)
    f_sort={}
    frontend_map = {} 
    for user in user_credentials:
      frontend_map[user]=user_credentials[user]["Frontend_score"]
    f_sort=sorted(frontend_map.items(), key=lambda x: x[1], reverse=True)

    response = m_conversation.message(
      workspace_id=workspace_id,
      message_input={},
      context=context,
    )

  def highBackendPerformer(self):
    for user in b_sort:
      if (user_credentials[user[0]]["Teammates"] == "Yes"):
        new.append(user[0])
        return "Backend High Perfomer: " + user[0]
    return "I want a dev" 
			
  def highFrontendPerformer(self):
    for user in f_sort:
      if(user_credentials[user[0]]["Teammates"] == "Yes"):
        new.append(user[0])
        return "Frontend High Perfomer: "+ user[0] 
    return "I want a dev" 

  def voice(self):

    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
      audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
  
    try:
      print("You said " + r.recognize_google(audio))    # recognize speech using Google Speech Recognition
    except LookupError:                            # speech is unintelligible
      print("Could not understand audio")

    text2 = r.recognize_google(audio)
    response = m_conversation.message(
    workspace_id=workspace_id,
    message_input={'text':text2},
    context=response['context'],
  )

    new = response['output']['text']
    print response['intents']
    intent = response['intents'][0]['intent']
    entity = response['entities'][0]['entity'] 
    value = response['entities'][0]['value']
    if(intent == 'Find_Developer' and entity == 'Developers' and value == 'Back End Developer'): 


      highBackendPerformer()
    elif(intent  == 'Find_Developer' and entity == 'Developers' and value == 'Front End Developer'):
      highFrontendPerformer()
    return json.dumps(new, indent=2)

