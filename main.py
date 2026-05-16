import numpy as np

# 1. ORGANIZAÇÃO DOS DADOS (Estruturas)
# ==========================================
colonia_dados = {
    "sistema_energetico": {
        "fontes": ["solar", "eolica"],
        "geracao": {"solar": 45, "eolica": 15}, 
        "reserva_bateria": 40
    },
    "sistema_consumo": {
        "setores": {
            "suporte_vida": 30,
            "pesquisa": 25,
            "mineracao": 15
        },
        "total_consumo": 70
    },
    "clima": {
        "velocidade_vento_historico": [10, 12, 15, 18, 20], 
        "energia_gerada_historico": [20, 24, 30, 36, 40],   
        "vento_atual": 16,
        "previsao_tempestade_areia": True  # Pode ser True (Sim) ou False (Não)
    }
}

# 2. SISTEMA DE DECISÃO AUTOMÁTICA (FLUXOGRAMA INTEGRADO)
# ==========================================
def tomar_decisoes_fluxograma():
    print("\n--- [🤖 Sistema de Decisão: Fluxograma de Contingência] ---")
    
    # 1. Leitura dos dados de entrada (Camadas laranjas e azuis do diagrama)
    bateria_atual = colonia_dados["sistema_energetico"]["reserva_bateria"]
    tempestade_prevista = colonia_dados["clima"]["previsao_tempestade_areia"]
    consumo_total = colonia_dados["sistema_consumo"]["total_consumo"]
    
    print(f"🔋 Leitura da Carga de Baterias: {bateria_atual} MWh")
    print(f"🌪️ Previsão de Tempestade de Areia: {'SIM' if tempestade_prevista else 'NÃO'}")
    
    # 2. Bloco de Decisão Principal: "Energia das Baterias é Suficiente?"
    # Consideramos insuficiente se houver tempestade (bloqueia solar) OU se a bateria estiver baixa (< 50)
    if tempestade_prevista or bateria_atual < 50:
        print("❓ Energia das Baterias é Suficiente? -> 🛑 NÃO")
        print("🚨 Ação: Ativar Modo de Emergência")
        
        # Priorizar Suporte de Vida (Desliga Pesquisa e Mineração)
        novo_consumo = colonia_dados["sistema_consumo"]["setores"]["suporte_vida"]
        print(f"🏥 [Priorizar Suporte de Vida] -> Sistemas secundários desligados.")
        print(f"📉 Consumo reduzido de {consumo_total} MWh para {novo_consumo} MWh.")
        return "EMERGENCIA"
    else:
        print("❓ Energia das Baterias é Suficiente? -> 🟢 SIM")
        print("✅ Ação: Manter Sistemas Normais")
        print(f"🏥 [Priorizar Suporte de Vida] -> Operando em carga total ({consumo_total} MWh).")
        return "NORMAL"

# 3. PREVISÃO DE COMPORTAMENTO
# ==========================================
def prever_energia_eolica():
    print("\n--- [📊 Previsão de Dados (Machine Learning)] ---")
    X = np.array(colonia_dados["clima"]["velocidade_vento_historico"])
    y = np.array(colonia_dados["clima"]["energia_gerada_historico"])
    m, c = np.polyfit(X, y, 1)
    
    vento_futuro = colonia_dados["clima"]["vento_atual"]
    energia_estimada = m * vento_futuro + c
    
    print(f"💨 Vento previsto: {vento_futuro} km/h")
    print(f"🔮 Geração Eólica estimada: {energia_estimada:.2f} MWh")
    return energia_estimada

# Execução do script modificado
if __name__ == "__main__":
    print("🚀 INICIANDO SISTEMA INTELIGENTE DA COLÔNIA DE MARTE V2 🚀")
    
    # Executa a tomada de decisão baseada no novo fluxograma
    tomar_decisoes_fluxograma()
    
    # Mantém a análise preditiva
    prever_energia_eolica()