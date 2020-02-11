from emp import Employee
from random import randint
import json

AMOUNT = 50
SIZE = 4 

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def fake_employee_number(list_empl):
    if(len(list_empl) > 0):
        fk_id = random_with_N_digits(SIZE)
        while fk_id in (empl.employee_number for empl in list_empl):
            fk_id = random_with_N_digits(SIZE)
        return fk_id
    else:
        return  random_with_N_digits(SIZE)
        

def fake_telephone():
	return str("61 9" + str(random_with_N_digits(4)) + '-' + str(random_with_N_digits(4)))

def fake_salary():
    pass
    
def fake_position():
    pass

def fake_address():
    pass

empl_list = []

for i in range(AMOUNT):
    empl = Employee(fake_employee_number(empl_list))
    empl.set_telephone(fake_telephone())
    empl_list.append(empl)
    

json_data = json.dumps([empl.__dict__ for empl in empl_list])
print(json_data)