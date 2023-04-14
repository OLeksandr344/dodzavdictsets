#K: Номер появи слова
word_count = {}
with open('input.txt', 'r') as text:
    for line in text:
        words = line.strip().split()
        for i, word in enumerate(words):
            if word not in word_count:
                word_count[word] = 0
            count = word_count[word]
            word_count[word] += 1
            print(count, end=' ')
print('\n---------')
#L
last_word = ''
with open('in.txt', 'r') as f:
    last_word = f.readlines()[-1].strip()
with open('in.txt', 'r') as f:
    for line in f:
        words = line.strip().split()
        print(words)
        if last_word in words:
            index = words.index(last_word)
            if index > 0:
                print(words[index - 1])
            else:
                print(words[index + 1])
            break
print('---------')
#M: Вибори в США
d = {}
with open('Mc.txt', 'r') as f:
    for line in f:
        key, value = line.strip().split()
        if key in d:
            d[key] += int(value)
        else:
            d[key] = int(value)
for key, value in d.items():
    print('{} {}'.format(key, value))
print('---------')
# Найчастіше слово
di = {}
with open('app.txt', 'r') as f:
    words = f.readlines()[0].strip().split()
    print(words)
    for word in words:
        if word not in di:
            di[word] = 0
        di[word] += 1
print(di)
max_word = ''
max_count = -1
for word, count in sorted(di.items()):
    if count > max_count:
        max_word = word
        max_count = count
print(max_word)
print('---------')
#P: Частотний аналіз
with open('v.txt', 'r') as f:
    text = f.read()
words = text.split()
freq_dict = {}
for word in words:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1
freq_list = [(freq, word) for word, freq in freq_dict.items()]
freq_list.sort(key=lambda x: (-x[0]))
for freq, word in freq_list:
    print(word)
print('---------')
#Q: Країни та міста
with open('countr.txt', 'r') as f:
    num_lists = int(f.readline().strip())
    cities = {}
    for i in range(num_lists):
        line = f.readline().strip().split()
        country = line[0]
        cities[country] = line[1:]
    while True:
        line = f.readline().strip()
        if not line:
            break
        for country, city_list in cities.items():
            if line in city_list:
                print(country)
                break
print('---------')
#R: Банківські рахунки
accounts = {}
with open("dep.txt", 'r') as f:
    for line in f:
        raxunky = line.strip().split()
        if raxunky[0] == 'DEPOSIT':
            name, amount = raxunky[1], int(raxunky[2])
            if name not in accounts:
                accounts[name] = 0
            accounts[name] += amount
        elif raxunky[0] == 'WITHDRAW':
            name, amount = raxunky[1], int(raxunky[2])
            if name not in accounts:
                 accounts[name] = 0
            accounts[name] -= amount
        elif raxunky[0] == 'BALANCE':
            name = raxunky[1]
            if name in accounts:
                print(accounts[name])
            else:
                print("ERROR")
        elif raxunky[0] == 'TRANSFER':
            name1, name2, amount = raxunky[1], raxunky[2], int(raxunky[3])
            if name1 not in accounts:
                    accounts[name1] = 0
            if name2 not in accounts:
                    accounts[name2] = 0
            accounts[name1] -= amount
            accounts[name2] += amount
        elif raxunky[0] == 'INCOME':
                p = int(raxunky[1])
                for name in accounts:
                    if accounts[name] > 0:
                        accounts[name] += int(accounts[name] * (p / 100))
        elif raxunky[0] == 'Exit':
            break
print('---------')
#S: Контрольна по наголосам
with open('fi.txt', 'r') as f:
    num_lines = int(f.readline().strip())
    slovnyk = [f.readline().strip() for _ in range(num_lines)]
    words_count = 0
    for line in f:
        for word in slovnyk:
            if word in line:
                words_count += 1
print(words_count)
print('---------')
#T: Продажі
total_amounts = {}
with open('ivanenko.txt', 'r') as file:
    for line in file:
        name, item, amount = line.split()
        amount = int(amount)
        if name not in total_amounts:
            total_amounts[name] = {}
        if item not in total_amounts[name]:
            total_amounts[name][item] = 0
        total_amounts[name][item] += amount
for name in sorted(total_amounts):
    print(f"{name}:")
    for item, amount in sorted(total_amounts[name].items()):
        print(f"{item} {amount}")
#V: Вибори в США - 2
print('---------')
with open('vyb.txt', 'r') as f:
    num_states = int(f.readline().strip())
    states = []
    vote_counts = {}
    for i in range(num_states):
        state, votes = f.readline().strip().split()
        states.append(state)
        vote_counts[state] = {'Bush': 0, 'Gore': 0}
        vote_counts[state][state] = int(votes)
    for line in f:
        state, candidate = line.strip().split()
        vote_counts[state][candidate] += 1
for state in states:
    total_votes = vote_counts[state][state]
    bush_votes = vote_counts[state]['Bush']
    gore_votes = vote_counts[state]['Gore']
    if bush_votes > gore_votes:
        winner = 'Bush'
    elif gore_votes > bush_votes:
        winner = 'Gore'
    else:
        winner = 'Draw'
    print(f"{winner} {total_votes}")
print('---------')
#O: Права доступу
with open('pr.txt', 'r') as f:
    num_files = int(f.readline().strip())
    file_permissions = {}
    for i in range(num_files):
        file, permissions = f.readline().strip().split(maxsplit=1)
        file_permissions[file] = set(permissions.split())
    num_requests = int(f.readline().strip())
    for i in range(num_requests):
        operation, file = f.readline().strip().split()
        if operation == 'read':
            if 'R' in file_permissions[file]:
                print('OK')
            else:
                print('Access denied')
        elif operation == 'write':
            if 'W' in file_permissions[file]:
                print('OK')
            else:
                print('Access denied')
        elif operation == 'execute':
            if 'X' in file_permissions[file]:
                print('OK')
            else:
                print('Access denied')




    


