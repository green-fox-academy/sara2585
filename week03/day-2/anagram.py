from collections import Counter

class Anagram:
    def is_Anagram(self, str1, str2):
        str1_group = Counter(str1)
        str2_group = Counter(str2)
        n = 0
        if len(str1_group) == len(str2_group):
            for key in str1_group:
                if str1_group[key] ==str2_group[key]:
                    n += 1
                else:
                    return False
        else:
            return False
        if n == len(str1_group) ==len(str2_group):
            return True

anagram = Anagram()
print(anagram.is_Anagram("abc", "cab"))


            