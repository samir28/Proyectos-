import operator

#get each word - turn to lower case (.lower())
#count duplicates of words
#dictionary {word: count, word2: count2}
#sort this based on most used word
#print the top 20 words

def sorted_dict(d, reverse = True):
         return sorted(d.iteritems(), reverse = reverse, \
                       key = operator.itemgetter(1))

def rank_word_from_file(f):
         """
         take in a file, then rank all the words within the file
         args: a file
         return: a dictionary of all the word as the key and the ranking as the value
         """

         word_dict = {}
         words = []

         for line in f:
                  list_of_word = line.split()
                  for w in list_of_word:
                           word.append(w.lower())
         
         for word in words:
                  if word_dict.has_key(word):
                           word_dict[word]+= 1
                  else:
                           word_dict[word] = 1

         return word_dict

def main():
         #title
         print("the word game")
         print("="*30)
         print(" ")

         #game setup
         f = open('alice.txt', 'rU')
         print("loading words...")
         orig_ranked_word_dict = rank_word_from_file(f)
         f.close()

         print("loading complete")
         print("game starting")
         print(" ")

         #game loop
         while True: #loop for each game
                  #determine what the round limits is
                  while True:
                           try:
                                    round_limit = int(input("choose game length, how many round?[enter a number larger then 0]:"))
                                    
                                       if int(round_limit) <= 0:
                                                
                                                print("answer must be more than 0, please try again")
                                                print(" ")

                                      else:
                                               
                                                break
                           except:
                                    
                                    print("an error occured, make sure you enter an integer")
                                    print(" ")

                  #setup initial variables
                  point = [0,0]
                  cur_player = 1
                  cur_word = " "
                  cur_round = 1
                  round_over = False

                  #important create a copy of the dictionary
                  ranked_word_dict = orig_ranked_word_dict.copy()

                  while True: #loop for each round
                           print("round", cur_round)
                           print("player 1: %d", "player 2: %d" % (point[0], point[1]))
                           print(" ")
                           print(" ")

                  while True: #loop for each word
                           if len(cur_word) > 0:
                                    print(" ")
                                    print(" ")
                                    print(" "*5) + 'Current string = %s' % cur_word
                                    print(" ")

                           #get the new letter
                           new_letter = str(input("player %d, please enter a letter: " % cur_player))
                           if len(new_letter) > 1:
                                    new_letter = new_letter[0]

                           #add it to the current word
                           cur_word = str(cur_word) + str(new_letter).lower()

                           #check if word in ranked word dict
                           potential_word = False
                           for key, value in ranked_word_dict.items()
                           #found = re.match((str(cur_word), str(key))
                           if len(cur_word) <= len(key) and str(cur_word)== str(key[:len(cur_word)]):
                                    potential_word = True
                           if str(cur_word) == str(key) and len(cur_word) > 3:
                                    round_over = True
                                    round_points = value
                                    del ranked_word_dict[key]

                           #check if the cur_word is not valid using the variable potential_word
                           if potential_word == False:
                                    round_over = True
                                    round_points = int(5)

                                    print(" ")
                                    print(" ")
                                    print("%s - will not make valid word, player %d lost that round!!" % \
                                          (cur_word, cur_player))


                                    #check if round_over is true
                                    if round_over:
                                             #statement to determine list position of winning player
                                             if cur_player == 2:
                                                      p = 0
                                                      winning_player = 1
                                             else:
                                                      p = 1
                                                      winning_player = 2

                                             #assign points to winning player
                                             point[p] += round_points

                                             print(" ")
                                             print("!#YAH#!"*10)
                                             print(" ")

                                             cur_word = " "
                                             #exit round

                                             break
                                    else:
                                             #change the player
                                             if cur_player == 1:
                                                      cur_player = 2
                                             else:
                                                      cur_player = 1

                                    #back inside of the rounds loop
                                    if cur_round == round_limit:
                                             print(" ")
                                             print("round limit reached")
                                             print(" ")
                                             print("player 1: %d  player 2: %d" % (points[0], points[1]))
                                             print(" ")
                                             print(" ")

                                             if points[0] > points[1]:
                                                      print("player 1 wins!!!!")
                                             elif point[0] < points[1]:
                                                      print("player 2 wins !!!")
                                             else:
                                                      print("it's a tie!!!")
                                             print(" ")
                                             break
                                    #back in the game loop
                                    user_input = str(input("type 'q' to quit or <any key> to play again: "))
                                    if user_input.lower() == 'q':
                                             break
                                    print(" ")
                                    print(" ")
                                    print("thank your playing")

if __name__== '__main__:
         main()

                                    

                                             
                                                      

                                    
                                    
                           


                                    
                           

                           
                           
                  




         



         

                           
