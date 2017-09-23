"""
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." So "Python" becomes "ythonpay.", “Egg” becomes “ggeay” To write a Pig Latin translator in Python, here are the steps we'll need to take:
1.	Ask the user to input a word in English.
2.	Make sure the user entered a valid word (check if the word has characters and is not blank).
3.	Convert the word from English to Pig Latin (moves first letter to the end and add ay).
4.	Display the translation result (print the output of word after translation).
"""

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
    print 'empty'