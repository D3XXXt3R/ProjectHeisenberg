import re


class Check:
    def checkLetters(self, seq):
        i = 0
        chars = ['A', 'C', 'G', 'U']
        while i < len(chars):
            if chars[i] not in seq:
                return True

    def checkNumbers(self, seq):
        if re.findall('\d+', seq):
            return True

    def checkLength(self, seq):
        if ("." in seq and len(seq) < 10) or (len(seq) < 3 and not ("." in seq)) \
            or (len(seq) < 6 and not (("(" in seq) or (")" in seq)))
