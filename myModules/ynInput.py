def ynCall(str):
  ans = ""
  while True:
    a = input(str + " y/n: ")
    if a == "y" or a == "n":
      ans = a
      break
    else:
      print("Input y or n.")

  return ans