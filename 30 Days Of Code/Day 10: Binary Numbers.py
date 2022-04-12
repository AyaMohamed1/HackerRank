if __name__ == '__main__':
    n = int(input().strip())
    binary_num_str = str(bin(n))[2:]
    binary_arr = binary_num_str.split('0')
    print(len(max(binary_arr)))
