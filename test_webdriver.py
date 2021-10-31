# bibliotecas
import pytest
import pytest_bdd
import behave
from selenium import webdriver

# definições / definitions
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


class Test_Webdriver():
    # Método de Inicialização do Teste
    def setup_method(self, method):
        # criar um objeto chamado "driver" e instancia-lo como Selenium para o navegador Chrome,
        # indicando onde está o seu chrome driver
        self.driver = webdriver.Chrome('drivers/chrome/94/chromedriver.exe')
        # definimos uma espera de até 3 segundos para qualquer elemento no teste
        self.driver.implicitly_wait(3)
        # maximizar a janela do browser
        self.driver.maximize_window()
        # declaramos uma atributo da classe chamado vars e ele é uma lista
        # self.vars = {}

    # Método de Finalização do Teste
    def teardown_method (self, method):
        # encerrar o objeto do Selenium WebDriver
        self.driver.quit()

    # Método de Teste - Consultar um Curso
    def test_consultar_curso(self):
        # o Selenium acessa o endereço do stie alvo
        self.driver.get('https://iterasys.com.br')

        # Página 1 - Home
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        # Como seria dar um tab a partir da caixa de texto
        # self.driver.find_element(By.ID, 'searchtext').send_keys(keys.TAB)
        # Clicar na lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()

        # Página 2
        # Clicar no botão Matricule-se
        self.driver.find_element(By.CSS_SELECTOR, '.comprar').click()

        # Página 3
        assert(self.driver.find_element(By.CSS_SELECTOR, '.item-title').text, 'Mantis')
        assert (self.driver.find_element(By.CSS_SELECTOR, '.new-price').text, 'R$ 59,99')







