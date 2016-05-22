from selenium import webdriver
from BioInfoRNA.MyHTMLParser import MyHTMLParser
import re


browser = webdriver.PhantomJS("C:/Users/Dante/Desktop/phantom/bin/phantomjs")
browser.get("http://rnafrabase.cs.put.poznan.pl")
button = browser.find_element_by_name("send")
text1 = browser.find_element_by_id("sequences")
text1.clear()
text1.send_keys(">strand1" +"\n")
text1.send_keys("(((.[[[[[[)))")
button.click()
stringer = browser.page_source

parser = MyHTMLParser()
stringer2 = parser.feed(stringer)






