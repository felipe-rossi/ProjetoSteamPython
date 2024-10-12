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
from enviarEmailCompraSucesso import enviarEmailCompra



class Steam(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:/ProgramData/Jenkins/.jenkins/workspace/SteamProjectKnives/User Data") # C:/Users/felip/AppData/Local/Google/Chrome/User Data / C:/Users/felip/Documents/ProjetoSteamPython/User Data
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
        selectFaca.select_by_value("tag_CSGO_Type_Knife") # tag_CSGO_Type_Knife

        
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='market_advancedsearch_bottombuttons']//following-sibling::span[contains(text(),'Buscar')]")))
        btnBuscar = driver.find_element(By.XPATH, "//div[@class='market_advancedsearch_bottombuttons']//following-sibling::span[contains(text(),'Buscar')]")
        btnBuscar.click()
        
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-sorttype='price'][1]")))
        btnOrdenarProPreco = driver.find_element(By.XPATH, "//div[@data-sorttype='price'][1]")
        btnOrdenarProPreco.click()
        

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "resultlink_0")))
        nome_primeira_skin = driver.find_element(By.ID, "result_0_name")

        WebDriverWait(driver, 30).until(EC.invisibility_of_element_located(nome_primeira_skin))
       
        primeiroResultado = driver.find_elements(By.XPATH, "//span[@class='normal_price']")
    
        precoSkin = primeiroResultado[0].text

        precoSkinTratada = tratarPrecoSkin(precoSkin)

        print("Preço mais barato da faca: ", precoSkin)

        if(precoSkinTratada <=  1782):
            print("Faca com valor menor que 100 reais")
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "result_0_name")))
            nome_primeira_skin = driver.find_element(By.ID, "result_0_name")
            nome_primeira_skin.click()

            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "largeiteminfo_item_actions")))

            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Comprar agora')]")))
            btnComprarAgora = driver.find_element(By.XPATH, "//span[contains(text(),'Comprar agora')]")
            driver.execute_script("arguments[0].scrollIntoView();", btnComprarAgora)
            btnComprarAgora.click()

            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "market_buynow_dialog_accept_ssa")))
            checkboxAceitoTermos = driver.find_element(By.ID, "market_buynow_dialog_accept_ssa")
            checkboxAceitoTermos.click()

            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='market_buynow_dialog_purchase']")))
            btnComprar = driver.find_element(By.XPATH, "//a[@id='market_buynow_dialog_purchase']")
            btnComprar.click()
            
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Parabéns pela compra!')]")))
            txtPrabensPelaSuaCompra = driver.find_element(By.XPATH, "//div[contains(text(),'Parabéns pela compra!')]")

            self.assertEqual(txtPrabensPelaSuaCompra.text, "Parabéns pela compra! Você pode ver o novo item no seu inventário.")            
            enviarEmailCompra()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()