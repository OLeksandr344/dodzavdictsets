#A
def difn(lst):
    return len(set(lst))
print(difn([1,2,3,4,1]))
print('----------')
#B
def count_numbers(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    common_numbers = set1.intersection(set2)
    return len(common_numbers)
print(count_numbers([1], [1,2,3]))
print('----------')
#C
def count_numbers(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    common_numbers = set1.intersection(set2)
    return list(common_numbers)
print(count_numbers([4,1,2,3], [4,1,2,3]))
print('----------')
#D
lst = [1,2,3,2,3,4]
seen = set()
for number in lst:
    if number in seen:
        print("YES")
    else:
        print("NO")
        seen.add(number)
#E
print('----------')
with open('Е.txt', 'r') as f:
    lines = f.readlines()
    num_balls = list(map(int, lines[0].split()))
    irina_balls = set(map(int, lines[1:num_balls[0]+1]))
    igor_balls = set(map(int, lines[num_balls[0]+1:]))
    common_balls = sorted(irina_balls & igor_balls)
    irina_only_balls = sorted(irina_balls - igor_balls)
    igor_only_balls = sorted(igor_balls - irina_balls)
print(*common_balls)
print(len(common_balls))
print(*irina_only_balls)
print(len(irina_only_balls)-1)
print(*igor_only_balls)
print('----------')
#f
with open('length.txt', 'r') as a:
    liness = a.readlines()
    lin_str = str(liness)
    w = lin_str.split(' ')
    w_set = set(w)
print(len(w_set)+1)
print('----------')
#g
with open('10.txt', 'r') as f:
    n = int(f.readline().strip())
    nums1 = set(map(int, f.readline().strip().split()))
    answer1 = f.readline().strip()
    nums2 = set(map(int, f.readline().strip().split()))
    answer2 = f.readline().strip()
    print(' '.join(map(str, sorted(nums1.difference(nums2)))))
print('----------')
#h
with open('r.txt', 'r') as f:
    lines = f.readlines() 
    first_row = lines[0].strip().split(' ') 
    second_row = lines[1].strip().split(' ') 
    third_row = lines[2].strip().split(' ') 
    if len(second_row) <= 5: 
        print("NO")
    else:
        print("YES")
    if len(third_row) >= 5: 
        print("YES")
    else:
        print("NO")
    yes_numbers = [] 
    for number in third_row:
        if len(second_row) <= 5 and number in third_row and number not in second_row:
            yes_numbers.append(number)
        elif len(second_row) > 5 and number in second_row and number not in third_row:
            yes_numbers.append(number)
print(' '.join(yes_numbers)) 
print('----------')
#i
my_dict = {}
with open('in.txt', 'r') as f:
    line = f.readline()
    j = int(line)
    while line:
        words = line.strip().split()
        for word in words:
            if not word.isdigit():
                my_dict[word] = my_dict.get(word, 0) + 1
        line = f.readline()
lng_lst = []
shr_lst = []
for key, value in my_dict.items():
    if value == j:
        lng_lst.append(key)
    if value >= 1:
        shr_lst.append(key)       
h = len(lng_lst)
print(h)
for key in lng_lst:
    print(key)
k = len(shr_lst)
print(k)
for key in shr_lst:
    print(key)  
print('----------')     
#j
def count_strikes(days, parties, strikes):
    strike_days = set()
    for i in range(parties):
        a, b = map(int, strikes[i])
        j = 0
        while a + j * b <= days:
            day = a + j * b
            if (day - 1) % 7 not in [5, 6]:
                strike_days.add(day)
            j += 1
    return len(strike_days)
with open('ut.txt', 'r') as f:
    days, parties = map(int, f.readline().split())
    strikes = [f.readline().split() for _ in range(parties)]
count = count_strikes(days, parties, strikes)
print(count)



    











    