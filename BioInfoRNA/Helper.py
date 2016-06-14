import re
from tkinter import filedialog, Tk


class Helper:
    def check_characters(self, seq):
        i = 0
        chars = ('A', 'C', 'G', 'U', 'R', 'Y', 'M', 'K', 'W', 'S', 'B', 'D', 'H', 'V', 'N',
                 '.', '(', ')', '[', ']', '{', '}', '<', '>', '?', '\n')
        while i < len(seq):
            if seq[i].upper() not in chars:
                print("Invalid characters in sequence")
                return True
            i += 1

    def check_numbers(self, seq):
        if re.findall('\d+', seq):
            print("Invalid characters in sequence")
            return True

    def check_length(self, seq):
        chars = ('A', 'C', 'G', 'U', 'R', 'Y', 'M', 'K', 'W', 'S', 'B', 'D', 'H', 'V', 'N')
        braces = ('(', ')', '[', ']', '{', '}')
        if len(seq) < 11 and (seq.count(seq[0]) == len(seq)) and all(x == seq[0] for x in seq) and seq[0] == ".":
            print("Sequence too short")
            return True
        elif len(seq) < 4 and seq in chars:
            print("Sequence too short")
            return True
        elif len(seq) < 6 and (seq.count(seq[0]) == len(seq)) and all(x == seq[0] for x in seq) and seq[0] in braces:
            print("Sequence too short")
            return True

    def check_identity(self, seq, flag, list1):
        if seq in list1 and flag > 1 and not (seq == list1[len(list1)-1]):
            print("Incorrect pattern definition")
            return True
        else:
            return False

    def main_alghorithm(self, answer, soup, counter, sequence, names):
        if answer.lower() == "yes":
            root = Tk()
            root.fileName = filedialog.askopenfilename()
            root.destroy()
            file = open(root.fileName, 'a', encoding='utf-8')
        for row in (soup.find_all(attrs={"class": ["row_table1", "row_table2"]})):
            for i in row.find_all("td"):
                if counter == 14:
                    counter = 0
                if counter % 13 == 0 and counter != 0:
                    sequence += " "
                    counter += 1
                    if answer.lower() == "yes":
                        file.write(sequence + "\n")
                    else:
                        print(sequence)
                    sequence = ""
                elif not i.text == "" or (names[counter] == "Å") or sequence == " ":
                    sequence += names[counter] + " " + i.get_text('\n' + names[counter] + " ").strip()
                    counter += 1
                    if answer.lower() == "yes":
                        file.write(sequence + "\n")
                        sequence = ""
                    else:
                        print(sequence)
                    sequence = ""
        if answer.lower == "yes":
            file.write("\n")
            file.close()
