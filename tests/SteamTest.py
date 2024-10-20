from selenium import webdriver
import unittest, time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from pages.lojaPage import LojaPage
from pages.mercadoComunidadePage import MercadoDaComunidadePage


class SteamTest(unittest.TestCase):
    
    
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:/Users/felip/AppData/Local/Google/Chrome/User Data") # C:/Users/felip/AppData/Local/Google/Chrome/User Data -  C:/ProgramData/Jenkins/.jenkins/workspace/SteamProjectKnives/User Data
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')  # Reduz o uso de memória compartilhada
        options.add_argument('--no-sandbox')  # Usado em alguns ambientes para evitar o sandbox
        options.add_argument('--disable-extensions')  # Desativa extensões
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors') 
        options.add_argument('--allow-insecure-localhost')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  
        self.driver.maximize_window()
        self.driver.get("https://store.steampowered.com/?l=portuguese")
        

    def test_validarPrecosFacas(self):
        loja_page = LojaPage(self.driver)
        loja_page.VerificarLogin()
        loja_page.acessarMercadoDaComunidade()
        
        mercado_page = MercadoDaComunidadePage(self.driver)
        mercado_page.verificarAvisoSolicitaoesDemais()
        mercado_page.filtrarPesquisaPorfacas("tag_CSGO_Type_Knife")
        mercado_page.filtarPeloMenorPreco()
        mercado_page.validarPrecoDaSkin()
    
    def test_validarPrecosLuvas(self):
        loja_page = LojaPage(self.driver)
        loja_page.VerificarLogin()
        loja_page.acessarMercadoDaComunidade()
        
        mercado_page = MercadoDaComunidadePage(self.driver)
        mercado_page.verificarAvisoSolicitaoesDemais()
        mercado_page.filtrarPesquisaPorfacas("tag_Type_Hands")
        mercado_page.filtarPeloMenorPreco()
        mercado_page.validarPrecoDaSkin()

    def tearDown(self):
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()