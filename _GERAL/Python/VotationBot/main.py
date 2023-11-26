from fileinput import close
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import ctypes
import time
import random as rd


def wait_and_click(id):
    while True:
        try:
            driver.find_element(By.ID, id).click()
            break
        except:
            time.sleep(3)


chrome = Service(ChromeDriverManager().install())

    
#driver = webdriver.Chrome(service=chrome)
for i in range(1, 9999):
    
    driver = webdriver.Firefox()
    driver.get("https://galeriapagebras.com.br/votacao/")
    print("abrindo site")
    wait_and_click("btnAcceptCookie")
    print("aceitando cookie")

    wait_and_click("6438")
    print("botão votar")

    WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.ID, "nome")))
    print("tela de dados apareceu")

    driver.find_element(By.ID, "nome").send_keys("jaskdjiojuwwia")
    driver.find_element(By.ID, "telDDD").send_keys(rd.randint(12,19))
    driver.find_element(By.ID, "telNumero").send_keys(rd.randint(100000000, 999999999))
    driver.execute_script("document.getElementsByTagName('button')[10].click()")
    print("dados preenchidos e enviados")

    result = "/html/body/div[1]/div[1]/section[3]/div/div/div/div[1]/div/div[1]/span"
    WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, result)))

    result = driver.find_element(By.ID, "telNumero").text
    if result == "Seu voto foi computado! Obrigado! ":
        with open("count.txt", "w") as f:
            f.write(str(i))
        print("registrado no txt")

    driver.close()


