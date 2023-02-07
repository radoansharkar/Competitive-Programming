for i in range(int(input())):
	s = input()
	rev = s[::-1]
	if s == rev:
		ans = "Yes"
	else:
		ans = "No"
	print(f"Case {i+1}: {ans}")
