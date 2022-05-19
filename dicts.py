import string
lst = [i for i in range(1, 21)]
lst1 = list(string.ascii_lowercase)
final = dict(zip(lst, lst1))
print(final)
print('GitHub works!')