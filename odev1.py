def flatten(liste):
  l1 = []
  for i in liste:
    if type(i) == list:
      l1 += flatten(i)
    else:
      l1.append(i)
  return l1


input = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(input))