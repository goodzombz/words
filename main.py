file = open('1984.txt', 'r')
book = file.read()
file = open('dalloway.txt', 'r')
book += file.read()
file.close()
total = 0
letter = []
for i in book.lower():
    if i in 'abcdefghijklmnopqrstuvwxyz':
        total += 1
        letter.append(i)

for i in 'abcdefghijklmnopqrstuvwxyz':
    print(f'{i}: {str(letter.count(i)/total * 100)[:4]}')