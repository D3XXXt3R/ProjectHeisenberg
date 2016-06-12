import re


class Check:
    def checkLetters(self, seq):
        i = 0
        chars = ('A', 'C', 'G', 'U', 'R', 'Y', 'M', 'K', 'W', 'S', 'B', 'D', 'H', 'V', 'N')
        while i < len(seq):
            if seq[i].upper() not in chars:
                return True
            i += 1

    def checkCharacters(self, seq):
        i = 0
        signs = ('.', '(', ')', '[', ']', '{', '}', '<', '>', '?', '\n')
        while i < len(seq):
            if seq[i] not in signs:
                return True
            i += 1

    def checkNumbers(self, seq):
        if re.findall('\d+', seq):
            return True

    def checkLength(self, seq):
        if ("." in seq and len(seq) < 10) or (len(seq) < 3 and not ("." in seq)) \
                or (len(seq) < 6 and not (("(" in seq) or (")" in seq))):
            return True

    def checkResult(self, seq, seq2):
        counter = 0
        chars = ('C', 'G', 'U', 'A')
        numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        for i in seq:
            if (len(seq2) == 6 and not (seq2 == " ")):
                seq2 += " " + str(i)
            else:
                seq2 += str(i)
            counter += 1
        print(seq2)
