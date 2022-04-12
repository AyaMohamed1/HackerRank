phone_book = {}
n = int(input())
for que in range(0, n):
    query = input().split(' ')
    phone_book[query[0]] = query[1]
while True:
    try:
        name = input()
        if phone_book.__contains__(name):
            print(name + '=' + phone_book[name])
        else:
            print("Not found")
    except:
        break
