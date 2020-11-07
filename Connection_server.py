import ftplib
import time
# import zipfile

login = 'josue.rosa'
passwd = str(input('Informe a senha do FTP: ')).strip()
dir_name = '/'

site = ftplib.FTP('127.0.0.1')
print('Conectando...')
site.login(login, passwd)
time.sleep(1)
print(f'Connection Successfuly \nLogado como: {login}')

site.cwd(dir_name) # Mudar para o diretorio
print(site.retrlines('LIST')) # Listar o conteudo do diretorio

site.quit()
site.close()
print('Desconectado do servidor \n')
