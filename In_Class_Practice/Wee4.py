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
example_url = "https://api.datamuse.com/words?ml=duck"

import json
import requests

word = 'duck'
search_word = 'ducky'

#get all keys you need to extract data - notice that we don't need everything!
key_word = 'word'
key_score = 'score'

url = example_url + word
print(url)


request = requests.get(url)
dct_full = json.loads(request.text) #load s = load string --> turns all text into python dictionary

print(dct_full)
#input('pause')



'''programming activity'''
#print the word scroe associated with 'dunk'

example_url = "https://api.datamuse.com/words?ml=duck"

#import json
#import requests

word = 'duck'
search_word = 'dunk'

#get all keys you need to extract data - notice that we don't need everything!
key_word = 'word'
key_score = 'score'

url = example_url + word
print(url)


request = requests.get(url)
dct_full = json.loads(request.text)

print(dct_full)
input('pause')