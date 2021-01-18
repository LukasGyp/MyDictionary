import glob
import csv

def openCSV():
  # ファイル選択 ---------------------------------------------
  fileList = glob.glob("data/*.csv")

  print("Choose the file you want to open")
  print("----------------------------------------")
  for f in fileList:
      print(str(fileList.index(f)) + ":" + f)
  print("n: Make a new CSV file")
  print("----------------------------------------") 
  # ----------------------------------------------------------

  # 開くファイルを指定 ---------------------------------------
  while True:
      ipt = input("Choose the option: ")

      # 新規ファイル作成 -------------------------------------
      if ipt == "n":
          name = input("What is the file neme?: ")
          file = "data/" + name + ".csv"
          mode = 'a+'
          break

      # 既存ファイル指定 -------------------------------------
      else:
          try: 
              innum = int(ipt)

          except:
              print("You typed something but number or n")
              continue

          try:
              file = fileList[innum]
              mode = 'r'
              break

          except:
              print("Listfile doesn't exist")
  # ----------------------------------------------------------

  # 単語が保存されているリストファイルを開く -----------------
  with open(file, mode, encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    l = [row for row in reader]
  print("Succeeded in opening the file: " + file)
  # ----------------------------------------------------------

  return l, file