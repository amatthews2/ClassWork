class Person:
    first_name = None
    last_name = None
    age = None
    weight = None

    def __init__(self, first_name_argument, last_name_arguments, age_arguments):
        self.first_name = first_name_argument
        self.last_name = last_name_arguments
        self.age = age_arguments
        self.weight = 0

    def increase_age(self, number_years=1):
        self.age = self.age + number_years

    def print_all_info(self):
        full_name = self.print_full_name()
        print('patient name is {}'.format(full_name))
        print('patient age is {}'.format(self.age))
        print('weight is {}'.format(self.weight))

    @property
    def get_weight(self):
            return self._weight

    def set_weight(self, weight_input):
        if weight_input < 0:
            weight_input = -weight_input
        self.weight = weight_input


def create_person():
    new_person = Person("anna", "matthews", 23)
    new_person.first_name = "Anna"
    new_person.last_name = "Matthews"
    new_person.age = 23
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
    x = create_person()
    print_info(x)
    x.increase_age(10)
    x.set_weight(-120)
    print(dir(x))
    for patient in db:
        patient.print_all_info()

if __name__ = '__main_'
main()
