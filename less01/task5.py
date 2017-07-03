import csv

from datetime import datetime

class Person(object):
	def __init__(self, surname, first_name, birth_date, nickname=None):
		self.surname = surname
		self.first_name = first_name
		self.nickname = nickname
		self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

	def __repr__(self):
		return str(self)

	def __str__(self):
		return "{} {}".format(self.surname, self.first_name)

	def get_age(self):
		diff = datetime.today() - self.birth_date
		return diff.days / 365

	def get_fullname(self):
		return str(self)

	def _gt__(self, other):
		return self.get_age() > other.get_age()	

	def __lt__(self, other):
         return self.get_age() < other.get_age()	
	


def find_oldest_person(fName='person.csv'):
	arr = []
	with open(fName, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			arr.append(Person(*row))
	arr.sort()
	return arr[-1].get_fullname()

def main():
	print find_oldest_person()


if __name__ == '__main__':
	main()