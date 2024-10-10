from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class Steam(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:/Users/Felipe_Rossi/Documents/ProjetoWYD/User Data")  # C:/Users/Felipe_Rossi/AppData/Local/Google/Chrome/User Data
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        

    def test_validarPrecosFacas(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/?l=portuguese")

        txtComunidade = driver.find_element(By.LINK_TEXT, "COMUNIDADE")
        EC.visibility_of_element_located(txtComunidade)
        ActionChains(driver).move_to_element(txtComunidade).perform()

        txtMercado = driver.find_elements(By.XPATH, "//a[contains(text(),'Mercado')]")
        EC.visibility_of_element_located(txtMercado[1])
        txtMercado[1].click()

        driver.execute_script("arguments[0].scrollIntoView();", element)
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()