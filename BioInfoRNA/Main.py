from selenium import webdriver
from BioInfoRNA.Check import Check
from bs4 import BeautifulSoup
from tkinter import filedialog, Tk


class Main:
    C = Check()
    sequence = ""
    counter = 0
    elementNumber = 0
    # browser = webdriver.Chrome("C:/Users/Dante/Desktop/chromedriver.exe")
    checkList = []
    browser = webdriver.PhantomJS("C:/Users/Dante/Desktop/phantom/bin/phantomjs")
    browser.get("http://rnafrabase.cs.put.poznan.pl")
    button = browser.find_element_by_name("send")
    text1 = browser.find_element_by_id("sequences")
    names = ("No.", "PDB id", "NDB id", "Sequence", "Secondary Structure",
             "Chain", "Start", "End  ", "Method", "Class", "PDB deposition", "Å", "Models")

    while True:
        print("Upload structure from file?")
        upload = input()
        if upload.lower() == "yes":
            root = Tk()
            root.fileName = filedialog.askopenfilename()
            root.destroy()
            fileIn = open(root.fileName, 'r', encoding='utf-8')
            break
        elif upload.lower() == "no":
            break

    flag = 1
    lines = []
    text1.clear()
    while True:
        if flag > 1:
            text1.send_keys("\n" + ">strand" + str(flag) + "\n")
        else:
            text1.send_keys(">strand" + str(flag) + "\n")
        if upload.lower() == "yes":
            text1.clear()
            seq = fileIn.read()
            fileIn.close()
            text1.send_keys(seq)
            button.click()
            break
        else:
            print("Please input sequence(s) and/or secondary structure(s) given in the dot-bracket notation")
            while True:
                seq = input()
                if seq:
                    lines.append(seq)
                    checkList.append(seq)
                else:
                    break
            seq = '\n'.join(lines)
            lines = []
        if C.checkIdentity(seq, flag, checkList) or C.checkNumbers(seq) or C.checkCharacters(seq) or C.checkLength(seq):
            # print("Sequence is too short or bad input")
            print("Please, try again")
            text1.clear()
        else:
            text1.send_keys(seq)
            while True:
                print("Next sequence?")
                answer = input()
                if answer.lower() == 'no':
                    url1 = "http://rnafrabase.cs.put.poznan.pl/index.php"
                    button.click()
                    url2 = str(browser.current_url)
                    if url1 == url2:
                        print("Bad input, please restart program")
                        quit()
                    else:
                        break
                elif not (answer.lower() == 'yes'):
                    print("Bad answer")
                if answer.lower() == 'yes':
                    flag += 1
            break

    # tmp = browser.page_source
    result = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print("Do you want to save data to a file?")
    answer2 = input()
    # C.mainAlg(answer2, soup, counter, sequence, names)

    while True:
        print("Please select what range of result do you want check")
        for row in (soup.find_all(attrs={"class": ["a2"]})):
            print("[" + str(elementNumber) + "] " + row.text)
            result.append(row.text)
            elementNumber += 1
        number = input()
        buttonC = browser.find_element_by_link_text(result[int(number)]).click()
        soup = BeautifulSoup(browser.page_source, "html.parser")
        C.mainAlg(answer2, soup, counter, sequence, names)
        print("Do you want more result?")
        answer3 = input()
        if answer3.lower() == "no":
            break
        else:
            elementNumber = 0
