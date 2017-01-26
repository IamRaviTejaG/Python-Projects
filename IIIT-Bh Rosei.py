from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

browser.get = ("https://172.16.2.200:8081/rosei/login.jsp")
print ("Welcome to Rosei Automation Tool\n\n")
x = raw_input("Input R1 for Roseighara-1 and R2 for Roseighara-2: ")
username = "B2160XX" #Edit the username and password fields before proceeding.
paword = "password"


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
