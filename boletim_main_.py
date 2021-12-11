from time import sleep

alunos = {}
# ordem_alfabetica = sorted(alunos.keys())
alunos_reprovados = []
alunos_aprovados = []
alunos_final = []
ordem_alfabetica = []
nota_media = []
notas = []

def linha():
    """
    FUNÇÃO PARA IMPRIMIR UMA LINHA PERSONALIZADA!
    :return:
    """
    print('\033[1;97m=\033[m' * 35)


def maior_media(alunos):
    """
    FUNÇÃO COM OUTRA FORMA PARA CALCULAR MAIOR MÉDIA DO ALUNO!

    :param alunos:
    :return:
    """
    maior = menor = 0
    for nome, nota in alunos.items():
        media = sum(nota) / len(nota)
        if len(alunos) == 0:
            menor = maior = media
        else:
            if media > maior:
                maior = media
            if media < menor:
                menor = media
    linha()
    print(f'A MELHOR média da turma foi {maior}. ')
    print(f'A MENOR média da turma foi {menor}. ')
    linha()


def media_turma(alunos):
    """
    FUNÇÃO PARA CALCULAR A MÉDIA DE TODOS OS ALUNOS
    :param alunos:
    :return:
    """
    media_total = 0
    linha()
    for nome, nota in alunos.items():
        media = sum(nota) / len(nota)
        media_total += media
    print(f'Média total da turma: {media_total / len(alunos):.1f}')
    linha()


def media_aluno(alunos):
    """
    FUNÇÃO PARA CALCULAR A MÉDIA DO ALUNO!

    :param alunos:
    :return:
    """
    linha()
    for nome, nota in alunos.items():
        print(f'Média do aluno {nome}: ', end='')
        media = sum(nota) / len(nota)
        print(f'{media:.2f}')
    linha()


def maior_media_aluno(alunos):
    """
    FUNÇÃO PARA BUSCAR A MAIOR MÉDIA DO ALUNO
    VAI IMPRIMIR O NOME DO ALUNO E SUA MÉDIA.


    :param alunos:
    :return:
    """
    maior = contador = 0
    temp = ''
    linha()
    # se o len(nota) == 0 da erro, senão funciona, onde está o erro ?
    for nome, nota in alunos.items():
        media = sum(nota) / len(nota)
        if contador != len(nota) + 1:
            if contador == 0:
                maior = media
                contador += 1
                temp = nome
            else:
                if media > maior:
                    maior = media
                    temp = nome
                    contador += 1
    print(f'\033[1mA maior média é de\033[m \033[1;4;32m{temp}\033[m: \033[1;34m{maior}\033[m')
    linha()


def situaçao_aluno(alunos):
    """
    OUTRA FUNÇÃO QUE IMPRIMI TODOS A SITUAÇÃO DE TODOS OS ALUNOS EM SEQUENCIA
    :param alunos:
    :return:
    """
    print('\033[1;97m=\033[m' * 35)
    for nome, nota in alunos.items():
        print(f'Média do aluno {nome}: ', end='')
        media = sum(nota) / len(nota)
        print(f'{media:.2f}')
        if media < 5.0:
            print(f'{nome} foi Reprovado!')
            alunos_reprovados.append(nome)
        elif 5 <= media <= 6.9:
            print(f'{nome} está na Final')
            alunos_final.append(nome)
        else:
            print(f'{nome} foi Aprovado(a)!')
            alunos_aprovados.append(nome)
        print('\033[1;97m=\033[m' * 35)


def situação_final(alunos):
    """
        MOSTRA OS ALUNOS NA SITUAÇÃO NA FINAL.
        corrigir bug que nao para de imprimir.

        :param alunos:
        :return:
        """
    print('\033[1;97m=\033[m' * 25)
    contador = 1
    print(f'\033[1;31m=> \033[m Alunos \033[1;33mNA FINAL:\033[m')
    for k in alunos_final:
        print(f'{contador}. \033[1m{k}\033[m')
        contador += 1
    print('\033[1;97m=\033[m' * 25)


def situação_aprovado(alunos):
    """
        MOSTRA OS ALUNOS NA SITUAÇÃO APROVADO.
        corrigir bug que nao para de imprimir.

        :param alunos:
        :return:
        """
    print('\033[1;97m=\033[m' * 25)
    contador = 1
    print(f'\033[1;31m=> \033[m Alunos \033[1;32mAPROVADOS:\033[m')
    for k in alunos_aprovados:
        print(f'{contador}. \033[1m{k}\033[m')
        contador += 1
    print('\033[1;97m=\033[m' * 25)


def situaçao_reprovado(alunos):
    """
    MOSTRA OS ALUNOS NA SITUAÇÃO REAPROVADO.
    corrigir bug que nao para de imprimir.

    :param alunos:
    :return:
    """
    print('\033[1;97m=\033[m' * 25)
    contador = 1
    print(f'\033[1;31m=> \033[m Alunos \033[1;32mREPROVADOS:\033[m')
    for k in alunos_reprovados:
        print(f'{contador}. \033[1m{k}\033[m')
        contador += 1
    print('\033[1;97m=\033[m' * 25)


def print_similares(alunos):

    """
    CÓDIGO FEITO PELO PROFESSOR EM SASLA PARA BUSCAR ALUNOS
    ACEITAM NOMES SIMILARES... PORÉM ALGUNS DÃO BUGS, CORRIGIR DEPOIS!
    :param alunos:
    :return:
    """
    nome = str(input('Voce deseja procurar por qual aluno? ').upper().strip())
    achou = False
    for aluno in alunos:
        if nome in aluno:
            print(f'\033[1;31m=>  {aluno}\033[m encontra-se no sistema!!')
            print('\033[1;31m=> Aluno:\033[m {} \n\033[1;31m=> Nota:\033[m{}'.format(nome, alunos[nome][::]))
            achou = True
    if not achou:
        print('Não achei esse aluno, tente novamente!')


def le_entrada(mensagem, mensagem_erro, tipo, valores, loop):
    """
    FUNÇÃO FEITA PELO PROFESSOR PARA VALIDAR A ENTRADA FEITA PELO USUÁRIO
    PARA ACEITAR SOMENTE AS OPÇÕES DO PROGRAMA
    LOOP NÃO FUNCIONA(?)
    :param mensagem:
    :param mensagem_erro:
    :param tipo:
    :param valores:
    :param loop:
    :return:
    """
    try:
        entrada = tipo(input(mensagem))
        if entrada in valores:
            return entrada
        else:
            print(mensagem_erro)
    except:
        print(mensagem_erro)


def exibir_alunos(alunos):
    """
    Função para exibir a lista final dos alunos em ordem alfabética
    com as 3 notas sendo o ultimo valor a média.
    :param alunos:
    :return:
    """
    print('\033[1;97m=\033[m' * 45)
    print(f'\033[1;30;107m {"Cod":<6}{"Nome":<12}{"Nota(s)":<2}     {"Média":>10}       \033[m')
    pos = 1
    for k, v in sorted(alunos.items()):
        print('%d. - %-10s: %8s' % (pos, k, v))
        pos += 1
    print('\033[1;97m=\033[m' * 45)


def ordem_alfab(alunos):
    """
    :param alunos
    Função para ordenar os alunos em ordem alfabética
    :contador = número de ordém dos alunos
    """
    ordem_alfabetica.append(alunos)
    print('\033[1;97mAlunos em ordem alfabética: \33[m')
    contador = 1
    linha()
    for aluno in sorted(alunos.keys()):
        print(f'\033[1;97m{contador}. -\33[m {aluno}')
        contador += 1
    linha()


print('\033[1;97m=\033[m' * 120)
print('\033[1;34m>>> SISTEMA MANIPULAÇÃO DE NOTAS <<<\033[m'.center(120))
print('\033[1;97m=\033[m' * 120)
menu = '\033[1m[ 1 ]\033[m\033[0;36m Adicionar aluno;\033[m' \
       '\n\033[1m[ 2 ]\033[m\033[0;36m Adicionar nota;\033[m' \
       '\n\033[1m[ 3 ]\033[m\033[0;36m Remover aluno;\033[m' \
       '\n\033[1m[ 4 ]\033[m\033[0;36m Remover nota;\033[m' \
       '\n\033[1m[ 5 ]\033[m\033[0;36m Editar nome de aluno;\033[m' \
       '\n\033[1m[ 6 ]\033[m\033[0;36m Editar nota de aluno;\033[m' \
       '\n\033[1m[ 7 ]\033[m\033[0;36m Buscar aluno por nome;\033[m' \
       '\n\033[1m[ 8 ]\033[m\033[0;36m Calular média da turma;\033[m' \
       '\n\033[1m[ 9 ]\033[m\033[0;36m Exibir o melhor aluno;\033[m' \
       '\n\033[1m[ 10 ]\033[m\033[0;36m Exibir alunos em ordem alfabética;\033[m' \
       '\n\033[1m[ 11 ]\033[m\033[0;36m Exibir alunos ordenados por nota;\033[m' \
       '\n\033[1m[ 12 ]\033[m\033[0;36m Exibir alunos aprovados por média;\033[m' \
       '\n\033[1m[ 13 ]\033[m\033[0;36m Exibir alunos na final;\033[m' \
       '\n\033[1m[ 14 ]\033[m\033[0;36m Exibir alunos reprovados;\033[m' \
       '\n\033[1m[ 15 ]\033[m\033[0;36m Encerrar programa.\033[m' \
       '\n\033[1;31m[ => ] Digite a opção desejada: \033[;97m'

opçao = le_entrada(menu, 'Erro. Valor inválido, digite um nº de 1 a 15: ', int, [i for i in range(1, 16)], True)

while opçao != 15:
    if opçao == 1:
        nome = str(input('Digite o nome do aluno: ').upper().strip())
        if nome not in alunos:
            soma = 0
            for i in range(1, 4):
                print(f'Digite a {i}ª Nota: ', end='')
                nota = float(input())
                notas.append(nota)
                soma += nota
            media = round(soma / 3, 1)
            notas.append(media)
            media_aluno = [nome, media]
            nota_media.append(media_aluno)
            alunos[nome] = notas[:]
            notas.clear()
            print('Aluno adicionado com sucesso!', end=' ')
            #print(emoji.emojize(':check_mark:'))

    # A opção 01 incorporou a segunda opção, não conseguimos implantar o insertionsort se não fizessemos dessa forma.
    #Deixamos a 2ª opção de toda forma para o senhor avaliar.

    elif opçao == 2:
        exibir_alunos(alunos)
        nome = str(input('Digite o nome do aluno: ').upper().strip())
        if nome in alunos:
            if len(alunos[nome]) < 3:
                nota = float(input('Digite uma nota para o aluno selecionado: '))
                if nota >= 0 and nota <= 10:
                    alunos[nome].append(nota)
                    print('Nota registrada com sucesso!', end=' ')
                    #print(emoji.emojize(':check_mark:'))
                else:
                    print('ERRO! Nota inválida.', end=' ')
                    #print(emoji.emojize(':cross_mark:'))
            else:
                print('ERRO! Número máximo de notas atingido.', end=' ')
                #print(emoji.emojize(':cross_mark:'))
        else:
            print('ERRO! O aluno selecionado não está inserido no sistema', end=' ')
            #print(emoji.emojize(':cross_mark:'))
            opçao = int(input(menu))
    elif opçao == 3:
        exibir_alunos(alunos)
        nome = str(input('Voçê deseja excluir qual aluno? [cod] ').upper().strip())
        if nome in alunos:
            del alunos[nome]
            print('Aluno removido com sucesso!', end=' ')
            #print(emoji.emojize(':check_mark:'))
        else:
            print('O aluno não se encontra no sistema!', end=' ')
            #print(emoji.emojize(':cross_mark:'))
            opçao = int(input(menu))
    elif opçao == 4:
        exibir_alunos(alunos)
        nome = str(input('Voçe deseja excluir a nota de qual aluno? ').upper().strip())
        if nome in alunos:
            exibir_alunos(alunos)
            pos = int(input('Digite a posição que deseja remover: '))
            print("Notas excluidas com sucesso!!", end=' ')
            #print(emoji.emojize(':check_mark:'))
            alunos[nome][pos - 1] = 0
    elif opçao == 5:
        exibir_alunos(alunos)
        nome = str(input('Voçe deseja editar qual aluno? ').upper().strip())
        if nome in alunos:
            alunos.pop(nome)
            nome = str(input('Digite o novo aluno: ')).upper().strip()
            alunos[nome] = []
            print('Operação realizada com sucesso!', end=' ')
            #print(emoji.emojize(':check_mark:'))
        else:
            print('O aluno escolhido não se encontra no sistema!', end=' ')
            #print(emoji.emojize(':cross_mark:'))
    elif opçao == 6:
        exibir_alunos(alunos)
        nome = str(input('Voçe deseja editar a nota de qual aluno? ').upper().strip())
        if nome in alunos:
            pos_nota = int(input(f'Qual voce gostaria de editar? Digite 1, 2 ou 3 '))
            print('Operação realizada com sucesso!', end=' ')
            #print(emoji.emojize(':check_mark:'))
            nova_nota = int(input('Digite a nova nota: '))
            alunos[nome][pos_nota - 1] = nova_nota
    elif opçao == 7:
        print_similares(alunos)
    elif opçao == 8:
        media_turma(alunos)
    elif opçao == 9:
        maior_media_aluno(alunos)
    elif opçao == 10:
        print()
        ordem_alfab(alunos)
        print()
    elif opçao == 11:
        for i in range(0, len(nota_media)):
            while i > 0:
                if nota_media[i - 1][1] < nota_media[i][1]:
                    nota_media[i - 1][1], nota_media[i][1] = nota_media[i][1], nota_media[i - 1][1]
                    nota_media[i - 1][0], nota_media[i][0] = nota_media[i][0], nota_media[i - 1][0]
                i -= 1
        for i in range(0, len(nota_media)):
            nome = nota_media[i][0]
            print(f'\033[1;32mAluno:\033[m {nome} \n \033[1;34m - Nota 1:\033[m {alunos[nome][0]} \n \033[1;34m - Nota 2:\033[m {alunos[nome][1]}'
                  f'\n\033[1;34m - Nota 3:\033[m {alunos[nome][2]} \n\033[1;31m=> \033[m \033[1;36mMédia:\033[m {alunos[nome][3]}')
    elif opçao == 12:
        situaçao_aluno(alunos)
        situação_aprovado(alunos)
    elif opçao == 13:
        situaçao_aluno(alunos)
        situação_final(alunos)
    elif opçao == 14:
        situaçao_aluno(alunos)
        situaçao_reprovado(alunos)
    sleep(0.2)
    print()
    exibir_alunos(alunos)
    print()
    opçao = le_entrada(menu, 'Erro. Valor inválido, digite um nº de 1 a 15: ', int, [i for i in range(1, 16)], True)

print('\033[0;36m>>> GERANDO BOLETIM DOS ALUNOS <<<\033[m')
for i in range(0, 11):
    sleep(0.3)
    print(' .', end=' ')

print()
exibir_alunos(alunos)
print()
print('>>> Obrigado <<<\n', end=' ')
print('By: Thiago Araujo e Caio Barbosa')
