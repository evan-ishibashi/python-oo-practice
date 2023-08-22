class WordFinder():
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,path):
        self.words = None

        self.assign_attribute_words(path)

    def assign_attribute_words(self,path):
        """"""

        file = open(path)
        word_list = []

        for line in file:
            word_list.append(line)

        self.words = word_list
        print(f"{len(word_list)} words read")

        file.close()

    def random(self):
        from random import randrange

        index = randrange(len(self.words))

        rand_word = self.words[index]
        return rand_word