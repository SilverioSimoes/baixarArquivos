import requests

def baixar_arquivo(url, local):  
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(local, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print(f'Download finalizado. Salvo em: {local}')
    else:
      resposta.raise_for_status()
      
if __name__=='__main__':
  baixar_arquivo(url, 'teste.jpg')