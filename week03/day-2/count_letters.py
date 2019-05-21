from collections import Counter

class CountLetters:
    def __init__(self, strings):
        self.strings = strings

    def countLetters(self):
        letter_dic = {}
        letter_dic = Counter(self.strings)
        return letter_dic



strr = CountLetters("Hello, world!")
print(strr.countLetters())