import requests
from bs4 import BeautifulSoup

url = 'http://servicos2.sjc.sp.gov.br/servicos/horario-e-itinerario.aspx?acao=p&opcao=1&txt='

request = requests.get(url)

soup = BeautifulSoup(request.text, 'lxml')

lista_all = soup.find_all('table', class_='textosm')

url = 'http://servicos2.sjc.sp.gov.br'

for lista_td in lista_all:
    lista = lista_td.find_all('td')
    for lista_data in lista:
        if lista_data.next_element.name== 'a':
            url_it = '{0}{1}'.format(url, lista_data.next_element.get('href'))
            print(url_it)
        else:
            print(lista_data.next_element)