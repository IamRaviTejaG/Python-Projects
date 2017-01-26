from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

browser.get = ("https://172.16.2.200:8081/rosei/login.jsp") #The Rosei URL.
print ("Welcome to Rosei Automation Tool\n\n")

"""Inputs section. Input your username, password and preferred Roseighara for once."""
x = raw_input ("Input 'R1' for Roseighara-1 and 'R2' for Roseighara-2: ")
username = raw_input ("Enter your username: ")
paword = raw_input ("Enter your password: ")

"""Browser action starts here. Before editing, please refer the Selenium Documentation."""
uname = browser.find_element_by_name('un')
pword = browser.find_element_by_name('pw')
uname.send_keys(username)
pword.send_keys(paword)
browser.find_element_by_name('submit').click()
browser.find_element_by_link_text('Issue Coupon').click()
if (x == "R1"):
    browser.selectbyvisibletext('Roseighara-1').click()
elif (x == "R2"):
    browser.selectbyvisibletext('Roseighara-2').click()
