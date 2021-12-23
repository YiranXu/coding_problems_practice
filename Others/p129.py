#P-1.29 from Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser-Data Structures and Algorithms in Python-Wiley (2013).pdf
#Write a Python program that outputs all possible strings formed by using
#the characters c , a , t , d , o ,and g exactly once.

def words(letters, word=''):
    letters or print(word)
    for letter in letters:
        print("letters",letters)
        print("letter",letter)
        words(letters - {letter}, word + letter)

words(set('catdog'))