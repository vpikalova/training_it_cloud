def f(s):
	ans = 0
	s = s.lower()
	s = s.replace(",", "")
	s = s.replace(".", "")
	s = s.replace(":", "")
	s = s.replace(";", "")
	s = s.replace("!", "")
	s = s.replace("?", "")
	for i in s.split():
		if i == i[::-1]:
			ans += 1
	return ans


def main():
	text = raw_input()
	print f(text)


if __name__ == '__main__':
	main()