def reverse_list(l):
 l = l[::-1]
 l = [i[::-1] for i in l]
 return l

input=[[1, 2], [3, 4], [5, 6, 7]]

print(reverse_list(input))