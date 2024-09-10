import json
import importlib
from dotenv import load_dotenv

# Carregar vari�veis de ambiente do .env
load_dotenv()

# Carregar configura��es do arquivo config.json
def carregar_configuracoes(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        return json.load(f)

def obter_robos(config):
    return {robo['key']: robo['value'] for robo in config.get('Robos', [])}

def main():
    # Carregar configura��es
    config = carregar_configuracoes('config.json')
    
    # Obter informa��es do rob� a partir da configura��o
    robos = obter_robos(config)
    nome_robo = config['Comum']['NomeRobo']
    
    if nome_robo not in robos:
        raise ValueError(f"Rob� com o nome '{nome_robo}' n�o encontrado na configura��o.")
    
    # Importar e instanciar o rob� dinamicamente
    caminho_robo = robos[nome_robo]
    modulo_nome, classe_nome = caminho_robo.rsplit('.', 1)
    modulo = importlib.import_module(modulo_nome)
    classe = getattr(modulo, classe_nome)
    
    # Instanciar o rob� (os par�metros s�o passados diretamente na classe)
    url = "https://weather.com"  # Essa URL � definida diretamente na classe
    download_directory = os.path.join(os.getcwd(), 'downloads')  # Diret�rio de downloads tamb�m definido na classe
    robo = classe(url, download_directory)
    robo.iniciar()

if __name__ == "__main__":
    main()
