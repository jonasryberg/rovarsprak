# coding=latin1
# Pythonskript för att skapa rövarspråk
# av Jonas Ryberg


print "Rövarspråksgenerator"



exit = "J"

while exit != "N" :
    woworordod = str()
    original = raw_input('Skriv in ett ord > ')

    if len(original) > 0 and original.isalpha():
    
        word = original.lower()
    
        letter_index = 0
    
        while letter_index <= len(word)-1:
    
            letter = word[letter_index]
    
            if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            
                woworordod = woworordod + letter
                letter_index = letter_index + 1
        
            else:
                woworordod = woworordod + letter + "o" + letter
                letter_index = letter_index + 1
            
            

    else:
        print 'inget ord eller mer än ett ord'
    
    print woworordod
    exit = raw_input("En gång till? (J/N) >")
    
    
