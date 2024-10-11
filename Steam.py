from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from TratamentoPreco import tratarPrecoSkin
import smtplib


class Steam(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:/Users/felip/AppData/Local/Google/Chrome/User Data") # C:/Users/felip/AppData/Local/Google/Chrome/User Data
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')  # Reduz o uso de memória compartilhada
        options.add_argument('--no-sandbox')  # Usado em alguns ambientes para evitar o sandbox
        options.add_argument('--disable-extensions')  # Desativa extensões
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors') 
        options.add_argument('--allow-insecure-localhost')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  

        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        

    def test_validarPrecosFacas(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/?l=portuguese")


        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "COMUNIDADE")))
        txtComunidade = driver.find_element(By.LINK_TEXT, "COMUNIDADE")
        ActionChains(driver).move_to_element(txtComunidade).perform()

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='global_header']//following::a[contains(text(),'Mercado')]")))
        txtMercado = driver.find_element(By.XPATH, "//div[@id='global_header']//following::a[contains(text(),'Mercado')]")
        txtMercado.click()

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Anunciar um item')]")))
        
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='browseItems']//following-sibling::span[contains(text(),'Counter-Strike 2')][1]")))
        btnCounterStrike2 = driver.find_element(By.XPATH, "//div[@id='browseItems']//following-sibling::span[contains(text(),'Counter-Strike 2')][1]")
        driver.execute_script("arguments[0].scrollIntoView();", btnCounterStrike2)
        btnCounterStrike2.click()

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "market_search_advanced_button")))
        btnExibirOpcoesAvancadas = driver.find_element(By.CLASS_NAME, "market_search_advanced_button")
        btnExibirOpcoesAvancadas.click()


        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "category_730_Type[]")))
        selectFaca = Select(driver.find_element(By.NAME, "category_730_Type[]"))
        selectFaca.select_by_value("tag_CSGO_Tool_WeaponCase_KeyTag") # tag_CSGO_Type_Knife

        
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='market_advancedsearch_bottombuttons']//following-sibling::span[contains(text(),'Buscar')]")))
        btnBuscar = driver.find_element(By.XPATH, "//div[@class='market_advancedsearch_bottombuttons']//following-sibling::span[contains(text(),'Buscar')]")
        btnBuscar.click()
        
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-sorttype='price'][1]")))
        btnOrdenarProPreco = driver.find_element(By.XPATH, "//div[@data-sorttype='price'][1]")
        btnOrdenarProPreco.click()
        

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "resultlink_0")))
        listaNomeSkinsSemFiltro = driver.find_elements(By.ID, "result_0_name")
        nome_primeira_skin = listaNomeSkinsSemFiltro[0]
        WebDriverWait(driver, 30).until(EC.invisibility_of_element_located(nome_primeira_skin))
       
        primeiroResultado = driver.find_elements(By.XPATH, "//span[@class='normal_price']")
    
        precoSkin = primeiroResultado[0].text

        precoSkinTratada = tratarPrecoSkin(precoSkin)

        print("Preço da Skin mais barata é de:" + precoSkin)
        print("Preço da Skin mais barata é de tratada:", precoSkinTratada)

        print(type(precoSkinTratada))

        if(precoSkinTratada <=  10000):
            print("Skin com valor menor que 100 reais")
            servidor_email = smtplib.SMTP("smtp.gmail.com", 587)
            servidor_email.starttls()
            servidor_email.login('felipaovs12@gmail.com','dgmj hyot mhbf ybzj')

            remetente = 'felipaovs12@gmail.com'
            destinatarios = ['caioansanelli1@gmail.com','rfgdfghgf@gmail.com']
            conteudo = "Email teste para compra de skins cs2"

            servidor_email.sendmail(remetente, destinatarios, conteudo)

            servidor_email.quit()


    def tearDown(self):
        #self.driver.close()
        print("Terminou")

if __name__ == "__main__":
    unittest.main()