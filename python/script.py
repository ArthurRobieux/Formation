from utils import countElementInList

a = 5
b = 5

c = a + b

print("result (python) : ", c)

i = 0

# Boucles while

while(i < 5):
    i += 1
    print(i)

# liste

names = ["John", "Michel", "Jack", "Juliette", "Isabelle", "Jean-Louis", "Jack"]

print('index', names.index('Juliette'))

print("count", countElementInList(names, "Jack"))

