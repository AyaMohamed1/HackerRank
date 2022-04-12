if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 or (not(n % 2) and n >= 6 and n <=20):
        print("Weird")
    elif not(n % 2) and (n > 20 or (n >= 2 and n < 5)):
        print("Not Weird")