#mensaje de bienvenida.
print("Hello, let's play hangman!")
#tengo que especificar el grupo al que pertenecen las palabras, si no sería un grupo
#infinito, dar el hint para que sepan mas o menos que palabras son.
from src import my_dictionary as my_dict
#random para que elija una palabra al azar dentro de de "house" y empiece a jugar. 
import random
word_to_guess = random.choice(my_dict.house)
#stages del juego, mostrara todas las posibilidades del muñequito.
fail_1 = '''
            ___
           |
           |
           |
           |
        ___|___
'''
fail_2 = '''
            ___    
           |   O
           |
           |
           |
        ___|___
'''
fail_3 = '''
            ___    
           |   O
           |   | 
           |   |
           |
        ___|___
'''
fail_4 = '''
            ___    
           |   O
           | / | 
           |   |
           |
        ___|___
'''
fail_5 = '''
            ___    
           |   O
           | / | \/
           |   |
           |
        ___|___
'''
fail_6 = '''
            ___    
           |   O
           | / | \/
           |   |
           |  /
        ___|___
'''
fail_7 = '''
            ___    
           |   O
           | / | \/
           |   |
           |  / \/
        ___|___
'''
#el juego itself.
choosen_word = "*" * len(word_to_guess) 
hang = True
letters_already_choosen = []
words_already_choosen = []
to_lose = 7
lost_rounds = 0
print("Hint: house")
while (hang):
    #pedirá una letra a usuario y la devolvera el lower, por si el usuario la escribe en upper.
    w = input("Your letter is: ").lower()
    if (lost_rounds < to_lose):
        if (len(w) == 1) and (w.isalpha()):
            if (w in letters_already_choosen):
                print("You've already chosen that letter")
                print(choosen_word)
                #print(lost_rounds)
            elif (w not in word_to_guess):
                print("Ups!")
                lost_rounds += 1
                letters_already_choosen.append(w)
                print(choosen_word)
                #print(lost_rounds)
            else:
                print("Yas!")
                letters_already_choosen.append(w)
                #print(letters_already_choosen)
                index_list = []
                for index,letter in enumerate(word_to_guess):
                    if letter == w:
                        index_list.append(index)
                        #print(index_list)
                #print(word_to_guess)
                choosen_word_list = list(choosen_word)
                #print(choosen_word_list)
                for index in index_list:
                    choosen_word_list[index] = w
                    #print(choosen_word_list)
                choosen_word = "".join(choosen_word_list)
                print(choosen_word)
                #print(lost_rounds)
        elif (len(w) == len(word_to_guess)) and (w.isalpha()):
                if (w in words_already_choosen):
                    print("You've already chosen that word")
                    print(fail_0)
                    print(choosen_word)
                    #print(lost_rounds)
                elif (w != word_to_guess):
                    print("Ups, that's not the word!")
                    words_already_choosen.append(w)
                    lost_rounds += 1
                    print(choosen_word)
                    #print(lost_rounds)
                else:
                    print("Yas, that's the word! You won!")
                    #creí que con esto pararía el loop pero no :( es imparable
                    hang == False
        else:
            print("Sorry, you must choose a letter")
        if (lost_rounds == 1):
            print(fail_1)
        elif (lost_rounds == 2):
            print(fail_2)
        elif (lost_rounds == 3):
            print(fail_3)
        elif (lost_rounds == 4):
            print(fail_4)
        elif (lost_rounds == 5):
            print(fail_5)
        elif (lost_rounds == 6):
            print(fail_6)
        elif (lost_rounds ==7):
            print(fail_7)
            print("HAHA, you lose!\nWord was: ", word_to_guess) 
        else:
            print("-----")
