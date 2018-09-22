from datetime import timedelta, datetime

pat = "%a %d %b %Y %H:%M:%S %z"
for _ in range(int(input())):
	print(int( (abs(datetime.strptime(input(), pat) - datetime.strptime(input(), pat))).total_seconds()))
