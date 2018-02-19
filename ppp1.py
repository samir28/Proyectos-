"""
#get each word - turn to lower case(.lower())
#count duplicates of words
#dictionary {word: count, word2: count2}
#sort this based on most used word
#print the top 20 words
"""

import operator

def rank_words(f):
    """
    takes in file, then ranks all the words within the file
    args: a file
    return: a sorted list of tuples
    """
    word_dict = {} #start with empty python dictionary
    word = [] #start with empty python list
    for line in f:
        list_of_words = line.split()
        for w in list_of_words:
            word.append(w.lower()) #add word to list

        for words in word:
            if word_dict.has_key(words):
                word_dict[words] += 1 #increment value in dict
            else:
                word_dict[words] = 1
        #this will sort the dictionary and return a list of tuples
        return sorted(word_dict.iteritems(), reverse = True, \
                      key = operator.itemgetter(1))
    
    

def main():
    #files
    f = open('Alice-text-file-For-Module-15-17-.txt', 'rU')
    ranked_words_list = rank_words(f)

    f.close()

    #print the result
    for w in list(ranked_words_list[:20]):
        print(w[0], "----", w[1])

if __name__== '__main__':
    main()
