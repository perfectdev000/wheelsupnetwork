import os
import requests
import json

JSON_FILE = 'wheelsup_wordpress_files.json'
DIR_UPLOADS = 'uploads'

with open(JSON_FILE, 'r') as json_f:
  DATA_FILES = json.load(json_f)

for local_file, url in DATA_FILES.items():
  localPath = os.path.join(DIR_UPLOADS, local_file)
  #if not os.path.exists(localPath):
  #  os.makedirs(os.path.dirname(localPath), exist_ok= True)
  try:
      u = url.replace('http://wheelsupnetwork.com', 'https://wun.josesalinero.dev')
      u = u.replace('https://wheelsupnetwork.com', 'https://wun.josesalinero.dev')
      print("Downloading - %s" % u)
      r = requests.get(u, verify=False)

      if r.status_code == 200:
        with open(localPath, 'wb') as f:
            f.write(r.content)
      else:
        print(f"File not found {r.status_code}")
  except Exception as e:
      print(e)
      print("Error downloading - %s" % u)
