from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from suporte.TratamentoPreco import tratarPrecoSkinReal
from suporte.TratamentoPreco import tratarPrecoSkinDollar
from suporte.enviarEmailCompraSucesso import enviarEmailCompra
import time, unittest
from datetime import datetime


class MercadoDaComunidadePage(unittest.TestCase):
    
    def __init__(self, driver):
        self.driver = driver
        self.textVoceRealizouSolicitaos = (By.XPATH, "//h3[contains(text(),'Você realizou solicitações demais recentemente')]")
        self.botaoCounterStrike2 = (By.XPATH, "//div[@id='browseItems']//following-sibling::span[contains(text(),'Counter-Strike 2')][1]")
        self.btnExibirOpcoesAvancadas = (By.CLASS_NAME, "market_search_advanced_button")
        self.selectTipo = (By.NAME, "category_730_Type[]")
        self.btnBuscar = (By.XPATH, "//div[@class='market_advancedsearch_bottombuttons']//following-sibling::span[contains(text(),'Buscar')]")
        self.btnOrdenarProPreco = (By.XPATH, "//div[@data-sorttype='price'][1]")
        self.primeiraSkinNome = (By.ID, "result_0_name")
        self.primeiroResultadoSkin = (By.XPATH, "//span[@class='normal_price']")
        self.namePrimeiraSkin = (By.ID, "result_0_name")
        self.botaoComprarAgora = (By.XPATH, "//span[contains(text(),'Comprar agora')]")
        self.checkboxAceitoTermos = (By.ID, "market_buynow_dialog_accept_ssa")
        self.btnComprar = (By.XPATH, "//a[@id='market_buynow_dialog_purchase']")
        self.btnFechar = (By.ID, "market_buynow_dialog_close")
    
    def verificarAvisoSolicitaoesDemais(self):
        txtVoceRealizou = self.driver.find_elements(*self.textVoceRealizouSolicitaos)
        quantidade_texto = len(txtVoceRealizou)

        if(quantidade_texto > 0):
            self.driver.save_screenshot("Realizou_Solicitacoes_demais.png")
            time.sleep(1800)     
    
    
    def filtrarPesquisaPorfacas(self, tipoSkin):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Anunciar um item')]")))
        
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='browseItems']//following-sibling::span[contains(text(),'Counter-Strike 2')][1]")))
        btnCounterStrike2 = self.driver.find_element(*self.botaoCounterStrike2)
        self.driver.execute_script("arguments[0].scrollIntoView();", btnCounterStrike2)
        btnCounterStrike2.click()

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "market_search_advanced_button")))
        self.driver.find_element(*self.btnExibirOpcoesAvancadas).click()
    
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.NAME, "category_730_Type[]")))
        select = Select(self.driver.find_element(*self.selectTipo))
        select.select_by_value(tipoSkin) 

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='market_advancedsearch_bottombuttons']//following-sibling::span[contains(text(),'Buscar')]")))
        self.driver.find_element(*self.btnBuscar).click()

    def filtarPeloMenorPreco(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-sorttype='price'][1]")))
        self.driver.find_element(*self.btnOrdenarProPreco).click()
    
    def validarPrecoDaSkin(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "resultlink_0")))
        nome_primeira_skin = self.driver.find_element(*self.primeiraSkinNome)

        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(nome_primeira_skin))
       
        primeiroResultado = self.driver.find_elements(*self.primeiroResultadoSkin)
    
        precoSkin = primeiroResultado[0].text

        if("R$" in precoSkin):
            precoSkinTratada = tratarPrecoSkinReal(precoSkin)
        else:
            precoSkinTratada = tratarPrecoSkinDollar(precoSkin)

        agora = datetime.now()
        self.driver.save_screenshot('screenshots/ultima_validacao_skin.png')
        print("Screenshot foi capturada na data e hora:", agora)
        print("Preço mais barato da faca: ", precoSkin)

        if(precoSkinTratada <=  10000 or precoSkinTratada <= 1782):
            self.realizarCompra()
    
    def realizarCompra(self):
        print("Skin com valor menor que 100 reais")
        self.driver.save_screenshot("screenshots/skin_preco_baixo.png")
        
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "result_0_name")))
        self.driver.find_element(*self.namePrimeiraSkin).click()

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "largeiteminfo_item_actions")))

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Comprar agora')]")))
        btnComprarAgora = self.driver.find_element(*self.botaoComprarAgora)
        self.driver.execute_script("arguments[0].scrollIntoView();", btnComprarAgora)
        btnComprarAgora.click()

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, "market_buynow_dialog_accept_ssa")))
        self.driver.find_element(*self.checkboxAceitoTermos).click()

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='market_buynow_dialog_purchase']")))
        self.driver.find_element(*self.btnComprar).click()
            
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Parabéns pela compra!')]")))
              
        self.driver.save_screenshot('screenshots/compra_realizada_com_sucesso.png')    
        
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, "market_buynow_dialog_close")))
        self.driver.find_element(*self.btnFechar).click()
        
        enviarEmailCompra()