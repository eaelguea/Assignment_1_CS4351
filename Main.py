#! /usr/bin/env python3
import time

from DictionaryBuild import DictionaryBuild
from Attacks import attacks


# dictionaryAttack() reads both a dictionary and user file and runs a dictionary attack to crack passwords
def dictionaryAttack():
    wordsList = DictionaryBuild("wordsEn.txt")  # sends the dictionary file to the dictionary class
    wordsList.makeDictList()  # calls dictionary class to read a dictionary file and store in a list

    test = DictionaryBuild("dictFile17.txt")  # sends the user file to the dictionary class
    test.makeDictList(",")  # calls dictionary class to read the user file and store in a list by split character

    # sends new lists and the two positions of the salt and hash for matching purposes
    dictAttack = attacks(word_list=wordsList.getDictionary(), test_file=test.getDictionary(), salt=1, hash_pos=2)

    print("--- Dictionary Attack ---")
    start = time.time()  # start time for attack
    dictAttack.attack()  # calls attack method to perform the right attack based on files present
    end = time.time()  # end time for attack
    total = end - start  # total elapsed time for the attack
    print(f"Total time: {total} seconds")
    dictAttack.printPasswords()  # prints the results of the attack


# randomAttack() performs a brute force approach to crack passwords
def randomAttack():
    test = DictionaryBuild("randFile17.txt")  # sends the user file to the dictionary class
    test.makeDictList(",")  # calls dictionary class to read the user file and store in a list by split character
    print("--- Random Attack ---")
    for i in range(1, 10):  # minimum length of a possible password is 1, max is 10
        # sends new lists and the position of the hash for matching purposes
        randAttack = attacks(test_file=test.getDictionary(), hash_pos=1, word_len=i)
        start = time.time()  # start time for attack
        randAttack.attack()  # calls attack method to perform the right attack based on files present
        end = time.time()  # end time for attack
        total = end - start  # total elapsed time for the attack
        print(f"Total time: {total} seconds")
        randAttack.printPasswords()  # prints the results of the attack


# play main methods for the attacks
if __name__ == "__main__":
    dictionaryAttack()
    print(' ')
    randomAttack()
