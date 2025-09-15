# Dados dos filmes
filmes = [
    {
        "titulo": "Inception",
        "diretor": "Christopher Nolan",
        "bilheteria": 830,
        "avaliacoes": [9, 10, 8, 9, 10]
    },
    {
        "titulo": "Avengers: Endgame",
        "diretor": "Anthony Russo",
        "bilheteria": 2797,
        "avaliacoes": [9, 9, 10, 10, 9]
    },
    {
        "titulo": "The Dark Knight",
        "diretor": "Christopher Nolan",
        "bilheteria": 1005,
        "avaliacoes": [10, 10, 9, 10, 10]
    },
    {
        "titulo": "Jurassic Park",
        "diretor": "Steven Spielberg",
        "bilheteria": 1029,
        "avaliacoes": [8, 9, 9, 8, 9]
    }
]

# Função auxiliar: média das avaliações
def media_avaliacoes(filme):
    return sum(filme["avaliacoes"]) / len(filme["avaliacoes"])

# 1. Top 3 maiores bilheterias
def top_bilheteria(filmes):
    return sorted(filmes, key=lambda f: f["bilheteria"], reverse=True)[:3]

# 2. Top 3 melhores avaliados
def top_avaliacao(filmes):
    return sorted(filmes, key=media_avaliacoes, reverse=True)[:3]

# 3. Bilheteria total por diretor
from collections import defaultdict

def bilheteria_por_diretor(filmes):
    resultado = defaultdict(int)
    for filme in filmes:
        resultado[filme["diretor"]] += filme["bilheteria"]
    return dict(resultado)

# 4. Campeão absoluto (melhor combinação de bilheteria + nota)
def campeao(filmes):
    max_bilheteria = max(f["bilheteria"] for f in filmes)

    def score(filme):
        nota_media = media_avaliacoes(filme)
        bilheteria_normalizada = filme["bilheteria"] / max_bilheteria  # entre 0 e 1
        return nota_media * bilheteria_normalizada  # ponderação combinada

    return max(filmes, key=score)

# ----------- Resultados -----------
print(" Top 3 Bilheterias:")
for filme in top_bilheteria(filmes):
    print(f"{filme['titulo']} - ${filme['bilheteria']}M")

print("\n⭐ Top 3 Avaliações:")
for filme in top_avaliacao(filmes):
    print(f"{filme['titulo']} - Média: {media_avaliacoes(filme):.2f}")

print("\n Bilheteria por diretor:")
for diretor, total in bilheteria_por_diretor(filmes).items():
    print(f"{diretor}: ${total}M")

print("\n Campeão absoluto:")
campeao_filme = campeao(filmes)
print(f"{campeao_filme['titulo']} - Bilheteria: ${campeao_filme['bilheteria']}M - Média: {media_avaliacoes(campeao_filme):.2f}")
