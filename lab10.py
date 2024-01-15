# Prolog
# Kylie Orozco
# Purpose: translates english sentence to simple pig latin and more complex pig latin
# Pre-cond: user inputs english sentence (string)
# Post-cond: program outputs english into pig latin using simple terms then with more complex terms for version 2

# returns location of vowel that is closest to the left end of word, and -1 if no vowel present
def find_vowel(word:str):
    vowels = 'aeiou'
    i = 0
    index = -1
    found = False 
    while i < len(word) and not found:
        if word[i].lower() in vowels:
            index = i
            found = True 
        i += 1
    
    return index
        
# Version 1
def PigLatin1(english):
    words = english.split()
    # version 1
    new_sentence = ''
    vowels = 'aeiou'
    # loop through the words
    for word in words:
        # if the word starts with a vowel
        if word[0].lower() in vowels:
            # add 'way' to the end of the word
            new_sentence += word + 'way '
        else:
            # add 'ay' to the end of the word
            new_sentence += word[1:] + word[0] + 'ay '
    
    return new_sentence 
        
# Version 2
def PigLatin2(english):
    words = english.split()
    new_sentence2 = ''
    for word in words:
        # index of the first vowel
        index = find_vowel(word)
        # if no vowel
        if index == -1:
            new_sentence2 += word + 'ay '
        elif index == 0:
            # word starts with a vowel
            new_sentence2 += word + 'way '
        else:
            # starts with a consonant
            new_sentence2 += word[index:] + word[:index] + 'ay '
    
    return new_sentence2


def main():
    # print header
    print("Translate an English sentence to a Pig Latin sentence!");
    # input sentence
    sentence = input("Enter English sentence: ");    
    # print sentence
    print("English: ", sentence);
    # print new sentence
    print('PL Ver1: ', PigLatin1(sentence));
    # print 2nd pig latin sentence
    print('PL Ver2: ', PigLatin2(sentence));
main()
