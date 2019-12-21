

import json , requests 

fname = "The file url"

def call_json_url(fname):
  """
  Function to load the json file from URL.
  Argument: str : fname
  return : dict: data
  
  """
    req = requests.get(fname)
    cont = req.content
    data = json.loads(cont)
    return data
