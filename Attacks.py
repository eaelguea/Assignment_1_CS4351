import hashlib as hash  # hashlib for SHA1 and SHA256 algorithms
from itertools import product  # itertools for product and iteration through files and permutations
from string import ascii_letters, digits  # string for permutations and combinations


class attacks:
    def __init__(self, test_file, hash_pos, salt=-1, word_list=None, word_len=0):
        if word_list is None:
            word_list = []
        self.word_list = word_list
        self.test_file = test_file
        self.salt = salt
        self.hash_pos = hash_pos
        self.word_len = word_len
        self.passwords = []

    def attack(self):
        if not self.word_list:
            self.randAttack()
        else:
            self.dictAttack()

    # grabs the created user list and permutations list, performs the SHA256 -> SHA1 process, and checks for matches
    def randAttack(self):
        self.word_list = permutationsList(self.word_len)
        for i in range(len(self.test_file)):
            for line in self.word_list:
                sha256 = hash.sha256(line.strip().encode('utf-8')).hexdigest()  # SHA256 the permutations
                sha1 = hash.sha1(sha256.encode('utf-8')).hexdigest().strip()  # SHA1 the previous result
                if sha1 == self.test_file[i][self.hash_pos].strip():  # check for a match
                    self.passwords.append([self.test_file[i][0], line])
                    break

    # grabs the created user dictionary and dictionary list, performs the SHA256 -> SHA1 process, and checks for matches
    def dictAttack(self):
        for i in range(len(self.test_file)):
            for line in self.word_list:
                # SHA256 the original hash
                sha256 = hash.sha256(f"{line.strip()}{self.test_file[i][self.salt].strip()}".encode('utf-8')).hexdigest()
                sha1 = hash.sha1(sha256.encode('utf-8')).hexdigest().strip()  # SHA1 the previous result
                if sha1 == self.test_file[i][self.hash_pos].strip():  # check for a match
                    self.passwords.append([self.test_file[i][0], line])  # adds the matching word to the passwords list
                    break

    def printPasswords(self):
        for line in self.passwords:
            print(f"Username: {line[0]},  Password: {line[1]}")


# creates the permutation list for the random/brute force attack
def permutationsList(i):
    permutations = []
    combination = ascii_letters + digits + "!@#$%^&*()_-=+~"
    for line in product(combination.strip(), repeat=i):
        permutations.append(''.join(line))
    return permutations

