import requests
from bs4 import BeautifulSoup

def search(word):
  ex = [[], []]
  '''
  ex[0]: exEn
  ex[1]: exJa
  '''
  t = 1
  search_word = "https://ejje.weblio.jp/sentence/content/" + word

  url = requests.get(search_word)
  soup = BeautifulSoup(url.text, "html.parser")

  exe = soup.find_all('p', class_='qotCE')
  ex[0] = [e.get_text().rstrip("発音を聞く例文帳に追加") for e in exe]

  exj = soup.find_all('p', class_='qotCJ')
  ex[1] = [j.get_text().split('-')[0].replace(u'\xa0', '') for j in exj]

  ex3 = [['', '', ''], ['', '', ''], [0, 0, 0]]

  t = 0
  for e in ex[0]:
    for i in range(3):
      if e.count(' ') > ex3[2][i] and e.count(' ') < 20:
        
        ex3[0].insert(i, e)
        ex3[1].insert(i, ex[1][t])
        ex3[2].insert(i, e.count(' '))

        for j in range(3):
          ex3[j].pop()

        break

    t += 1

  examples = []
  for i in range(3):
    ex = []
    ex.append(ex3[0][i])
    ex.append(ex3[1][i])

    examples.append(ex)

  return examples