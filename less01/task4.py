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

def main():
	petroff = Person("Petrov", "Petro", "lol", "1952-01-02")
	print petroff.surname 
	print petroff.first_name
	print petroff.nickname 
	print petroff.birth_date 
	print petroff.get_fullname()
	print petroff.get_age() 


if __name__ == '__main__':
	main()