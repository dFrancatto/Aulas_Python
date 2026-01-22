entrada =input('[E]ntrar  [S]air ')
senha = input('Senha: ')

senha_permitida = '123456'

#IF para saber se o usuario inputou E ou S e se digitou a senha corretamente

if entrada =='E' and senha ==senha_permitida:
    print('Entrar')

elif entrada =='E' and senha != senha_permitida:
    print('Senha incorreta')

else:
    print('Sair')