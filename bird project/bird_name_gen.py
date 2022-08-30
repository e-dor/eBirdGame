import requests
import random
url = "https://api.ebird.org/v2/ref/taxonomy/ebird"

payload={}
params={'fmt': 'json'}
headers = {
  'X-eBirdApiToken': '{{x-ebirdapitoken}}'
}

response = requests.request("GET", url, headers=headers, data=payload, params=params)

def get_bird():
  if response.status_code == 200:
      taxonomy = response.json()
      bird_name_list = [i['comName'] for i in taxonomy]
      n = random.randint(0, len(bird_name_list)-1)
      return(bird_name_list[n])
  else:
      print("An error occurred.")
