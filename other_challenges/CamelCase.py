def camelcase(s):
    sum = 1
    for sub in s :
        if(sub.isupper()):
            sum += 1
    return sum
print(camelcase("saveChangesInTheEditor"))