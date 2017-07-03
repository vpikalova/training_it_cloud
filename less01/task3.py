def find_most_frequent(s):
	res = []
	stat = {}
	s = s.lower()
	s = [i.rstrip("',.:;!?'") for i in s.split()]
	for i in s:
		if i in stat:
			stat[i] += 1
		else:
			stat[i] = 0
	m = -1
	for x in sorted(stat, key=stat.get, reverse=True):
		if m == -1:
			m = stat[x]
		if stat[x] == m:
			res.append(x)
		else:
			return res 




def main():
	print find_most_frequent('This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 120,571 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons Attribution/Share-Alike License 3.0 and GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk.')


if __name__ == '__main__':
	main()