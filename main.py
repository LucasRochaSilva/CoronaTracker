from selenium import webdriver
from time import sleep

url = "https://www.coronatracker.com/pt-br/"


driver = webdriver.Chrome()
driver.get(url)

sleep(3)
casos = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span')
curados = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span')
mortes = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span')
casosbr = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[2]/div[1]/table/tbody/tr[3]/td[2]')
teste = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[2]/div[1]/div[1]/div[1]/span')

casestext_casos = casos.text
casestext_curados = curados.text
casestext_mortes = mortes.text
casestext_casosbr = casosbr.text
teste_text = teste.text


print(f'Casos Confirmados: {casestext_casos}')
print(f'Curados: {casestext_curados}')
print(f'Mortes: {casestext_mortes}')
