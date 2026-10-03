#get the current directory
#import directory
#curr_dir =  os.path.dirname(__file__)

#json dump into Final JSON Data
#json.dump(d,open(cur_dir + "/FinalJsonData/" + coin + ".json", "w"))

import json
import requests

url = 'https://data.cdc.gov/resource/pwn4-m3yp.json'
req = requests.get(url)

'''#double check everything works
print(url)
print(req.text)'''

DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

params = {
    "$where": "state='UT' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
    "$order": "end_date ASC"
}
req = requests.get(BASE_URL, params=params)
#print(req.text)

new_cases_key = 'new_cases'

new_cases = []

#convert request txt to python data types
dict_full = json.loads(req.text)
#print(dict_full)

# pull out new cases
    #loop thorugh dictionaries and pull out new_cases
for item in dict_full:
    print('new_cases: ', item[new_cases_key])
    new_cases.append(float(item[new_cases_key]))
    print()

