'''--------Notes---------
JSON: JavaScript Object Notation
key in json has to be a string
key in dictioaries can be any mutible type

#review:
mutable: changable 
- lists
- dict
- set
- bytearray

immutable: unchangable 
- string
- floats
- int
- complex
- bool
- tuple
- frozenset
- bytes



Immutable Ex: 
name = "andy"
print(id(name)) 
#python interperater doesn't go thorugh and change the memory, it gets new memory
name = 'esther'
print(id(name))
#if i reassign the variable back to the origional, it doesn't create new memory, it grabs the old memory
name = "andy"
print(id(name)) 
input(pause)
'''

#loop through them and print out first names output should be: jon anna peter
dct = {
    'employees': [{'firstName' : "Jon", 'lastName':"Doe"},
    {'firstName' : "Anna", 'lastName':"Smith"},
    {'firstName' : "Peter", 'lastName':"Jones"},]
}

# make sure I can print at least 1
# print(dct["employees"][0]['firstName'])

for employee in dct['employees']:
    print(employee['firstName'])

#input("Pause")


'''----------Web JSON API Duck example:----------'''
import json
import requests

example_url = "https://api.datamuse.com/words?ml="

word = "duck"

url = example_url + word
print(url)

request = requests.get(url)
dct_full = json.loads(request.text)

print(dct_full)
print()
print()

for item in dct_full:
    if item['word'] == 'dunk':
        print(item['score'])
print()
print()
'''
#part 2 - smthing wrong here figure it out
word = 'aggies'
key_word = 'word'
key_score = 'score'
search_word = 'usu'

url = 'https://api.datamuse.com/words?ml=' + word
print(url)
print()
print()


dct_full = json.loads(request.text)
print(dct_full)


for dct in dct_full:
    if dct['word'] == search_word: 
        val = dct['score']
print(val)'''


#practice again lol
#how much is it to buy 1 solana coin in USD
import requests
import json

url = 'https://api.coingecko.com/api/v3/coins/solana/history?date=23-09-2026&localization=false'

key_md = 'market_data'
key_cp = 'current_price'
key_usd = 'usd'

req = requests.get(url)
d = json.loads(req.text)

print(d[key_md][key_cp][key_usd])