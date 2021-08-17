#Here are my notes on what have I learned on Udemy on How to manipulate string in python.

#example sentence
sentence = "I lOvE wiNe and CheeSe. I lOvE tO swim Too."

print(sentence)
# prints the variable sentence

print(sentence.lower())
# lowercase all the letters. the string will now print as "i love wine and cheese. i love to swim too."

print(sentence.upper())
# uppercase all the letters

print(sentence.islower())
# checks if the letters are all in lowercase. 
# It will print "False", letters are not all in lowercase. 

print(sentence.isupper())
# checks if the letters are all in uppercase.
# prints "False", letters are not all in uppercase

print(sentence.lower().islower())
# lowercase all the letters in the sentence and checks if all letters are all in lowercase.
# prints "True" 

print(len(sentence))
# counts the letters 

print(sentence.replace("CheeSe","siSig"))
# replace the word "CheeSe" into "siSig"
# prints "I lOvE wiNe and siSig. I lOvE tO swim Too."

print(sentence.index("and"))
# counts where the sentence or letter is found.

########################################################################
#display string in f format 
store_street = "Ayala Blvd."
City="Ermita, Manila"
Country = "Philippines"

print(store_street + City + Country) #prints string in traditional way
address = f'{store_street}\n{City}\n{Country}' #f format
print(address)

num_vegetables = 3
num_fruits =4
print(f"I eat {num_vegetables} vegetables and {num_fruits} fruits everyday")

############################################################################

#choosing what phrase will print using slice operator
science = 'Earth revolves around the sun'
print(science[6:14]) #can also use science[slice(6,14)] 
#prints "revolves"
print(science[-3:])
#prints "sun"


s='main 200 banana khaye'
print(s.replace("banana", "samosa").replace('200','10'))
