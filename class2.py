class Person:
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name_argument, last_name_arguments, age_arguments):
        self.first_name = first_name_argument
        self.last_name = last_name_arguments
        self.age = age_arguments

    def increase_age(self, number_years=1):
        self.age = self.age + number_years


def create_person(first, last, age):
    new_person = Person(first, last, age)
    return new_person


def print_info(pat):
    print("First name is {}".format(pat.first_name))
    print("Last name is {}".format(pat.last_name))
    print("age is {}".format(pat.age))


def age_patient(pat):
    pat.age = pat.age + 1
    return pat


def main():
    db = list()
    x = create_person("bob", "mat", 23)
    db.append(x)
    for patient in db:
        print("{} {}".format(patient.first_name, patient.last_name))


main()
