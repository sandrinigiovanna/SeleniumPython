import json
import importlib
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Carregar configurações do arquivo config.json
def carregar_configuracoes(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        return json.load(f)

def obter_robos(config):
    return {robo['key']: robo['value'] for robo in config.get('Robos', [])}

def main():
    # Carregar configurações
    config = carregar_configuracoes('config.json')
    
    # Obter informações do robô a partir da configuração
    robos = obter_robos(config)
    nome_robo = config['Comum']['NomeRobo']
    
    if nome_robo not in robos:
        raise ValueError(f"Robô com o nome '{nome_robo}' não encontrado na configuração.")
    
    # Importar e instanciar o robô dinamicamente
    caminho_robo = robos[nome_robo]
    modulo_nome, classe_nome = caminho_robo.rsplit('.', 1)
    modulo = importlib.import_module(modulo_nome)
    classe = getattr(modulo, classe_nome)
    
    # Instanciar o robô (os parâmetros são passados diretamente na classe)
    url = "https://weather.com"  # Essa URL é definida diretamente na classe
    download_directory = os.path.join(os.getcwd(), 'downloads')  # Diretório de downloads também definido na classe
    robo = classe(url, download_directory)
    robo.iniciar()

if __name__ == "__main__":
    main()
