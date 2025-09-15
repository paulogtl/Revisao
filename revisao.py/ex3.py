musicas = [
    {
        "titulo": "Back in Black",
        "artista": "AC/DC",
        "downloads": 6800,
        "avaliacoes": [5, 4, 5, 5, 4, 5]
    },
    {
        "titulo": "Stairway to Heaven",
        "artista": "Led Zeppelin",
        "downloads": 8900,
        "avaliacoes": [5, 5, 4, 5, 5]
    },
    {
        "titulo": "Enter Sandman",
        "artista": "Metallica",
        "downloads": 8100,
        "avaliacoes": [5, 5, 4, 4, 4, 5]
    }
]

# Função 1
def nota_media(musica):
    avaliacoes = musica["avaliacoes"]
    return sum(avaliacoes) / len(avaliacoes) if avaliacoes else 0

# Função 2
from collections import defaultdict

def artista_mais_baixado(musicas):
    total_por_artista = defaultdict(int)
    for musica in musicas:
        total_por_artista[musica["artista"]] += musica["downloads"]
    return max(total_por_artista.items(), key=lambda x: x[1])

# Função 3
def ranking_musicas(musicas):
    return sorted(
        [(musica["titulo"], nota_media(musica)) for musica in musicas],
        key=lambda x: x[1],
        reverse=True
    )

# Resultados
print("Médias de avaliação:")
for musica in musicas:
    print(f"{musica['titulo']}: {nota_media(musica):.2f}")

print("\nArtista mais baixado:", artista_mais_baixado(musicas))

print("\nRanking das músicas mais bem avaliadas:")
for titulo, media in ranking_musicas(musicas):
    print(f"{titulo}: {media:.2f}")
