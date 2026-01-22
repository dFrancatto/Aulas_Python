entrada =input('[E]ntrar  [S]air ')
senha = input('Senha: ')

senha_permitida = '123456'

#IF para saber se o usuario inputou E ou S e se digitou a senha corretamente
#Utilizado OR para o usuario poder colocar o E em minusculo

if (entrada =='E' or entrada =='e') and senha ==senha_permitida:
    print('Entrar')

elif (entrada =='E' or entrada== 'e') and senha != senha_permitida:
    print('Senha incorreta')

else:
    print('Sair')