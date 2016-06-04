from selenium import webdriver
from BioInfoRNA.MyHTMLParser import MyHTMLParser
from BioInfoRNA.Check import Check
from bs4 import BeautifulSoup
import re


class Main:
    C = Check()
    table = []
    sequence = ""
    file = open('Text.txt', 'w')
    browser = webdriver.PhantomJS("C:/Users/Dante/Desktop/phantom/bin/phantomjs")
    # browser = webdriver.Chrome("C:/Users/Dante/Desktop/chromedriver.exe")
    browser.get("http://rnafrabase.cs.put.poznan.pl")
    button = browser.find_element_by_name("send")
    text1 = browser.find_element_by_id("sequences")
    text1.clear()
    flag = 1
    while (True):
        if flag > 1:
            text1.send_keys("\n" + ">strand" + str(flag) + "\n")
        else:
            text1.send_keys(">strand" + str(flag) + "\n")
        print("Please input sequence(s) and/or secondary structure(s) given in the dot-bracket notation")
        seq = input()
        if C.checkLength(seq) or C.checkNumbers(seq) \
                or C.checkLetters(seq):
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
    if answer2.lower() == 'yes':
        for row in (soup.find_all(attrs={"class": ["row_table1", "row_table2"]})):
            list1 = row.text.splitlines()
            sequence = ''.join(list1)
            # print(str(len(row.text)) + "fsafasfasfas")
            file.write(row.text)
            print(' '.join(sequence.split()))
    else:
        parser.feed(tmp)
    file.close()
