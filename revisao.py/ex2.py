# Dados
atletas = [
    {
        "nome": "Lucas",
        "idade": 20,
        "modalidades": ["Natação", "Corrida"],
        "treinos": {"Natação": 12, "Corrida": 8}
    },
    {
        "nome": "Mariana",
        "idade": 25,
        "modalidades": ["Musculação", "Yoga", "Pilates"],
        "treinos": {"Musculação": 15, "Yoga": 10, "Pilates": 5}
    },
    {
        "nome": "João",
        "idade": 22,
        "modalidades": ["Corrida", "Ciclismo"],
        "treinos": {"Corrida": 20, "Ciclismo": 18}
    }
]

# Funções
def media_idade_por_modalidade(atletas, esporte):
    idades = [atleta["idade"] for atleta in atletas if esporte in atleta["modalidades"]]
    return sum(idades) / len(idades) if idades else 0

def esporte_mais_treinado(atleta):
    return max(atleta["treinos"].items(), key=lambda item: item[1])[0]

def atletas_com_mais_de_duas_modalidades(atletas):
    return [atleta["nome"] for atleta in atletas if len(atleta["modalidades"]) > 2]

# Exemplos
print("Média de idade (Corrida):", media_idade_por_modalidade(atletas, "Corrida"))
print("Mais treinado (Mariana):", esporte_mais_treinado(atletas[1]))
print("Atletas com mais de 2 modalidades:", atletas_com_mais_de_duas_modalidades(atletas))
