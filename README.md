# 🚀 Projeto Aurora 3 - Sistema Inteligente da Colônia de Marte

Este projeto consiste num sistema integrado de monitorização e contingência desenvolvido em **Python** para simular a gestão de recursos energéticos, consumo e análise climática de uma base humana no planeta Marte. 
O software unifica conceitos de **Estruturas de Dados**, **Lógica de Programação (Sistemas de Decisão)** e **Ciência de Dados (Modelos Preditivos)** para resolver um cenário crítico de sobrevivência espacial.

------
## 📊 Casos de Teste (Exemplos de Entrada e Saída)
 - Configuração de entrada:

"reserva_bateria": 45
"total_consumo": 70
"vento_atual": 12
"previsao_tempestade_areia": False
 
 - Configuração de saída:

--- [🤖 Sistema de Decisão: Fluxograma de Contingência] ---
🔋 Leitura da Carga de Baterias: 45 MWh
🌪️ Previsão de Tempestade de Areia: NÃO
❓ Energia das Baterias é Suficiente? -> 🛑 NÃO
🚨 Ação: Ativar Modo de Emergência
🏥 [Priorizar Suporte de Vida] -> Sistemas secundários desligados.
📉 Consumo reduzido de 70 MWh para 30 MWh.

--- [📊 Previsão de Dados (Machine Learning)] ---
💨 Vento previsto: 12 km/h
🔮 Geração Eólica estimada: 24.00 MWh

------
## 📂 Estrutura do Código

O fluxo lógico implementado segue o seguinte mapeamento de funções:

- `colonia_dados`: Base de dados estruturada com os estados atuais da colónia.
- `tomar_decisoes_fluxograma()`: Processa as variáveis de risco ambientais e dita as ações automáticas de corte de carga.
- `analisar_eficiencia()`: Executa as equações de balanço energético e consumo das baterias.
- `prever_energia_eolica()`: Aplica `np.polyfit()` nos dados históricos para traçar a linha de tendência preditiva.

------

## 🚀 Guia de Execução (Utilizando o VS Code)

Siga os passos abaixo para abrir e rodar o projeto corretamente no ambiente de desenvolvimento do VS Code.

### Passo 1: Abrir o Projeto no VS Code
1. Certifique-se de que a pasta `ProjetoAurora.Cap3` está salva no seu computador.
2. Abra o **VS Code**.
3. No menu superior, clique em **File** (Arquivo) ➔ **Open Folder...** (Abrir Pasta...).
4. Selecione a pasta do projeto e clique em **Selecionar Pasta**. 
   *(O arquivo `main.py` e este `README.md` devem aparecer na barra lateral esquerda).*

### Passo 2: Instalar as Dependências (NumPy)
O sistema utiliza a biblioteca `numpy` para realizar os cálculos da regressão linear.
1. Abra o terminal integrado do VS Code usando o atalho `Ctrl + '` ou indo no menu superior em **Terminal** ➔ **New Terminal**.
2. Digite o seguinte comando e pressione **Enter**:
   ```bash
   pip install numpy
