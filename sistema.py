#programa principal
import banco
import utilidades

def mostrar_menu():
    print('\n=============================')
    print('SISTEMA DE NOTAS ESCOLARES')
    print('\n=============================')
    print("1 - Cadastrar aluno")
    print("2 - Lista alunos")
    print("3 - Buscar aluno")
    print('4 - Atualizar notas')
    print('5 - Remover aluno')
    print('6 - Relatorio da turma')
    print("0 - sair")
    return input('escolha uma opcao: ')

def mostrar_aluno(aluno):
    '''Mostrs ums linhs com os dados de um aluno.'''
    id_aluno, nome, nota1, nota2 = aluno
    media = utilidades.calcular.media(nota1,nota2)
    situacao = utilidades.situacao(media)
    print(f'[{id_aluno:>3}] {nome:<22}'
          f"N1: {nota1:>4.1f} n2;{nota2:>.1f}"
          f"Media: {media:4.1f} {situacao}")

def catastrar_aluno():
    print("\n--- Cadastrar o aluno ---")
    nome = utilidades.ler_texto('Nome:')
    nota1 = utilidades.ler_nota('Nota1 (0 a 10): ')
    nota2 = utilidades.ler_nota('Nota2 (0 a 10): ')
    banco.inserir_aluno(nome,nota1, nota2)
    print('Aluno cadastrado com sucesso!')

def listar_alunos():
    print("\n--- Listar a alunos ---")
    alunos = banco.listar_alunos()
    if len(alunos) == 0:
        print("nem um aluno encontrado.")
        return
    for aluno in alunos:
        mostrar_aluno()

def buscar_aluno():
    print("\n--- Cadastrar o aluno ---")
    texto = utilidades.ler_texto("Digite parte do nome do aluno: ")
    alunos = banco.buscar_por_nome(texto)
    if len(alunos) == 0:
            print("nem um aluno encontrado.")
            return
    for aluno in alunos:
            mostrar_aluno()

def atualizar_notas():
        print('\n--- Atualizar notas ---')
        id_aluno = utilidades.ler_inteiro("Digite o id do aluno: ")
        aluno  = banco.buscar_por_id(id_aluno)
        if aluno is None:
            print("Aluno nao encontrado")
            return
        mostrar_aluno()
        nota1 = utilidades.ler_nota("Nova nota 1: ")
        nota2 = utilidades.ler_nota("Nova nota 2: ")
        banco.atualizar_notas(id_aluno, nota1, nota2)
        print ("Notas atualizada")
def remover_aluno():
     print('\n--- Remover Aluno ---')
     id_aluno = utilidades.ler_inteiro("Digite ID do aluno: ")
     aluno = banco.buscar_por_id(id_aluno)
     if aluno is None:
          print("Aluno nao encontrado.")
          return
     mostrar_aluno()
     confirma = input('Tem Certeza que deseja remover? (s/n): ').lower()
     if confirma == "s":
          banco.remover_aluno(id_aluno)
          print('Aluno removido.')
     else:
          print('Remoção canselada.')
def mostrar_relatorio():
     print("\n--- Relatorio da turma ---")
     alunos = banco.listar_alunos()
     if len(alunos) == 0:
          print('Nenhum aluno cadastrado.')
          return

     soma_medias = 0
     aprovados = 0 
     recuperacao = 0
     reprovados = 0
     melhor_nome = 0 
     melhor_media = -1

     for id_aluno, nome, nota1, nota2 in alunos:
          media = utilidades.calcular_media(nota1 ,nota2)
          soma_medias += 1

          situacao = utilidades.situacao(media)
          if situacao == "Aprovado":
            aprovados +=1
          elif situacao == "Recuperacao":
            recuperacao += 1
          else:
            reprovados += 1

          if media > melhor_media:
               melhor_media = media
               melhor_nome = nome

               print(f"Total do aluno : {len(alunos)}")
               print(f"Media da turma : {soma_medias / len(alunos):.2f}")
               print(f"Aprovado       : {aprovados}")
               print(f"Em recuperacao : {recuperacao}")
               print(f"Reprovados     : {reprovados}")
               print(f"Melhor media   : {melhor_nome} ({melhor_media:1f})")


          



    
