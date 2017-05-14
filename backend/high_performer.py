
import json



with open('user_credentials.json') as datafile:
  user_credentials=json.load(datafile)

backend_map = {}
frontend_map = {}
for user in user_credentials:
  backend_map[user]=user_credentials[user]["Backend_score"]
  frontend_map[user]=user_credentials[user]["Frontend_score"]

b_sort={}
b_sort=sorted(backend_map.items(), key=lambda x: x[1], reverse=True)
f_sort={}
f_sort=sorted(frontend_map.items(), key=lambda x: x[1], reverse=True)

print b_sort
print user_credentials
def highBackendPerformer():
  for user in b_sort:
    if (user_credentials[user[0]]["Teammates"] == "Yes"):
      
      return "Backend High Perfomer: " + user[0]
  return "" 

def highFrontendPerformer():
  for user in f_sort:
    if (user_credentials[user[0]]["Teammates"] == "Yes"):
      return "Frontend High Perfomer: " + user[0]
  return "" 

print highBackendPerformer()
print highFrontendPerformer()
