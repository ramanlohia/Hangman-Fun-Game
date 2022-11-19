import random
import hangman_art as art
import hangman_words as word
# Stages

print(art.logo)

stages = art.stages
word_list=word.word_list
end_of_game = False

randomNumber = random.randint(0,2)
chosen_word=word_list[randomNumber]
lives=6
display=[]

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')


for j in range(len(chosen_word)):
  display.append("_")
while not end_of_game:
  
  guess=input("Guess a letter : ").lower()

  if guess in display:
    print("You have already guessed that word, Don't Worry you won't lose a life")
  
  for i in range(len(chosen_word)):
  
    if chosen_word[i] == guess:
      display[i] = chosen_word[i]
    
  if guess not in chosen_word:

    print(f"This letter {guess} is not in the word. You lose 1  Life")
    
    lives=lives-1
    print(f"Remaining Lives - {lives}")
    
    if lives<=0:
      end_of_game=True
      print("\n********\nYou Lose\n********")
      
  print(f"{' '.join(display)}")
      
  if '_' not in display:
    end_of_game = True
    print("\n*******\nYou Win\n*******")
  print(stages[lives])