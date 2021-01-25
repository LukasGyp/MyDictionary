import requests
from bs4 import BeautifulSoup
import csv
import myModules.ynInput
from myModules.openFile import openCSV
import myModules.searchExamples

l = [['', '']]
l, file = openCSV()
    
while True:
    # 検索する単語を入力------------------------------------
    print("----------------------------------------")
    word = input("search word(if you want to exit, input e):")
    # ------------------------------------------------------

    # プログラムを終了 -------------------------------------
    if word == 'e':
        print("See you")
        break
    # ------------------------------------------------------

    # すでに保存されている単語かどうかチェック -------------
    flag = False
    for exist_word in l:
        if exist_word[0] == word:
            exist_word_verif = myModules.ynInput.ynCall("This word is already registered. Check mean?")
            if exist_word_verif == "y":
                print(exist_word[1])
            flag = True
            break
    if flag: 
      continue            
    # ------------------------------------------------------

    # urlを検索・スクレイピング ----------------------------
    search_word = "https://ejje.weblio.jp/content/" + word

    try:
        url = requests.get(search_word)
        soup = BeautifulSoup(url.text, "html.parser")
        word_mean = soup.find(class_='content-explanation ej').get_text()

    except:
        print("This word doesn't exist. Start again.")
        continue
    # ------------------------------------------------------

    # 単語の意味を表示 -------------------------------------
    print(word_mean)
    # ------------------------------------------------------

    # 例文を取得 -------------------------------------------
    ex = myModules.searchExamples.search(word)
    examples = sum(ex, [])

    # リストファイルに追加するかどうか選択 -----------------
    append_or_not = myModules.ynInput.ynCall("Do you want to append?")

    if append_or_not == "y":
        data = [word, word_mean]
        data.extend(examples)
        with open(file, 'a', encoding="utf-8-sig") as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(data)
            print('Completed.')
        l.append(data)
    # ------------------------------------------------------

    
    
'''
今後の改善点
・同綴異義語の検索
'''