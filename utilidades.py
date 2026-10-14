def ler_texto(mensagem):
    '''Pede um texto e repete ate o usuario digitar algo(nao vazio).'''
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("Este campo nao pode fficar vazio.")

def ler_inteiro(mensagem):
    '''Pede um numero intero ate o usuario digitar algo certo'''
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print( "Digite um numero intero.")

def ler_nota(mensagem):
    '''Pede uma nota de 1 a 10. Aceita virgula ou ponto.'''
    while True:
        try:
            nota = float(input(mensagem).replace(',','.'))
        except ValueError:
            print('digite um numero por exemplo 7.5')
            continue
        if 0 <= nota <= 10:
            return nota
        print('A nota deve estar entre 0 e 10.')

def calcular_media(nota1,nota2):
    '''Devolver a media simples de duas notas'''
    return (nota1 + nota2) / 2

def situacao(media):
    '''Devolver a situacao do aluno de acordo com a media'''
    if media >= 7:
        return("aprovado")
    elif media >= 5 and media < 7:
        return("recuperacao")
    else:
        return('REPROVADO!!!')
    


