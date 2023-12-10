import datetime, os, app
from flask import Flask

from replit import db
# Existing code...

# Existing code...


def getChat():
  message = ""
  filepath = os.path.join(app.root_path, "templates", "message.html")
  try:
    with open(filepath, "r") as f:
      message = f.read()
  except FileNotFoundError:
    return "Message template not found"

  keys = db.keys()
  keys = list(keys)
  result = ""
  recent = 0
  for key in reversed(keys):
    myMessage = message
    myMessage = myMessage.replace("{username}", db[key]["username"])

    # Convert timestamp to a readable date and time format
    timestamp = float(key)
    date_time = datetime.datetime.fromtimestamp(timestamp).strftime(
      '%Y-%m-%d %H:%M:%S')

    myMessage = myMessage.replace("{timestamp}", date_time)
    myMessage = myMessage.replace("{message}", db[key]["message"])
    result += myMessage
    recent += 1
    if recent == 5:
      break
  return result


# Remaining code...
