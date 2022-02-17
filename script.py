"""
Desenvolvido por George Fábio Fonseca
E-mail: georgefcfonseca@gmail.com
Data: 2022-02-16
Sempre: Faça, Fuce, Force
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import SessionNotCreatedException
import time

url = "https://tasy.hospitalsaojudas.com.br"

options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
prefs = {"credentials_enable_service": False,
     "profile.password_manager_enabled": False,
     "useAutomationExtension": False}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver_path = '.\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
driver.get(url)
time.sleep(20)
driver.find_element(By.ID, "loginUsername").send_keys("usuario_cadastrado")
time.sleep(3)
driver.find_element(By.ID, "loginPassword").send_keys("senha_usuario" + Keys.ENTER)
time.sleep(20)
actions = ActionChains(driver)
element1 = driver.find_element_by_xpath('//*[@id="datagrid"]/div[4]/div[3]/div/div[1]/div[1]/div/span')
actions.double_click(element1).perform()
time.sleep(20)

"""
#  Dai-me um desafio, que eu darei o meu melhor !!!
"""
