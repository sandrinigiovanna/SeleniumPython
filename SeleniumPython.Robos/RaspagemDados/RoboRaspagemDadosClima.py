from datetime import datetime, time
import os
import pandas as pd
from selenium.webdriver.common.by import By
from DAO.RaspagemDados.RaspagemDados import CidadesDAO
from DAO.RoboStatusDAO import RoboStatusDAO
from Helpers.SeleniumHelper import SeleniumHelper
from RoboWeb.RoboWebChrome import RoboWebChrome

class RaspagemDadosClima:
    def __init__(self, url, download_directory):
        self.robo = RoboWebChrome(download_directory)
        self.url = url
        self.selenium_helper = SeleniumHelper()  # Inicializa o SeleniumHelper

    def iniciar(self):
        try:
            RoboStatusDAO.robo_iniciou()
            self.robo.iniciar_driver()
            self.executar_rotina()
        finally:
            RoboStatusDAO.robo_finalizou()
            self.robo.finalizar_driver()

    def executar_rotina(self):
        self.robo.driver.get(self.url)

        cidades = CidadesDAO.listar_cidades()
        dados = []  # Lista para armazenar os dados coletados

        for cidade in cidades:
            try:
                print(f"Coletando dados para a cidade: {cidade['cidade']}")

                pesquisaCidade = self.selenium_helper.existe_elemento(
                    self.robo.driver, (By.ID, 'LocationSearch_input')
                )
                if pesquisaCidade:
                    pesquisaCidade.clear()  # Limpa o campo de pesquisa
                    pesquisaCidade.send_keys(cidade['cidade'])  # Envia o nome da cidade para o campo
                    time.sleep(5)

                    temperatura_elemento = self.selenium_helper.existe_elemento(
                        self.robo.driver, (By.CSS_SELECTOR, ".CurrentConditions--tempValue--3a50n")
                    )
                    temperatura = temperatura_elemento.text
                    print(f"Temperatura atual em {cidade['cidade']}: {temperatura}")

                    # Adiciona os dados à lista
                    dados.append({
                        'cidade': cidade['cidade'],
                        'temperatura': temperatura,
                        'status_data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })

                    # Atualiza a temperatura no banco de dados
                    CidadesDAO.atualizar_temperatura(cidade['cidade'], temperatura)

            except Exception as e:
                print(f"Erro ao coletar dados para {cidade['cidade']}: {e}")

        # Exporta os dados para um arquivo Excel
        if dados:
            df = pd.DataFrame(dados)
            df.to_excel('dados_climaticos.xlsx', index=False)

if __name__ == "__main__":
    url = "https://weather.com"  # Defina a URL desejada
    download_directory = os.path.join(os.getcwd(), 'downloads')  # Diretório de downloads
    raspagem = RaspagemDadosClima(url, download_directory)
    raspagem.iniciar()
