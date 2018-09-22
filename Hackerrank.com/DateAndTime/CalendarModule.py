from calendar import weekday, day_name
s = list(map(int,input().split()))
print(day_name[weekday(s[2],s[0],s[1])].upper())
