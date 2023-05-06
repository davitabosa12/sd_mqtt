# AT03
Projeto sobre MQTT

## Projetos
- **Boiler**: Lançador de eventos da caldeira.
- **CAT**: Calcula métricas da caldeira e gera alarmes de temperatura alta.
- **Alarms**: Página web que mostra alarmes e métricas da caldeira.
## Tópicos
- /boiler: Informações de temperatura da caldeira
- /boiler/cat: Alertas sobre a caldeira, computados pelo CAT

## Requisitos
- Python 3.10
- Servidor MQTT

## Configuração
A configuração é feita via variáveis de ambiente:
- MQTT_BROKER: O endereço do broker MQTT.
- MQTT_PORT: A porta onde o broker está ouvindo. Deve ser um número inteiro. (padrão: 1883)

## Como executar
1. Crie um environment Python

    Linux: `python3 -m venv venv`

    Windows: `python -m venv venv`
2. Entre no seu environment

    Linux: `source ./venv/bin/activate`

    Windows: `venv\Scripts\activate`

3. Instale as dependências:
    `pip install -r requirements.txt`

4. Execute a aplicação desejada, a partir da raiz deste projeto

    `python ./boiler`

    `python ./cat`

    `python ./alarms`