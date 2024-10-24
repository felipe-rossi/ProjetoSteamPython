from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from suporte.obterCodigoSteamViaOutlook import CodigoSteam
import time

class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.txtIniciarSessao = (By.XPATH, "//a[text()='Iniciar sessão']")
        self.inputNomeUsuario = (By.XPATH, "//div[text()='Iniciar sessão com o nome de usuário']//following-sibling::input[@type='text']")
        self.inputSenha = (By.XPATH, "//input[@type='password']")
        self.btnIniciarSessao = (By.XPATH, "//button[text()='Iniciar sessão']")
    
    def realizarLogin(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Iniciar sessão']")))
        self.driver.find_element(*self.txtIniciarSessao).click()

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Iniciar sessão com o nome de usuário']//following-sibling::input[@type='text']")))
        self.driver.find_element(*self.inputNomeUsuario).send_keys("feliperossisteam")

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
        self.driver.find_element(*self.inputSenha).send_keys("EL3+X]r+1r")
            
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Iniciar sessão']")))
        self.driver.find_element(*self.btnIniciarSessao).click()

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='A conta está protegida por autenticação via e-mail.']")))
        
        obterCodigoSteam = CodigoSteam
        codigo = obterCodigoSteam.obterCodigoViaEmail()
        
        if(codigo):
                
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text']")))
            self.inputPreencherCodigo = self.driver.find_elements(By.XPATH, "//input[@type='text']")
            print("Tamanho da lista: ", len(self.inputPreencherCodigo))

            self.inputPreencherCodigo[0].send_keys(codigo[0])
            time.sleep(1)
            self.inputPreencherCodigo[1].send_keys(codigo[1])
            time.sleep(1)
            self.inputPreencherCodigo[2].send_keys(codigo[2])
            time.sleep(1)
            self.inputPreencherCodigo[3].send_keys(codigo[3])
            time.sleep(1)
            self.inputPreencherCodigo[4].send_keys(codigo[4])
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "account_pulldown")))