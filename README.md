# Documentação do Projeto de Raspagem de Dados Climáticos

## Visão Geral

Este projeto tem como objetivo coletar dados climáticos de cidades específicas e armazenar essas informações em um banco de dados, além de exportar os dados para um arquivo Excel. O projeto utiliza o **Selenium** para raspagem de dados e a configuração é gerenciada através de arquivos **JSON** e **.env**.

## Estrutura do Projeto

### Arquivos de Configuração

- **`config.json`**: Contém as configurações do robô, como a URL do site a ser acessado e outras configurações relevantes.
- **`.env`**: Armazena variáveis de ambiente, como credenciais e diretórios para relatórios.

### Classes Principais

- **`RaspagemDadosClima`**: Classe principal que coordena a raspagem de dados, coleta informações climáticas e atualiza o banco de dados.
- **`RoboWebChrome`**: Gerencia o driver do navegador Chrome, incluindo configurações de download e inicialização.
- **`SeleniumHelper`**: Fornece métodos auxiliares para interagir com o Selenium, como verificar a presença de elementos e manipular páginas web.
- **`CidadesDAO` e `RoboStatusDAO`**: Data Access Objects (DAOs) para interagir com o banco de dados, gerenciar cidades e status do robô.

### Scripts de Execução

- **`main.py`**: Script principal para carregar as configurações, instanciar o robô e iniciar a raspagem de dados.

## Arquivos de Configuração

### `config.json`
```json
{
  "Comum": {
    "Ambiente": "Producao",
    "NomeRobo": "nome_robo",
    "DiretorioParaRelatorioFinal": "c:\\relatorios",
    "HoraEncerramento_24H": ""
  },
  "Email": {
    "To": "seu_email",
    "CC": "",
    "BCC": "",
    "Sistemas": "seu_email"
  },
  "Repositorio": {
    "Diretorio": "\\\\seu_repositorio"
  },
  "OCR": {
    "UtilizarAzureOCR": "1",
    "IronOCR_LicenceKey": "sua_licença",
    "Azure_Key": "sua_chave",
    "Azure_Endpoint": "seu_endpoint"
  },
  "Robos": [
    {
      "key": "robo_raspagem_dados_clima",
      "value": "SeleniumPython.Robos.RaspagemDados.RoboRaspagemDadosClima"
    }
  ]
}
```

- **Comum**: Configurações gerais do robô, como ambiente e diretório de relatórios.
- **Email**: Configurações para envio de emails.
- **Repositorio**: Diretório do repositório.
- **OCR**: Configurações de OCR (caso necessário).
- **Robos**: Mapeia o nome do robô para a classe correspondente.

### `.env`

```ini
COMUM_AMBIENTE=P
COMUM_NOME_ROBO=MeuRobo
COMUM_DIRETORIO_PARA_RELATORIO_FINAL=/caminho/para/relatorio
COMUM_HORA_ENCERRAMENTO_24H=18:00
EMAIL_TO=example@example.com
EMAIL_CC=cc@example.com
EMAIL_BCC=bcc@example.com
EMAIL_SISTEMAS=sistemas@example.com
REPOSITORIO_DIRETORIO=/caminho/para/repositorio
OCR_IRONOCR_KEY=your_ironocr_key
OCR_UTILIZAR_AZURE_OCR=1
OCR_AZURE_KEY=your_azure_key
OCR_AZURE_ENDPOINT=https://your_azure_endpoint
```

### Variáveis de Ambiente:

Utilizadas para configuração do ambiente de execução e credenciais.

### Classes Principais

- **RaspagemDadosClima**: Gerencia o processo de raspagem de dados. Inclui métodos para iniciar o robô, coletar dados climáticos e atualizar o banco de dados.
- **RoboWebChrome**: Gerencia o driver do navegador Chrome, configurando opções como o diretório de downloads.
- **SeleniumHelper**: Auxilia na interação com elementos da página usando o Selenium.

### Script de Execução

- **main.py**: O script principal que carrega as configurações, instancia o robô e inicia a raspagem.

### Execução do Projeto

## Configurar o Ambiente:
Certifique-se de que o Python e o Selenium estejam instalados.

Instale as dependências do projeto usando:
```bash
pip install -r requirements.txt
```

#### Configurar o Ambiente:

Certifique-se de que o **Python** e o **Selenium** estejam instalados.

Instale as dependências do projeto usando:
```bash
pip install -r requirements.txt
```

Configure o arquivo .env com as variáveis de ambiente apropriadas.

Executar o Robô:
Execute o script main.py para iniciar o robô:

```bash
python main.py
```

O robô irá ler as configurações do config.json, instanciar a classe apropriada e iniciar a raspagem de dados.

## Verificar Resultados:
Os dados climáticos serão atualizados no banco de dados e exportados para um arquivo Excel (dados_climaticos.xlsx).

### Nota
Certifique-se de que o ChromeDriver esteja corretamente instalado e configurado. O projeto utiliza o Selenium com o navegador Chrome para realizar a raspagem de dados.

