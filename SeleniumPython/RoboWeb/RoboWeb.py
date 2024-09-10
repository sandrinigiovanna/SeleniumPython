import os
import subprocess
from abc import ABC, abstractmethod
from DAO.RoboStatusDAO import RoboStatusDAO
from Robo import Robo
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver as IWebDriver
from selenium.webdriver.remote.webdriver import WebDriver as IWebDriverEx
from typing import Optional
from datetime import datetime

class RoboWeb(Robo):
    def __init__(self):
        self.tipo_robo = 'Web'
        self.driver: Optional[IWebDriverEx] = None
        self.element: Optional[webdriver.WebElement] = None
        self.wait: Optional[WebDriverWait] = None
        self.java_script_executor: Optional[webdriver.JavascriptExecutor] = None

    @abstractmethod
    def iniciar_driver(self):
        pass

    def iniciar_componentes(self):
        self.iniciar_driver()

    def finalizar_componentes(self):
        if self.driver:
            self.driver.quit()

        diretorio_para_downloads = Configuracao.Comum.DiretorioParaDownloads
        if os.path.exists(diretorio_para_downloads):
            os.rmdir(diretorio_para_downloads)

    def obter_processo_do_driver(self, driver: IWebDriverEx) -> Optional[subprocess.Popen]:
        ie_processes = [p for p in psutil.process_iter() if p.name() == "iexplore"]
        for process in ie_processes:
            if process.pid == driver.process_id:
                return process
        return None

    def gerar_parametros_com_driver(self):
        return {
            "Driver": self.driver,
            "JavaScriptExecutor": self.java_script_executor
        }

    def realizar_login(self, login):
        tipo_erro = login.acessar()
        return self.tratar_retorno(tipo_erro, login)

    def tratar_retorno(self, tipo_erro, login) -> bool:
        mensagem_erro = str(tipo_erro)
        email = Email()

        if tipo_erro in [MensagemErroLogin.SemErro, MensagemErroLogin.Autenticado]:
            return True

        if tipo_erro == MensagemErroLogin.ServicoNaoDisponivel:
            self.reiniciar_componente()
            tipo_erro = login.acessar()
            return self.tratar_retorno(tipo_erro, login)

        if tipo_erro == MensagemErroLogin.SenhaExpirada:
            tipo_erro = login.trocar_senha()
            return self.tratar_retorno(tipo_erro, login)

        RoboStatusDAO.indicar_erro_no_robo(self.nome_robo, mensagem_erro)
        assunto = f"ERRO: {self.nome_robo} {mensagem_erro} - {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
        email.enviar_email("", "", "", assunto, "")

        return False

    @abstractmethod
    def reiniciar_componente(self):
        pass
