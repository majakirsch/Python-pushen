pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    
    # der erste Buchstabe vom Wort
    first = word[0]
    
    # das Wort plus dem  Anfangsbuchstaben des Wortes und der Endung ay
    new_word = word + first + pyg
    
    # das Wort angefangen beim zweiten Buchstaben bis zum Ende plus die Endung Anfangsbuch     staben des Wortes und ay 
    new_word = word[1:len(new_word)] + word[0] + pyg

    # zweite new_word Variable wird angezeigt
    print new_word
    
else:
    print 'empty'