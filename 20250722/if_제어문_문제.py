strdata = "PYTHON PROGRAMMING"
strlist = [chr(ord(x)+32) if x != ' ' else x for x in strdata] # 리스트 내포 + 조건표현식
print(strlist)
print("".join(strlist)) # python programming

total = 0
for x in range(1, 101):
    if x%2 == 0:
        total += x
print("total : ", total) # 짝수의 합


my_dict = { 'a':1, 'b':2, 'c':3, 'd':4 }
rev_dict = {}
# print(type(rev_dict))
# 반복문 동작에 의해 키와 value 값을 swap 시켜서 저장하는 로직 구현
for key in my_dict:
    rev_dict[my_dict[key]] = key

print(my_dict)
print(rev_dict)


mystrdata = "#s45cD!K2ab@"
mylistdata = []

# 알파벳 영문 대소문자만 추출해서 mylistdata 에 저장
for item in mystrdata:
    if 'A' < item and item < 'z':
        mylistdata.append(item)

mystr_cov = "".join(mylistdata)
print(mystr_cov) #scDKab

wordlist = ['air', 'book', 'apple', 'atom', 'bar', 'bus', 'car', 'cost']
by_letter = {}

# 반복 구문 수행
for word in wordlist:
    letter = word[0]
    if letter in by_letter:
        by_letter[letter].append(word)
    else:
        by_letter[letter] = [word]

print(by_letter) # {'a': ['air', 'apple', 'atom'], 'b': ['book', 'bar', 'bus'], 'c': ['car', 'cost']}
