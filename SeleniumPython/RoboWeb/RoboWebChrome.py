from RoboWeb.RoboWeb import RoboWeb
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import os
import time

# Classe para gerenciar o driver do Chrome e funcionalidades extras
class ChromeDriverEx(webdriver.Chrome):
    def __init__(self, download_directory, timeout=300):
        chrome_options = Options()

        # Configurações de perfil do Chrome
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_directory,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True
        })
        chrome_options.add_argument("--allow-running-insecure-content")

        # Instala o ChromeDriver automaticamente
        chromedriver_autoinstaller.install()

        # Inicia o ChromeDriver com as opções e timeout
        super().__init__(options=chrome_options)
        self.command_timeout = timeout
        self.process_id = self._get_process_id()

    # Método para obter o ID do processo do ChromeDriver (exemplo simplificado)
    def _get_process_id(self):
        # No Python, você pode usar bibliotecas como psutil para obter o PID
        # Aqui vou retornar um placeholder, ajuste conforme a necessidade
        return os.getpid()

# Classe abstrata para robôs que usam o Chrome
class RoboWebChrome(RoboWeb):
    def __init__(self, download_directory):
        self.download_directory = download_directory
        self.driver = None
        self.wait = None
        self.js_executor = None
        self.element = None

    def iniciar_driver(self):
        # Cria o diretório de downloads, se não existir
        if not os.path.exists(self.download_directory):
            os.makedirs(self.download_directory)

        # Inicia o ChromeDriver personalizado
        self.driver = ChromeDriverEx(self.download_directory)
        self.wait = WebDriverWait(self.driver, 300)  # Timeout de 5 minutos
        self.js_executor = self.driver.execute_script  # Executor de JavaScript

    def close_driver(self):
        if self.driver:
            self.driver.quit()

# Exemplo de uso
if __name__ == "__main__":
    robo = RoboWebChrome(download_directory=os.path.join(os.getcwd(), 'downloads'))
    robo.iniciar_driver()

    # Exemplo de navegação para um site
    robo.driver.get("https://www.example.com")
    
    # Após usar o robô, feche o driver
    time.sleep(5)  # Espera um pouco para ver a página
    robo.close_driver()
