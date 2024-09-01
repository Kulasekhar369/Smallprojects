import random


print("Hangman")
Words_list=["apple", "book", "desk", "pen", "cat", "dog", "tree", "house", "car", "phone",
"computer", "laptop", "keyboard", "mouse", "chair", "table", "door", "window", "wall", "floor"]
chosen_word= random.choice(Words_list)
print(chosen_word)
guess=input("Guess a letter: ")
letter=""
for i in chosen_word:
    if(guess==i):
        letter+=i
    else:
        letter+="_"
print(letter)
