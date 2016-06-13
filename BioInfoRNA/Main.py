from selenium import webdriver
from Check import Check
from bs4 import BeautifulSoup
from tkinter import filedialog, Tk


class Main:
    C = Check()
    sequence = ""
    counter = 0
    # browser = webdriver.Chrome("C:/Users/Dante/Desktop/chromedriver.exe")
    browser = webdriver.PhantomJS("C:/Users/Dante/Desktop/phantom/bin/phantomjs")
    browser.get("http://rnafrabase.cs.put.poznan.pl")
    button = browser.find_element_by_name("send")
    text1 = browser.find_element_by_id("sequences")
    names = ("No.", "PDB id", "NDB id", "Sequence", "Secondary Structure",
             "Chain", "Start", "End  ", "Method", "Class", "PDB deposition", "Å", "Models")

    print("Upload structure from file?")
    upload = input()
    if upload.lower() == "yes":
        root = Tk()
        root.fileName = filedialog.askopenfilename()
        root.destroy()
        fileIn = open(root.fileName, 'r', encoding='utf-8')
    flag = 1
    lines = []
    while True:
        text1.clear()
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

    tmp = browser.page_source
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print("Do you want to save data to a file?")
    answer2 = input()
    if answer2.lower() == "yes":
        root = Tk()
        root.fileName = filedialog.askopenfilename()
        root.destroy()
        fileOut = open(root.fileName, 'w', encoding='utf-8')
    for row in (soup.find_all(attrs={"class": ["row_table1", "row_table2"]})):
        for i in row.find_all("td"):
            if counter == 14:
                counter = 0
            if counter % 13 == 0 and counter != 0:
                sequence += " "
                counter += 1
                if answer2.lower() == "yes":
                    fileOut.write(sequence + "\n")
                else:
                    print(sequence)
                sequence = ""
            elif not i.text == "" or (names[counter] == "Å") or sequence == " ":
                sequence += names[counter] + " " + i.get_text('\n' + names[counter] + " ").strip()
                counter += 1
                if answer2.lower() == "yes":
                    fileOut.write(sequence + "\n")
                    sequence = ""
                else:
                    print(sequence)
                sequence = ""
    if answer2.lower == "yes":
        fileOut.close()
