# 📊 Dashboard Meteorológico — Jaraguá do Sul/SC

Aplicação desenvolvida em **Python** para consultar condições meteorológicas em tempo real por meio da API pública **Open-Meteo** e apresentá-las em uma interface web interativa construída com **Streamlit**.

## 🎯 Objetivo da Aplicação

O sistema tem como objetivo integrar uma fonte de dados externa (API REST) a uma interface gráfica de monitoramento, permitindo acompanhar de forma rápida e organizada os seguintes indicadores climáticos atuais para o município de **Jaraguá do Sul/SC**:

-   🌡️ **Temperatura do ar** (°C)
    
-   🌧️ **Umidade relativa do ar** (%)
    
-   🌡️ **Sensação térmica** (°C)
    
-   🍃 **Velocidade do vento** (km/h)
    
-   ☔ **Precipitação** (mm)
    

## 🏗️ Arquitetura e Fluxo de Dados

O projeto foi estruturado aplicando o princípio de **separação de responsabilidades**, dividindo a lógica de comunicação de dados da camada de apresentação visual:

1.  **Identificação do Endpoint:** O módulo `consumidor_api.py` define a URL base da API Open-Meteo (`https://api.open-meteo.com/v1/forecast`).
    
2.  **Definição de Parâmetros:** É montado um dicionário contendo as coordenadas geográficas de Jaraguá do Sul (`latitude: -26.48`, `longitude: -49.07`), a lista de variáveis atuais desejadas (`current`) e o fuso horário local (`timezone: America/Sao_Paulo`).
    
3.  **Requisição HTTP GET:** A biblioteca `requests` envia a solicitação ao servidor com um limite de tempo de espera (`timeout=15` segundos) para evitar travamentos.
    
4.  **Verificação da Resposta:** O método `resposta.raise_for_status()` valida o código de status HTTP, disparando uma exceção automaticamente caso ocorra algum erro na comunicação (como códigos `400`, `404` ou `500`).
    
5.  **Interpretação do JSON:** O corpo da resposta é convertido de JSON para um dicionário Python através de `resposta.json()`, isolando o bloco `dados["current"]`.
    
6.  **Seleção e Mapeamento:** Apenas os campos necessários são extraídos e retornados em um dicionário padronizado com chaves em português (`temperatura`, `umidade_relativa`, `sensacao_termica`, `velocidade_vento` e `precipitacao`).
    
7.  **Integração com a Interface:** O arquivo `frontend03.py` importa a função `obter_dados_meteorologicos()` e a executa dentro de um indicador de carregamento (`st.spinner`).
    
8.  **Exibição Visual:** Os valores retornados são organizados em três colunas (`st.columns(3)`) e exibidos por meio de cartões de métricas (`st.metric`) com suas respectivas unidades de medida.
    
9.  **Tratamento de Falhas:** Toda a operação na interface é protegida por um bloco `try/except`. Caso ocorra falha de rede, erro HTTP ou ausência de dados, a aplicação exibe uma mensagem amigável ao usuário usando `st.error()`.
    

## 🛠️ Tecnologias e Bibliotecas Utilizadas

-   **Linguagem:** Python 3
    
-   **Consumo de API HTTP:** `requests` (v2.34.2)
    
-   **Interface Web:** `streamlit` (v1.67.0)
    
-   **Manipulação de Dados (dependência auxiliar):** `pandas` (v3.1.1)
    
-   **Fonte de Dados:** [Open-Meteo Weather Forecast API](https://open-meteo.com/en/docs "null")
    

## 📁 Organização dos Arquivos

```
projeto_meteorologico/
├── .venv/               # Ambiente virtual isolado (ignorado pelo Git)
├── consumidor_api.py    # Módulo responsável pela requisição HTTP e tratamento do JSON
├── frontend03.py        # Módulo da interface web desenvolvida em Streamlit
├── requirements.txt     # Lista de dependências e versões instaladas no projeto
├── .gitignore           # Regras de exclusão de arquivos locais/temporários do versionamento
└── README.md            # Documentação técnica e guia de execução do projeto
```

## ⚙️ Requisitos e Instalação

### Pré-requisitos

-   **Python 3.x** instalado e configurado nas variáveis de ambiente (`PATH`).
    
-   **Git** instalado para controle de versão.
    
-   Conexão ativa com a internet para consultar a API externa.
    

### Passo a passo para configuração

1.  **Acesse o diretório do projeto pelo terminal (PowerShell):**
    
    ```
    cd caminho\para\projeto_meteorologico
    ```
    
2.  **Crie o ambiente virtual Python:**
    
    ```
    python -m venv .venv
    ```
    
3.  **Ative o ambiente virtual:**
    
    ```
    .\.venv\Scripts\Activate.ps1
    ```
    
    _(Confirme se o prefixo `(.venv)` apareceu no início da linha do terminal)._
    
4.  **Atualize o gerenciador de pacotes e instale as dependências:**
    
    ```
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    ```
    

## ▶️ Como Executar a Aplicação

Com o ambiente virtual ativado, inicie o servidor local do Streamlit executando:

```
python -m streamlit run frontend03.py
```

Após a inicialização, o painel será aberto automaticamente no navegador padrão através do endereço local (geralmente `http://localhost:8501`). Para atualizar as medições manualmente, utilize o botão **"🔄 Consultar novamente"** na interface.

## 🧪 Procedimentos de Teste e Validação

Para garantir o funcionamento adequado da integração, foram previstos os seguintes testes:

1.  **Validação do Endpoint (Postman / Navegador):** Envio de requisição `GET` para a URL completa com parâmetros para confirmar o retorno `200 OK` e a estrutura do objeto `"current"`:
    
    ```
    https://api.open-meteo.com/v1/forecast?latitude=-26.48&longitude=-49.07&current=temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,precipitation&timezone=America/Sao_Paulo
    ```
    
2.  **Verificação de Sintaxe dos Arquivos Python:**
    
    ```
    python -m py_compile consumidor_api.py frontend03.py
    ```
    
3.  **Teste de Tratamento de Exceções:** Simulação de indisponibilidade de rede ou alteração temporária de endpoint para validar se o `raise_for_status()` captura o erro e se o `st.error()` exibe o alerta na interface sem quebrar a aplicação.
    

## ⚠️ Limitações Conhecidas e Cuidados de Utilização

-   **Localização Fixa:** As coordenadas geográficas (`-26.48`, `-49.07`) estão definidas diretamente no código para atender ao escopo de monitoramento de Jaraguá do Sul/SC.
    
-   **Dependência de Conectividade:** Por realizar consultas em tempo real a um serviço externo, a aplicação exige acesso à internet no momento da execução.
    
-   **Limite de Requisições:** Embora a API Open-Meteo seja pública e não exija chave de autenticação (`API Key`), o uso excessivo em curto intervalo de tempo pode resultar em bloqueio temporário por limite de taxa (HTTP `429 Too Many Requests`).
