import sys
from random_word import RandomWords
import threading as th
import Hangman_Visuals


def game_start():
    start = input("Press enter to start the game.")
    if start == "\n":
        word_length = int(input("How long do you want the word to be? (Input length of the word)"))
        start_guess(word_length)


def start_guess(length: int):
    words = open("dictionary.txt").read().splitlines()
    words = [i for i in words if len(i) == length]
    while True:
        guess = guess_letter()
        words = word_family(words, guess)


def word_family(dictionary: list, guess: str):
    count_dict = {num: [] for num in range(len(max(dictionary, key=len)))}

    for i in dictionary:
        count_dict[i.count(guess)].append(i)

    longest = max(len(count_list) for count_list in count_dict.values())
    longest_word_list = [word_list for word_list in count_dict.values() if len(word_list) == longest]

    return longest_word_list


def guess_letter():
    guess = input("Enter your guessed letter: ")
    if len(guess) != 1 or guess.isnumeric() or any(i.isdigit() for i in guess) or any(not i.isalnum() for i in guess):
        print("Invalid guess.")
        guess_letter()
    else:
        return guess


if __name__ == "__main__":
    pass
