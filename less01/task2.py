def f(text, limit):
	if len(text) <= limit:
		return text
	res = ""
	for i, j in enumerate(text.split()):
		res = res + j + " "
		if len(res + "...") -1 > limit:
			if i != 0:
				return res[:-len(j)-2] + "..."
			else:
				return res[:limit-3] + "..."


def main():
	print f("Proin eget tortor risus.", 24)
	print f("Proin eget tortor risus.", 23)
	print f("Proin eget tortor risus.", 6)
	print f('Python is simple to use, but it is a real programming language.', 63)

if __name__ == '__main__':
	main()
