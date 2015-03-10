#Extremely simple hash code.

def hash(word):
  h = 0
  for letter in word:
    h += ord(letter)
  return h
  
"""This is flawed because certain words can give the same hash value"""
