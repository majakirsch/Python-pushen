pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = word[1:len(new_word)] + word[0] + pyg
    print original
    print new_word
else:
    print 'empty'