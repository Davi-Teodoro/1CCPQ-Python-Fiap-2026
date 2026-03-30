# LÓGICA E (and)

verifica_email = True
verifica_senha = True

verifica_login = verifica_email and verifica_email
print(verifica_login)

if verifica_login:
    print("entar no progama")

# LÓGICA OU (or)

logica_ou = False or True or True
print(logica_ou)

# OPERADOR DE NEGAÇÃO (not)

negacao = not False
print(negacao)

if not verifica_login:
    print("loga certo ai....")