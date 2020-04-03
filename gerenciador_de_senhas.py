import random
wi = '=' * 16
fri = f'{wi} GERENCIADOR DE CONTAS {wi}'
print(f'{fri:^50}')
print('')
e1 = 2
while e1 == 2:
    e = int(input('''Qual operação você gostaria de realizar hoje? (Digite o número correspondente)
[1] Adicionar uma nova conta
[2] Excluir uma conta adicionada
[3] Alterar uma senha existente
[4] Ver suas contas salvas
[5] Encerrar Programa
Sua escolha: '''))
    if e == 1:
        e1 = 1
        while e1 == 1:
            num = random.randint(1, 100)
            social = str(input('\nDigite o nome de uma rede social ou site: ')).strip().title()
            user = str(input('Digite o seu nome de usuário: ')).strip()
            password = str(input('Digite a sua senha: ')).strip()
            c = open('contas.txt', 'a')
            c.write('=-=' * 10)
            c.write(f'\nID da Conta: {num}\n')
            c.write(f'\nRede Social ou Site: {social}\n')
            c.write(f'Usuario: {user}\n')
            c.write(f'Senha: {password}\n')
            c.write('=-=' * 10)
            c.write('\n\n')
            c.close()
            e1 = int(input('''\nDeseja Adicionar uma nova conta?
[1] SIM
[2] NÃO
Sua escolha: '''))
            print('=' * 50)
    elif e == 2:
        print('\n')
        c = open('contas.txt').read().splitlines()
        for linhas in c:
            print(linhas)
        excluir = str(input('Digite o ID da conta que deseja excluir: ')).strip()
        b = open('contas.txt')
        q = b.readlines()
        for num in range(len(q)):
            if excluir in q[num]:
                for ex in range(len(q)):
                    q[num - 1] = q[num] = q[num + 1] = q[num + 2] = ''
                    q[num + 3] = q[num + 4] = q[num + 5] = q[num + 6] = ''
                b = open('contas.txt', 'w')
                b.writelines(q)
                b.close()
        print('\nConta excluída com Sucesso!!\n')
    elif e == 3:
        c = open('contas.txt').read().splitlines()
        for ler in c:
            print(ler)
        senha = str(input('\nDigite o ID da conta que deseja mudar a senha: ')).strip()
        novasenha = str(input('Digite uma nova senha: ')).strip()
        b = open('contas.txt')
        q = b.readlines()
        for num in range(len(q)):
            if senha in q[num]:
                q[num + 4] = f'Senha: {novasenha}\n'
                b = open('contas.txt', 'w')
                b.writelines(q)
                b.close()
        print('\nSenha trocada com Sucesso!!\n')
    elif e == 4:
        c = open('contas.txt').read().splitlines()
        for ler in c:
            print(ler)
    elif e == 5:
        e1 = 0
        print('\nPrograma encerrado com sucesso!\n')
