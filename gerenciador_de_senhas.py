wi = '=' * 16
fri = f'{wi} GERENCIADOR DE SENHAS {wi}'
print(f'{fri:^50}')
print('')
e = int(input('''Qual operação você gostaria de realizar hoje? (Digite o número correspondente)
[1] Adicionar uma nova conta
[2] Excluir uma conta adicionada
[3] Ver suas contas salvas
Sua escolha: '''))
if e == 1:
    social = str(input('Digite o nome de uma rede social: ')).strip().title()
    user = str(input('Digite o seu nome de usuário: ')).strip()
    password = str(input('Digite a sua senha: ')).strip()
    c = open('contas.txt', 'a')
    c.write('=-=' * 10)
    c.write(f'\nRede Social: {social}\n')
    c.write(f'Usuário: {user}\n')
    c.write(f'Senha: {password}\n')
    c.write('=-=' * 10)
