class Employee(object):


    employee_number = None
    name = {
    "last": None,
    "first": None,
    "middle": None
    }
    telephone = None
    address = {
    "description": None,  # Endereço
    "city": None,
    "state": None,
    "zip": None
    }
    position = {
    "title": None,
    "salary": None,  # Na media de 30 a 90
    "hours": None,
    "date_of_employment": None
    }
    abstences = []

    def __init__(self , id):
        self.employee_number = id # Não pode repetir
        #self.name['last'] = "Smith"
        #self.name['first'] = "Peter"
        #self.name['middle'] = "Robert"
        #self.telephone = "61 9" + str(random_with_N_digits(4)) + '-' + str(random_with_N_digits(4))  # 61 9XXXX-XXXX
        #self.address['description'] = "SQS 404, Bl. A, Apt 108"
        #self.address['city'] = "Brasilia"
        #self.address['state'] = "DF"
        #self.address['zip'] = "70357-100"
        #self.position['title'] = "Software Engineer"
        #self.position['salary'] = 73.00 # 30 ~ 90
        #self.position['hours'] = 30
        #self.position['date_of_employment'] = "2019-02-06"
        """
        self.abstences.append(  # Lista de faltas, pode ser vazio
            {
                    "period":
                    {
                    "initial_date": "2019-07-12",
                    "end_date": "2019-07-19"
                    },
                    "type": "vacation"
            }
        )
        """

    def set_name(self, first, middle, last):
        self.name['last'] = first
        self.name['first'] = last
        self.name['middle'] = middle
        
    def set_telephone(self, tel):
        self.telephone = tel
        
    def set_address(self, description, city, state, zip):
        self.address['description'] = description
        self.address['city'] = city
        self.address['state'] = state
        self.address['zip'] = zip
        
    def set_position(self, title, salary, hours, doe):
        self.position['title'] = title
        self.position['salary'] = salary
        self.position['hours'] = hours
        self.position['date_of_employment'] = doe
        
    def add_abstences(self, init_date, end_date, type):
         self.abstences.append(  # Lista de faltas, pode ser vazio
            {
                    "period":
                    {
                    "initial_date": init_date,
                    "end_date": end_date
                    },
                    "type": type
            }
        )