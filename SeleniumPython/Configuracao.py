import json
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Função para carregar configurações do arquivo JSON
def carregar_config_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        return json.load(file)

# Função para carregar variáveis de ambiente
def carregar_config_env():
    return {
        'ambiente': os.getenv('COMUM_AMBIENTE'),
        'nome_robo': os.getenv('COMUM_NOME_ROBO'),
        'diretorio_para_relatorio_final': os.getenv('COMUM_DIRETORIO_PARA_RELATORIO_FINAL'),
        'hora_encerramento': os.getenv('COMUM_HORA_ENCERRAMENTO_24H'),
        'email_to': os.getenv('EMAIL_TO'),
        'email_cc': os.getenv('EMAIL_CC'),
        'email_bcc': os.getenv('EMAIL_BCC'),
        'email_sistemas': os.getenv('EMAIL_SISTEMAS'),
        'repositorio_diretorio': os.getenv('REPOSITORIO_DIRETORIO'),
        'ocr_utilizar_azure_ocr': os.getenv('OCR_UTILIZAR_AZURE_OCR'),
        'ocr_azure_key': os.getenv('OCR_AZURE_KEY'),
        'ocr_azure_endpoint': os.getenv('OCR_AZURE_ENDPOINT'),
    }
