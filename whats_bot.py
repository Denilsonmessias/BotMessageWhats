from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r'C:\Python310\chromedriver.exe')

driver.get('https://web.whatsapp.com/')
time.sleep(30)

contatos = ['Hi']
mensagem = 'Olá, tenha um ótimo dia!'

def search_contact(contact):
    search = driver.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    time.sleep(5)
    search.click()
    search.send_keys(contact)
    search.send_keys(Keys.ENTER)

def sent_message(message):
    field_message = driver.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    time.sleep(5)
    field_message.click()
    field_message.send_keys(message)
    field_message.send_keys(Keys.ENTER)

for contato in contatos:
    search_contact(contato)
    sent_message(mensagem)