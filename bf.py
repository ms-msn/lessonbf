from bs4 import BeautifulSoup
import requests



url = "https://www.specialist.ru/product/windows-server-2012-courses"
html = requests.get(url)
filename = 'Microsoft.html'
with open(filename, encoding="utf8") as file:
    text = file.read()




soup = BeautifulSoup(html.text, 'lxml')

#print(soup.prettify())
#print(soup.find_all('a'))

    
with open("hello.txt", "w") as somefile:
    for link in soup.find_all("tr"):
        for link2 in link.find_all('td'):
            print(link2.contents)
            somefile.write(str(link2.contents))
