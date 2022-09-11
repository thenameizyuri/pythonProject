import requests
import pyttsx3

word_srch = input('Enter the word to get meaning: \n')
api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word_srch
meaning_word = requests.get(api_url).json()

definition = meaning_word[0]["meanings"][0]["definitions"][0]['definition']
audio = pyttsx3.speak(word_srch)
audiodef = pyttsx3.speak(definition)
print(definition,audio,audiodef)