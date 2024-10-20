from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.loginPage import LoginPage
from pages.mercadoComunidadePage import MercadoDaComunidadePage
from selenium.webdriver.common.action_chains import ActionChains


class LojaPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.btnFelipeRossiLogado = self.driver.find_elements(By.ID, "account_pulldown")
        self.txtComunidade = (By.LINK_TEXT, "COMUNIDADE")
        self.txtMercado = (By.XPATH, "//div[@id='global_header']//following::a[contains(text(),'Mercado')]")
        
        
    def VerificarLogin(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "logo_holder")))
        
        quantidade_btn_logado = len(self.btnFelipeRossiLogado)
        
        if(quantidade_btn_logado == 0):
            login_page = LoginPage(self.driver)
            login_page.realizarLogin()
        
    def acessarMercadoDaComunidade(self):        
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "COMUNIDADE")))
        comunidade = self.driver.find_element(*self.txtComunidade)
        ActionChains(self.driver).move_to_element(comunidade).perform()

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='global_header']//following::a[contains(text(),'Mercado')]")))
        self.driver.find_element(*self.txtMercado).click()