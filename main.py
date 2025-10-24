lista_equipes = [
    ('Equipe A', [10, 9, 8, 7]),
    ('Equipe B', [8, 8, 8, 8]),
    ('Equipe C', [10, 9, 8, 10]),
    ('Equipe D', [6, 7, 8, 7]),
]

medias = [(equipe, sum(pontos)/len(pontos)) for equipe, pontos in lista_equipes]

classificacao = sorted(medias, key=lambda x:x[1], reverse=True)

print(classificacao)