from random import randint
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
dig1 = randint(0,9)
dig2 = randint(0,9)
dig3 = randint(0,9)
dig4 = randint(0,9)
dig5 = randint(0,9)
dig6 = randint(0,9)
dig7 = randint(0,9)
dig8 = randint(0,9)
dig9 = randint(0,9)

total = (dig1 * 10) + (dig2 * 9) + (dig3 * 8 ) + (dig4 * 7) + (dig5 * 6) + (dig6 * 5 ) + (dig7 * 4) + (dig8 * 3) + (dig9 * 2 )
divisao = total % 11

if (divisao < 2):
	dig10 = 0
else:
	dig10 = 11 - divisao

total2 = (dig1 * 11) + (dig2 * 10) + (dig3 * 9 ) + (dig4 * 8) + (dig5 * 7) + (dig6 * 6 ) + (dig7 * 5) + (dig8 * 4) + (dig9 * 3 ) + (dig10 * 2 )
divisao2 = total2 % 11
if(divisao2 < 2):
	dig11 = 0
else:
	dig11 = 11 - divisao2

cpf = str(dig1) + str(dig2) + str(dig3) + "." + str(dig4) + str(dig5) + str(dig6) + "." + str(dig7) + str(dig8) + str(dig9) + "-" + str(dig10) + str(dig11)

#print("CPF Gerado: %s " % cpf)
 
 
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r"C:\\geckodriver.exe")
driver.get('https://www.netflix.com/signup/regform')
driver.find_element_by_css_selector("div.submitBtnContainer").click()
time.sleep(1)
driver.find_element_by_css_selector("div.submitBtnContainer").click()
time.sleep(1)
driver.find_element_by_css_selector("div.submitBtnContainer").click()

campo_email = driver.find_element_by_id('id_email')
campo_email.send_keys('54655575727@gmail.com')
time.sleep(2)
campo_senha = driver.find_element_by_id('id_password')
campo_senha.send_keys("senhadonet")
time.sleep(2)
driver.find_element_by_css_selector("div.submitBtnContainer").click()
time.sleep(1)
driver.get('https://www.netflix.com/signup/directdebitoption')
time.sleep(1)
campo_nome = driver.find_element_by_id('id_firstName')
campo_nome.send_keys("Lucas")
time.sleep(1)
campo_sobrenome = driver.find_element_by_id('id_lastName')
campo_sobrenome.send_keys("Fernandes")
time.sleep(1)
campo_cpf = driver.find_element_by_id('id_customerIdentification')
campo_cpf.send_keys(cpf)
time.sleep(1)
""""

select = driver.find_element_by_css_selector('nfSelectPlacement')
select.select_by_value("001")
time.sleep(1)
#campo_operacao = driver.find_element_by_css_selector('div.nfSelectPlacement')
#campo_operacao.click()
driver.find_element_by_css_selector()
time.sleep(1)
"""
campo_agencia = driver.find_element_by_id('id_branchCode')
campo_agencia.send_keys("432424242")
time.sleep(1)
campo_conta = driver.find_element_by_id('id_accountNumber')
campo_conta.send_keys("4002")