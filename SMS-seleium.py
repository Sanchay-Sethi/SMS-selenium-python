from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import openpyxl
import time
import sys
# check here for update
filex = openpyxl.load_workbook("Remove this text and type the source code of your excel file here like C:\\Users\\hunny\\Downloads\\abc.xlsx")
sh = filex["Sheet1"]

print("*************************************************************")
print("SMS sending program...")
print("*************************************************************")
print("\n")

print("Please enter the limit from excel file :")
st = int(input("1. Start point"))
ed = int(input("2. End point"))

#  Check here for update
driver = webdriver.Chrome(executable_path='Type location of your web driver here : like C:\\Users\\hunny\\Desktop\\whatsappbot\\chromedriver')
driver.get('https://messages.google.com/web/conversations')

time.sleep(8)
print("Successfully scanned.....")

time.sleep(3)
driver.find_element_by_xpath('/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/div/mw-fab-link/a').click()
time.sleep(8)

driver.find_element_by_xpath('/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/div/mw-new-conversation-start-group-button/button').click()
time.sleep(5)
count = 0
while(st<=ed):

    cl = sh.cell(st,1)
    element = driver.find_element_by_xpath('//*[@id="mat-chip-list-0"]/div/input')
    element.send_keys(cl.value)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/div/mw-contact-selector-button/button').click()
    # time.sleep(1)
    st+=1
    count+=1
time.sleep(2)
message = "Hey We are here with The Viral Voice (LPU's First E-Singing Reality show) Participate and Win Prizes upto INR5000 For more details Visit Now bit.ly/tvvf"
driver.find_element_by_xpath('/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/mw-new-conversation-sub-header/div/div[2]/mw-contact-chips-input/button').click()
time.sleep(16)
messend = driver.find_element_by_xpath('/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div/mws-message-compose/div/div[2]/div/mws-autosize-textarea/textarea')
messend.send_keys(message)
time.sleep(4)
driver.find_element_by_xpath('/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div/mws-message-compose/div/mws-message-send-button/button').click()
time.sleep(2)
print(f"{count} messages sent already..")

sys.exit() 