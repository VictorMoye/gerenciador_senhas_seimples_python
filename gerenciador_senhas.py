import sqlite3

MASTER_PASSSWORD = "1234"

senha_Usuario = input("Digite sua senha: ")
conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    service TEXT NOT NULL,
    username TEXT NOT NULL, 
    passwrd TEXT NOT NULL
    );
''')
    



if senha_Usuario != MASTER_PASSSWORD:
    print("Senha errada \n Encerrando...")
    break; 
    conn.close()
def Menu():
    print("* I: Inserir uma nova senha: ")
    print("L: Listar serviços salvos: ")
    print("*R: Recuperar senha:")
    print("*S: Sair !")

while(True):
    Menu()
    op = input("Qual opção deseja fazer: ").upper()
    if op not in ['I','L','R','S']:
        print("Opção Invalida !!")
        continue

    if op == 'S':
        break;
 
conn.close()
