#GREETING MESSAGE
def greeter (name):
    return "Hi " + str(name)


print(greeter("Michael"))


#CHECKING FOR EMPTINESS IN A STRING
def word_checker(word):
    if len(word) >= 1:
        return True
    else: return False    
    
    
print(word_checker(""))


#REMOVING EXTRA WHITESPACES
def space_remover(word):
    return " ".join(word.split())


print(space_remover(' I am        learning Python      bject        oriented     programming '))

word = "I am a python developer"
print(word)


#STRING REVERSAL
def reverser(word):
    return word[::-1]


print(reverser("I am a python developer"))


#DISPLAY NUMBER OF LETTERS
def number_of_letters(word):
    space_remover = "".join(word.split())
    print(space_remover)
    return len(space_remover)


print(number_of_letters("Python is wonderful"))


#CONCANTENATING TWO STRINGS
def string_concantenator(string_left, string_right):
    return str(string_left) + str(string_right)


print(string_concantenator("I am a python developer ", 3))
    
    
#DISPLAY TWO STRING WITH A WHITESPACE IN BETWEEN
def space_creator(string_left, string_right):
    return f"{string_left} {string_right}"


print(space_creator("I am a python developer", "my name is kayler"))


#CUTTING OUT A PART OF A STRING
def string_cutout(word):
    return word[slice(1,4)]    


print(string_cutout("I am a python developer"))


#REPLACING A LETTER WITH ANOTHER LETTER
phrase = "Somebody said something to Sara" 
new_word = phrase.lower()
print(new_word)
if "s" in new_word:
    print(new_word.replace("s","x"))