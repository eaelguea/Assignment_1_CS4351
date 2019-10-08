class DictionaryBuild:

    # defines the file and dictionary list that will be used in this program
    def __init__(self, file):
        self.file = file
        self.dict = []

    # builds the dictionary list by splitting at each white space
    def makeDictList(self, split=""):
        f = open(self.file, "r")
        for line in f:
            line = line.strip()
            if split is "":
                self.dict.append(line)
            else:
                self.dict.append(line.split(split))

    def getDictionary(self):
        return self.dict
