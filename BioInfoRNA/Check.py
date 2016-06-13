import re


class Check:
    def checkCharacters(self, seq):
        i = 0
        chars = ('A', 'C', 'G', 'U', 'R', 'Y', 'M', 'K', 'W', 'S', 'B', 'D', 'H', 'V', 'N',
                 '.', '(', ')', '[', ']', '{', '}', '<', '>', '?')
        while i < len(seq):
            if seq[i].upper() not in chars:
                return True
            i += 1

    def checkNumbers(self, seq):
        if re.findall('\d+', seq):
            return True

    def checkLength(self, seq):
        if ("." in seq and len(seq) < 10) or (len(seq) < 3 and not ("." in seq)) \
                or (len(seq) < 6 and not (("(" in seq) or (")" in seq))):
            return True

    def checkSize(self, list1):
        i = 0
        while i < (len(list1) - 1):
            if list1[i] > list1[i-1] or list1[i] < list1[i-1]:
                return True
