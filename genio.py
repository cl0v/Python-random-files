
# # melhor maneira de criar uma lista de valores


monstros = ["a", "b", "c", "b", "c", "a", "a"]
# os valores inciais sao os primeiros valores, depois guardo
# valores na sequencia e trato cada um deles de maneira isolada

for m in monstros[3:]:
  if m == monstros[0]:
    print ("a")
  elif m == monstros[1]:
    print ("b")
  elif m == monstros[2]:
    print ("c")