from tabulate import tabulate
from tabela import TABELA

def formatar_liga_tabela(objeto):
    cabecalho = ['POS', 'TIME', 'PTS', 'J', 'V-E-D', 'GOLS', 'SG']
    linhas = []

    for time in objeto['standings'][0]['rows']:
        posicao = str(time['position']).zfill(2)
        nome_time = time['team']['name']
        pontos = time['points']
        partidas = time['matches']
        vitorias = time['wins']
        empates = time['draws']
        derrotas = time['losses']
        gols_marcados = time['scoresFor']
        gols_sofridos = time['scoresAgainst']
        saldo = gols_marcados - gols_sofridos
        ved = f'{vitorias}-{empates}-{derrotas}'
        gols = f'{gols_marcados}:{gols_sofridos}'
        linhas.append([posicao, nome_time, pontos, partidas, ved, gols, saldo])

        tabela_formatada = tabulate(linhas, headers=cabecalho, tablefmt='grid')

    return tabela_formatada

resultado = formatar_liga_tabela(TABELA)
print(resultado
