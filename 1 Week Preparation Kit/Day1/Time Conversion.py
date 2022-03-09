def timeConversion(s):
    time = s.split(":")
    period = time[2][2]
    if(period == 'A'):
        if time[0] == '12':
            time[0] = '00'
            new_s = time[0] + ":" + time[1] + ":" + time[2][0:2]
            return new_s
        return s[0:8]
    else:
        if time[0] == '12':
            return s[0:8]
        time[0] = str(int(time[0]) + 12)
        new_s = time[0] + ":" + time[1] + ":" + time[2][0:2]
        return new_s

print(timeConversion("07:05:45PM"))