import ftplib
import time
import zipfile

login = 'josue.rosa'
passwd = str(input('Informe a senha do FTP: ')).strip()
dir_name = '/'

conexao = ftplib.FTP('127.0.0.1')
print('Conectando...')
conexao.login(login, passwd)
time.sleep(1)
print(f'Connection Successfuly \nLogado como: {login}')

conexao.cwd(dir_name) # Mudar para o diretorio
print(conexao.retrlines('LIST')) # Listar o conteudo do diretorio

conexao.quit()
print('Desconectado do servidor \n')
