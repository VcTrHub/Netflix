import random 
from random import randint
from biblioteca import cpf
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.select import Select
import time
funcao = cpf()
cpf = funcao.gerar()
list_nome = ["Jose","Carlos",'Felipe','João','Fernando','Rafaela','Katianne','Pedro','Henrique','Rafaela','Felipe','Kakaroto','Hernandes','Franscico','Bolsonaro','Felipao','Hernandes','Doria','Dilma','Lula']
list_Sobrenome = ["Santos","Lima",'Silva','Roussef','Chagas','Teles','Moura','Pereira','Amado','Junior','Alvares','Penha','Barraco','Araujo','Alencar','Devilaque','Amaro','Nascimento']
nome = random.choice(list_nome)
sobrenome = random.choice(list_Sobrenome)
em1 = randint(0,1000)
em2 = randint(0,50)
email = "count" +  str(em1) + str(em2) + "@vctr.com"
senha = "senhadonet"
cdig1 = randint(0,9)
cdig2 = randint(0,9)
cdig3 = randint(0,9)
cdig4 = randint(0,9)
cdig5 = randint(0,9)
cdig6 = randint(0,9)
cdig7 = randint(0,9)
cdig8 = randint(0,9)
adig1 = randint(0,9)
adig2 = randint(0,9)
adig3 = randint(0,9)
adig4 = randint(0,9)
conta = str(cdig1) + str(cdig2) + str(cdig3) +  str(cdig4) + str(cdig5) + str(cdig6) + str(cdig7) + str(cdig8)
agencia = str(adig1) + str(adig2) + str(adig3) +  str(adig4)
soma = ((cdig1 * 9) + (cdig2 * 8) + (cdig3 * 7) + (cdig4 * 6 ) + (cdig5 * 5) + (cdig6 * 4) + (cdig7 * 3) + (cdig8 * 2) + 2 + (adig1 * 8) + (adig2 * 7) + (adig3 * 6) + (adig4 * 5)) * 10
divisao = soma // 11
dv = soma - divisao
if (dv >= 10):
	dv = 0
time.sleep(1)
binary = FirefoxBinary(".\\Firefox\\App\\Firefox\\firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r".\\geckodriver.exe")
driver.get('https://www.netflix.com/signup/regform')
driver.find_element_by_css_selector("div.submitBtnContainer").click()
time.sleep(1)
driver.find_element_by_css_selector("div.submitBtnContainer").click()
time.sleep(1)
driver.find_element_by_css_selector("div.submitBtnContainer").click()
time.sleep(1)
campo_email = driver.find_element_by_id('id_email').send_keys(email)
time.sleep(1)
campo_senha = driver.find_element_by_id('id_password').send_keys(senha)
time.sleep(1)
driver.find_element_by_css_selector("div.submitBtnContainer").click()
time.sleep(1)
driver.get('https://www.netflix.com/signup/directdebitoption')
time.sleep(1)
campo_nome = driver.find_element_by_id('id_firstName').send_keys(nome)
time.sleep(1)
campo_sobrenome = driver.find_element_by_id('id_lastName').send_keys(sobrenome)
time.sleep(1)
campo_cpf = driver.find_element_by_id('id_customerIdentification').send_keys(cpf)
time.sleep(1)
select = Select(driver.find_element_by_name('accountType'))
select.select_by_index(1)
time.sleep(1)
campo_agencia = driver.find_element_by_id('id_branchCode').send_keys(agencia)
time.sleep(1)
campo_conta = driver.find_element_by_id('id_accountNumber').send_keys(conta)
time.sleep(1)
campo_dv = driver.find_element_by_id('id_accountNumberCheckDigits')
campo_dv.send_keys(dv)
time.sleep(1)
driver.find_element_by_css_selector("div.submitBtnContainer").click()
time.sleep(1)
url = driver.current_url
while(url != "https://www.netflix.com/simpleSetup/orderfinal"):
		dv = dv + 1
		time.sleep(1)
		campo_dv.clear()
		time.sleep(1)
		campo_dv.send_keys(dv)
		time.sleep(1)
		driver.find_element_by_css_selector("div.submitBtnContainer").click()
		time.sleep(1)
		url = driver.current_url
print(email)
print(senha)
