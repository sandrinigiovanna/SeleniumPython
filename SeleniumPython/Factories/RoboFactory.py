import json
from pathlib import Path

class RoboFactory:
    def __init__(self, config_file: str):
        self.config = self.load_config(config_file)
        self.robos = self.config.get("Robos", [])

    def load_config(self, config_file: str) -> dict:
        with open(config_file, 'r') as file:
            return json.load(file)

    def criar_robo(self, nome_robo: str, args: Optional[List[str]] = None):
        robo = None
        try:
            robo_type = next((item for item in self.robos if item['key'].upper() == nome_robo.upper()), None)
            if not robo_type:
                raise ValueError(f"Rob� n�o encontrado para o nome: {nome_robo}")
            
            # Aqui, voc� deve ter uma maneira de mapear `robo_type['value']` para o tipo real de rob�
            # Por exemplo, se `robo_type['value']` � uma string com o nome do m�dulo e classe, voc� pode fazer:
            module_name, class_name = robo_type['value'].rsplit('.', 1)
            module = __import__(module_name, fromlist=[class_name])
            robo_class = getattr(module, class_name)
            robo = robo_class(*args)  # Cria uma inst�ncia do rob�
        except Exception as e:
            raise Exception(f"Erro ao criar o rob�. Nome indicado: {nome_robo}. Erro: {e}")
        
        return robo
