#importar bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#navegar na web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

#definir contatos, grupos e mensagens
contacts = ['group', 'people']
message = "Hi, how are you?"

# buscar contatos/grupos
def search_contact(contact):
    field_search = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    field_search.click()
    field_search.send_keys(contact)
    field_search.send_keys(Keys.ENTER)

def submit_message(message):
    field_message = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    field_message[1].click()
    time.sleep(3)
    field_message[1].send_keys(message)
    field_message[1].send_keys(Keys.ENTER)

# enviar mensagens
for contact in contacts: 
    search_contact(contact)
    submit_message(message)
    
# campo de pesquisa 'copyable-text selectable-text'
# campo de mensagem privada 'copyable-text selectable-text'

