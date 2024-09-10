import requests
from bs4 import BeautifulSoup
import psutil

class WebClientHelper:
    
    @staticmethod
    def enviar_requisicao_json(url, json_data, cookies):
        try:
            headers = {
                'Content-Type': 'application/json',
                'Cookie': cookies
            }
            response = requests.post(url, json=json_data, headers=headers)
            response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP de erro
            return response.text
        except requests.RequestException as e:
            print(f"Erro ao enviar requisição: {e}")
            return ""

    @staticmethod
    def obter_html_da_pagina(url, cookies, parametros=None):
        try:
            headers = {
                'Cookie': cookies
            }
            response = requests.get(url, headers=headers, params=parametros)
            response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP de erro
            
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        except requests.RequestException as e:
            print(f"Erro ao obter HTML: {e}")
            return None

    @staticmethod
    def fechar_processo_maquina(nome_processo):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == nome_processo:
                try:
                    proc.terminate()  # Ou proc.kill() para forçar o encerramento
                except psutil.AccessDenied:
                    print(f"Permissão negada para encerrar o processo {nome_processo}")
                except psutil.NoSuchProcess:
                    print(f"O processo {nome_processo} não existe")
