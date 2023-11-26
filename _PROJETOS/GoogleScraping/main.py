#coding=UTF-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.proxy import Proxy, ProxyType
import pandas as pd
import re


# API_KEY = "b065742bc1da263a2512340630993a08"
# APIURL = F"http://api.scraperapi.com?{api_key}=APIKEY&url="

PROXY = '91.107.247.138:4000'

def main():
  schoolar_resultado = {
    'titulo': [],
    'ano': [],
    'revista': [],
    'autor': [],
    'citação_numero':[]
  }
  
  pesquisa = '"parenthetical man"'
  # pesquisa = str(input("Pesquisa: "))
  # proxy = {
  #   'proxy': {
  #     'http': f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001',
  #     'https': f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001',
  #     'no_proxy': 'localhost,127.0.0.1'
  #   }
  # }
  
  options = webdriver.ChromeOptions()
  options.add_argument(f"--proxy-server={PROXY}")
  browser = webdriver.Chrome(options = options)
  wait = WebDriverWait(browser, 20)
  
  try:
    browser.get("https://scholar.google.com/")
    search_bar = wait.until(ec.presence_of_element_located((By.NAME, "q")))
  except:
    browser.close()
  # search_bar = browser.find_element(By.NAME, "q")
  search_bar.clear()
  search_bar.send_keys(pesquisa)
  search_bar.send_keys(Keys.ENTER)
  regex_ano = r"[0-9]{4}"
  regex_autor = "[A-ZÀ-Ö]+\,\s[a-zA-Zà-öù-ÿ\s]+"
  print()
  print(browser.find_element(By.XPATH, '//*[@id="gs_ab_md"]/div').text)
  print()
  
  
  while True:
    resultado = browser.find_elements(By.CSS_SELECTOR, ".gs_r.gs_or.gs_scl")
    for i in resultado:
      titulo =  i.find_element(By.CLASS_NAME, "gs_rt").text
      citação_numero = re.findall(r"Citado por [0-9]+", i.text)
      
      i.find_element(By.CSS_SELECTOR, ".gs_or_cit.gs_or_btn.gs_nph").click()
      citar_janela = wait.until(ec.presence_of_element_located((By.CLASS_NAME, "gs_citr")))
      revista = citar_janela.find_element(By.XPATH, '//*[@id="gs_citt"]/table/tbody/tr[2]/td/div/b').text
      
      autor = re.findall(regex_autor, citar_janela.text)
      ano = re.findall(regex_ano, citar_janela.text)
      
      schoolar_resultado['titulo'].append(titulo)
      schoolar_resultado['ano'].append(ano)
      schoolar_resultado['revista'].append(revista)
      schoolar_resultado['autor'].append(autor)
      schoolar_resultado['citação_numero'].append(citação_numero)
      # browser.find_element(By.ID, 'gs_cit-x').click()
      # wait.until_not(ec.presence_of_element_located((By.CLASS_NAME, 'gs_vis')))
      print(titulo, ano, revista, autor, citação_numero)

    browser.quit()
    break
      
      # titulo =  resultado.find_element(By.CLASS_NAME, "gs_rt").text
      # # titulo = titulo.find_elements(By.TAG_NAME, "a") # titulo
      # citação_numero = resultado.find_elements(By.TAG_NAME, "a")
      # # print(citação_numero)
      # for a in citação_numero:
      #   if re.search(r"^Citado por.[0-9]+$", a.text):
      #     citação_numero = a.text  
      # citação_numero = re.findall(r"^Citado por.[0-9]+$", resultado.find_element(By.CLASS_NAME, "gs_ri").text)  # numero de citações
      
      # print( titulo, citação_numero)
      
      # resultado.find_element(By.CLASS_NAME, "gs_or_cit gs_or_btn gs_nph").click()
      
      # citar_janela = wait.until(ec.presence_of_element_located((By.XPATH, f'//*[@id="gs_citt"]/table/tbody/tr[2]/td/div')))
      
      # revista = citar_janela.find_element(By.TAG_NAME, "b").text
      
      # autor = re.findall(regex_autor, citar_janela.text)
      
      # ano = re.findall(regex_ano, citar_janela.text)
      
      # schoolar_resultado['titulo'].append(titulo)
      # schoolar_resultado['ano'].append(ano)
      # schoolar_resultado['revista'].append(revista)
      # schoolar_resultado['autor'].append(autor)
      # schoolar_resultado['citação_numero'].append(citação_numero)
      # browser.back()
      # # browser.find_element(By.XPATH, '//*[@id="gs_cit-x"]').click()
      # # wait.until_not(ec.presence_of_element_located((By.CLASS_NAME, 'gs_vis')))
      # print('registrado...')
    # browser.find_element(By.XPATH, '//*[@id="gs_nm"]/button[2]').click()
  
  print(pd.DataFrame(schoolar_resultado))

if __name__ == "__main__":
  main()
  
  # teste = "[HTML] Bernard Lonergan and Alberto Guerreiro Ramos: dialogues between the existential subject and the parenthetical man"
  # print(re.findall(r"^[\[A-Z\]]+", teste))
  # teste = "RAMOS, Alberto Guerreiro. 1.6 Models of Man and Administrative Theory. The Management of Organizations and Individuals, v. 1, p. 46, 1975."
  # teste2 = "AZEVÊEDO, Ariston; ALBERNAZ, Renata Ovenhausen. Alberto Guerreiro Ramos's anthropological approach to the social sciences: the parenthetical man. Administrative Theory & Praxis, v. 28, n. 4, p. 501-521, 2006."
  # print(re.findall(r"[0-9]{4}", teste))
  # print(re.findall(r"[A-ZÀ-Ö]+\,\s[a-zA-Zà-öù-ÿ\s]+", teste))
  # print(re.findall(r"\.\s[A-Za-z0-9\s\.\:\`\-]+\.", teste))