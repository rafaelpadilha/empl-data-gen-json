class Employee(object):


    #employee_number = None
    

    def __init__(self , id):
        self.employee_number = id # Não pode repetir
        self.name = {
            "last": None,
            "first": None,
            "middle": None
        }
        self.telephone = None
        self.address = {
            "description": None,  # Endereço
            "city": None,
            "state": None,
            "zip": None
        }
        self.position = {
            "title": None,
            "salary": None,  # Na media de 30 a 90
            "hours": None,
            "date_of_employment": None
        }
        self.abstences = []

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

    def to_dict(self):
        return {
            "employee_number": self.employee_number,
            "name":{
                "last": self.name['last'],
                "first": self.name['first'],
                "middle": self.name['middle']
            },
            "telephone": self.telephone,
            "address:": {
                "description": self.address['description'],
                "city": self.address['city'],
                "state": self.address['state'],
                "zip": self.address['zip']
            },
            "position": {
                "title": self.position['title'],
                "salary": self.position['salary'],
                "hours": self.position['hours'],
                "date_of_employment": self.position['date_of_employment'] #TODO Formatar data "2019-02-06"
            },
            #TODO Abstences
        }