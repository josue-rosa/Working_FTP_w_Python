import ftplib

def upload_content(site, remote_dir, filename, login, senha, verbose=True):
    
    local_file = open('C:\\MATERIAL_TB\\Intro.pptx', 'rb')
    site.storbinary('STOR ' + filename, local_file)

    print('Transferência realizada com sucesso!')

    site.quit()

if __name__ == '__main__':
    # login = str(input('Informe seu usuário: '))
    # senha = str(input('Informe a senha: '))

    login = 'josue.rosa'
    senha = str(input('Informe a senha do FTP: ')).strip()

    site = ftplib.FTP('127.0.0.1')

    # Realizando login
    site.login(login, senha)
    print(f'Login realizado com sucesso.\nBem-vindo {login}')


    remote_dir = site.cwd('/')
    print(site.retrlines('LIST'))
    
    filename = 'Intro.pptx'

    upload_content(site, remote_dir, filename, login, senha)
