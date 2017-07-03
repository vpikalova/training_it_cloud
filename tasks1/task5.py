from datetime import datetime, date
import csv


class Person:
    surname = "Petrov"
    first_name = "Petr"
    nickname = "Petrov"
    birth_date = date(1952, 1, 2)

    def __init__(self, surname, first_name, nickname, birth_date):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    def get_age(self):
        today = date.today()
        retnum = today.timetuple()[0] - self.birth_date.timetuple()[0]
        if (today.timetuple()[7] < self.birth_date.timetuple()[7]):
            retnum -= 1
        return retnum

    def get_fullname(self):
        return (self.surname + " " + self.first_name)


def find_oldest_person(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        person = Person('', '', '',datetime.today().strftime('%Y-%m-%d'))
        for row in reader:
            person1 = Person(row[0], row[1], row[3], row[2])
            if (person1.get_age() > person.get_age()):
                person = person1
    return person.get_fullname()


def main():
    print(find_oldest_person('person.csv'))


if __name__ == '__main__':
    main()
