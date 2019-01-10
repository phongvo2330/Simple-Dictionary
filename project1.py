import json
import difflib
from difflib import get_close_matches
from difflib import SequenceMatcher
data = json.load(open("data.json"))
def translate(w):
    w.lower()
    if w in data:
        return(data[w])
    elif w.title() in data:
        return (data[w.title()])
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead ? Enter Y if Yes or N if No \n" % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please enter another word."
        else:
            return "Please enter Y or N"
    else:
        return "No results found with your word."
word = input("Enter your word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
