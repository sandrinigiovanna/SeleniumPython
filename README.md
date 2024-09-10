# Documenta��o do Projeto de Raspagem de Dados Clim�ticos

## Vis�o Geral

Este projeto tem como objetivo coletar dados clim�ticos de cidades espec�ficas e armazenar essas informa��es em um banco de dados, al�m de exportar os dados para um arquivo Excel. O projeto utiliza o **Selenium** para raspagem de dados e a configura��o � gerenciada atrav�s de arquivos **JSON** e **.env**.

## Estrutura do Projeto

### Arquivos de Configura��o

- **`config.json`**: Cont�m as configura��es do rob�, como a URL do site a ser acessado e outras configura��es relevantes.
- **`.env`**: Armazena vari�veis de ambiente, como credenciais e diret�rios para relat�rios.

### Classes Principais

- **`RaspagemDadosClima`**: Classe principal que coordena a raspagem de dados, coleta informa��es clim�ticas e atualiza o banco de dados.
- **`RoboWebChrome`**: Gerencia o driver do navegador Chrome, incluindo configura��es de download e inicializa��o.
- **`SeleniumHelper`**: Fornece m�todos auxiliares para interagir com o Selenium, como verificar a presen�a de elementos e manipular p�ginas web.
- **`CidadesDAO` e `RoboStatusDAO`**: Data Access Objects (DAOs) para interagir com o banco de dados, gerenciar cidades e status do rob�.

### Scripts de Execu��o

- **`main.py`**: Script principal para carregar as configura��es, instanciar o rob� e iniciar a raspagem de dados.

## Arquivos de Configura��o

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
    "IronOCR_LicenceKey": "sua_licen�a",
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

- **Comum**: Configura��es gerais do rob�, como ambiente e diret�rio de relat�rios.
- **Email**: Configura��es para envio de emails.
- **Repositorio**: Diret�rio do reposit�rio.
- **OCR**: Configura��es de OCR (caso necess�rio).
- **Robos**: Mapeia o nome do rob� para a classe correspondente.

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

### Vari�veis de Ambiente:

Utilizadas para configura��o do ambiente de execu��o e credenciais.

### Classes Principais

- **RaspagemDadosClima**: Gerencia o processo de raspagem de dados. Inclui m�todos para iniciar o rob�, coletar dados clim�ticos e atualizar o banco de dados.
- **RoboWebChrome**: Gerencia o driver do navegador Chrome, configurando op��es como o diret�rio de downloads.
- **SeleniumHelper**: Auxilia na intera��o com elementos da p�gina usando o Selenium.

### Script de Execu��o

- **main.py**: O script principal que carrega as configura��es, instancia o rob� e inicia a raspagem.

### Execu��o do Projeto

## Configurar o Ambiente:
Certifique-se de que o Python e o Selenium estejam instalados.

Instale as depend�ncias do projeto usando:
```bash
pip install -r requirements.txt
```

#### Configurar o Ambiente:

Certifique-se de que o **Python** e o **Selenium** estejam instalados.

Instale as depend�ncias do projeto usando:
```bash
pip install -r requirements.txt
```

Configure o arquivo .env com as vari�veis de ambiente apropriadas.

Executar o Rob�:
Execute o script main.py para iniciar o rob�:

```bash
python main.py
```

O rob� ir� ler as configura��es do config.json, instanciar a classe apropriada e iniciar a raspagem de dados.

## Verificar Resultados:
Os dados clim�ticos ser�o atualizados no banco de dados e exportados para um arquivo Excel (dados_climaticos.xlsx).

### Nota
Certifique-se de que o ChromeDriver esteja corretamente instalado e configurado. O projeto utiliza o Selenium com o navegador Chrome para realizar a raspagem de dados.

