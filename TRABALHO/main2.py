# Dados de faturamento mensal para cada estadoo
faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcular valor total do mes
valor_total_mensal = sum(faturamento_mensal.values())

# Calcular percentual de representação de cada estado
for estado, valor in faturamento_mensal.items():
    percentual = (valor / valor_total_mensal) * 100
    print(f"Percentual de representação do estado {estado}: {percentual:.2f}%")

    def invert_string