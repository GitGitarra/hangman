#!/usr/bin/python3
import random
import sys
import os




def start():
    """Display menu start"""
    print("Want to play a game? Let's check if you can manage! ")
    print("Try to guess an European capital city name:")
    start_key = input("\nType 1 to start a game, 2 to exit. ")
    while start_key != "1" or start_key != "2":
        if start_key == "1":
            os.system('clear')
            user_choice()
        elif start_key == "2":
            sys.exit()
        start_key = input("\nType 1 to start a game, 2 to exit. ")


def user_choice():
    """User decides if guess letter or whole word"""
    print("\n \t \t \tYou have %d lifes! " % life)
    print("\n\t", " ".join(hidden))
    print("\nLetters used:%s" % "\t", ", ".join(not_in_word))
    choice = input("\nYou want 'letter' or whole 'word'? ").lower()
    if choice == "letter":
        os.system('clear')
        user_letter()
    elif choice == "word":
        os.system('clear')
        user_word()
    else:
        os.system('clear')
        user_choice()


def user_letter():
    """Checking if user input is valid"""
    print("\n \t \t \tYou have %d lifes! " % life)
    print("\n\t", " ".join(hidden))
    global letter
    print("\nLetters used:%s" % "\t", ", ".join(not_in_word))
    letter = input("\nLet's see if your letter is here! ").upper()
    if letter.isalpha() and len(letter) == 1:
        letter_script()
    else:
        os.system('clear')
        print("Only letters, and only one please. ", end="")
        user_letter()


def letter_script():
    """Checking if user letter is in guessing word, and showing it"""
    if letter in visible:
        for index, value in enumerate(visible):
            if letter == value:
                hidden[index] = value #if letter is in visible, add it to hidden
                os.system('clear')
        os.system('clear')
        print("It's here. ", end="")
        if visible == hidden: #always check if visible is same as hidden = win
            print("\n \t \t \tYou have %d lifes! " % life)
            print("\n\t", " ".join(hidden))
            print("\nLetters used:%s" % "\t", ", ".join(not_in_word))
            print("\nYou won! ")
            again()
        else:
            user_choice()
    else:
        not_in_word.append(letter)
        user_wrong()


def user_word():
    """Checking is user word is same as riddle"""
    print("\n \t \t \tYou have %d lifes! " % life)
    print("\n\t", " ".join(hidden))
    print("\nLetters used:%s" % "\t", ", ".join(not_in_word))
    word = input("\nTell me what's your guess?: ").upper()
    if word == (riddle):
        os.system('clear')
        print("\n \t \t \tYou have %d lifes! " % life)
        print("\n\t", " ".join(visible))
        print("\nLetters used:%s" % "\t", ", ".join(not_in_word))
        print("\nYou won! ")
        again()
    elif word != (riddle):
        user_wrong()


def user_wrong():
    """Decreasing lifes if user made mistake, checking if life>0"""
    global life
    life = life-1
    print("\n \t \t \tYou have %d lifes! " % life)
    if life > 0:
        os.system('clear')
        print("Not this time! ", end="")
        user_choice()
    elif life == 0:
        os.system('clear')
        print("\n \t \t \tYou have %d lifes! " % life)
        print("\n\t", " ".join(hidden))
        print("\nLetters used:%s" % "\t", ", ".join(not_in_word))
        print("\nGame over. You are hanging! ")
        again()


def again():
    """Asking if user want to play again"""
    play_again = input("\nMain menu or exit (m/x) ").lower()
    if play_again == "m":
        main()
    elif play_again == "x":
        sys.exit()
    else:
        print("I don't understand. ")
        again()


def main():
    """Creating all tabels and variables needed in game"""
    os.system('clear')
    global life, capitals, visible, riddle, hidden, not_in_word
    life = 5
    capitals = ["TIRANA", "YEREVAN", "VIENNA", "BAKU",
                 "MINSK", "BRUSSELS", "SARAJEVO", "SOFIA", "ZAGREB", "NICOSIA",
                 "PRAGUE", "COPENHAGEN", "TALLINN", "HELSINKI", "PARIS", "TBILISI",
                 "BERLIN", "ATHENS", "BUDAPEST", "REYKJAVIK", "DUBLIN", "ROME",
                 "ASTANA", "PRISTINA", "RIGA", "VADUZ", "VILNIUS", "LUXEMBOURG",
                 "SKOPJE", "VALLETTA", "CHISINAU", "MONACO", "PODGORICA", "AMSTERDAM",
                 "OSLO", "WARSAW", "LISBON", "BUCHAREST", "MOSCOW",
                 "BELGRADE", "BRATISLAVA", "LJUBLJANA", "MADRID", "STOCKHOLM", "BERN",
                 "ANKARA", "KYIV", "LONDON"]
    visible = [] #visible contain all charcters of a capital as seperate values
    riddle = random.choice(capitals)
    for item in riddle:
        visible.append(item)
    hidden = ["_" for letter in visible] #creates copy of visible but with '_'
    not_in_word = [] #table for used letters
    start()


if __name__ == "__main__":
    main()
