from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
navegador = webdriver.Chrome(ChromeDriverManager().install())

def rpa_env_texto(xpath,text):
    """
    Envia um texto para o local especificado.

    :param xpath: string
    :param text: string, float, int, double
    """
    while True:
        try:
            navegador.find_element(By.XPATH,xpath).send_keys(text)
            break
        except:
            time.sleep(0.0001)
def rpa_click(xpath):
    """
    Clica no local especificado.

    :param xpath: string
    """

    while True:
        try:
            navegador.find_element(By.XPATH,xpath).click()
            break
        except:
            time.sleep(0.0001)  
def rpa_sel_texto(xpath):
    """
    Seleciona e copia o texto do local especificado.

    :param xpath: string

    :return string variavel
    """

    while True:
        try:
            navegador.find_element(By.XPATH, xpath).click()
            break
        except:
            time.sleep(0.0001)        
    navegador.find_element(By.XPATH,xpath).send_keys(Keys.CONTROL+"A")
    navegador.find_element(By.XPATH,xpath).send_keys(Keys.CONTROL+"C")
    variavel = pyperclip.paste()
    return(variavel)            
def rpa_texto_xpath(xpath):
    """
    Copia texto do local especificado.

    :param xpath: string

    :return string variavel
    """

    while True:
        try:
            variavel = navegador.find_element(By.XPATH,xpath).text
            break
        except:
            time.sleep(0.0001)
    return(variavel)
def rpa_site(link):
    """
    Abre o navegador no link enviado.

    :param link: string
    """
    navegador.get(link)
def rpa_clique_direito(xpath):
    action = ActionChains(navegador)
    source = navegador.find_element(By.XPATH,xpath);
    while True:
        try:
            action.context_click(source).perform()
            break
        except:
            time.sleep(0.0001)    
def rpa_click_duplo(xpath):
    action = ActionChains(navegador)
    source = navegador.find_element(By.XPATH, xpath);
    while True:
        try:
            action.double_click(source).perform()
            break
        except:
            time.sleep(0.0001)  
def rpa_em_cima(Nome_do_Texto):
    action = ActionChains(navegador)
    source = navegador.find_element(By.LINK_TEXT,Nome_do_Texto);
    while True:
        try:
            action.move_to_element(source).perform()
            break
        except:
            time.sleep(0.0001) 
def rpa_aba(indice):
    while True:
        try:
            variavel = navegador.window_handles[indice]
            break
        except:
            time.sleep(0.0001)
    return(variavel)
def rpa_tentar_clicar(xpath_1):
    while True:
        try:
            navegador.find_element(By.XPATH, xpath_1).click()
            clicou = True
            break
        except:
            clicou = False
            break
    return(clicou)
def rpa_maximizar_janela():
    while True:
        try:
            navegador.maximize_window()
            break
        except:
           time.sleep(000.1)
def rpa_enter(xpath):
    while True:
        try:
            navegador.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)
            break
        except:
            time.sleep(0.0001)
def rpa_achar_classe(classe):
    while True:
        try:
            navegador.find_element(By.CLASS_NAME, classe)
            time.sleep(000.1)
        except:
            print('Nao achou')
            break

def rpa_locate(xpath):
    element = navegador.find_element(By.XPATH,xpath)
    sytle = element.get_attribute("style")
    return(sytle)

def rpa_achar(xpath):
    while True:
        try:
            navegador.find_element(By.XPATH, xpath)
            print('Achou')
            break
        except:
            print('Não Achou')
            time.sleep(000.1)
def rpa_pegar_url():
    while True:
        try:
            variavel = navegador.current_url
            break
        except:
            time.sleep(000.1)
    return variavel
def rpa_trocar_aba(indice):
    while True:
        try:
            navegador.switch_to.window(indice)
            break
        except:
            time.sleep(0.001)