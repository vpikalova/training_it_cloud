from datetime import datetime, date
class Person:
    surname = "Petrov"
    first_name = "Petr"
    nickname = "Petrov"
    birth_date = date(1952, 1, 2)

    def __init__(self, surname, first_name, nickname, birth_date):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        self.birth_date = datetime.strptime(birth_date,"%Y-%m-%d")

    def get_age(self):
        today = date.today()
        retnum = today.timetuple()[0] - self.birth_date.timetuple()[0]
        if (today.timetuple()[7] < self.birth_date.timetuple()[7]):
            retnum -= 1
        return retnum

    def get_fullname(self):
        return (self.surname + " " + self.first_name)


def main():
    petroff = Person("Petrov", "Petro","nick", "1952-01-02")
    print(petroff.surname)
    print(petroff.first_name)
    print(petroff.nickname)
    print(petroff.birth_date)
    print(petroff.get_fullname())
    print(petroff.get_age())

if __name__ == '__main__':
    main()
