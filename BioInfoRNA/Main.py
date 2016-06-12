from selenium import webdriver
from ProjectHeisenberg.BioInfoRNA.MyHTMLParser import MyHTMLParser
from ProjectHeisenberg.BioInfoRNA.Check import Check
from bs4 import BeautifulSoup


class Main:
    C = Check()
    table = []
    sequence = ""
    counter = 0
    names = ("No.", "PDB id", "NDB id", "Sequence", "Secondary Structure",
             "Chain", "Start", "End  ", "Method", "Class", "PDB deposition", "Å", "Models")
    file = open('Text.txt', 'w', encoding='utf-8')
    browser = webdriver.PhantomJS("C:/Users/Dante/Desktop/phantom/bin/phantomjs")
    # browser = webdriver.Chrome("C:/Users/Dante/Desktop/chromedriver.exe")
    browser.get("http://rnafrabase.cs.put.poznan.pl")
    button = browser.find_element_by_name("send")
    text1 = browser.find_element_by_id("sequences")
    text1.clear()
    flag = 1
    lines = []
    while True:
        if flag > 1:
            text1.send_keys("\n" + ">strand" + str(flag) + "\n")
        else:
            text1.send_keys(">strand" + str(flag) + "\n")
        print("Please input sequence(s) and/or secondary structure(s) given in the dot-bracket notation")
        while True:
            seq = input()
            if seq:
                lines.append(seq)
            else:
                break
        seq = '\n'.join(lines)
        if C.checkNumbers(seq) and (C.checkLetters(seq) or C.checkCharacters(seq)):  # C.checkLength(seq)
            print("Sequence is too short or bad input")
            print("Please, try again")
        else:
            text1.send_keys(seq)
            print("Next sequence?")
            answer = input()
        if answer.lower() == 'no':
            break
        elif not (answer.lower() == 'yes'):
            print("Bad answer")
        if answer.lower() == 'yes':
            flag += 1

    button.click()
    tmp = browser.page_source
    soup = BeautifulSoup(browser.page_source, "html.parser")

    parser = MyHTMLParser()
    print("Do you want to save data to a file?")
    answer2 = input()
    for row in (soup.find_all(attrs={"class": ["row_table1", "row_table2"]})):
        for i in row.find_all("td"):
            if counter == 14:
                counter = 0
            if counter % 13 == 0 and counter != 0:
                sequence += " "
                counter += 1
                file.write(sequence + "\n")
                print(sequence)
                sequence = ""
            elif not i.text == "" or (names[counter] == "Å") or sequence == " ":
                sequence += names[counter] + " " + i.get_text('\n' + names[counter] + " ").strip()
                counter += 1
                if answer2.lower() == "yes":
                    file.write(sequence + "\n")
                    sequence = ""
                else:
                    print(sequence)
                    sequence = ""
    file.close()
