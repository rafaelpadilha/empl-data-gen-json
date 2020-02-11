from emp import Employee
from random import randint
from random import randrange
from random import uniform
import datetime
from time import time
import sys
import json

AMOUNT = int(sys.argv[1])
SIZE = len(str(AMOUNT)) + 1

with open('resource/first-names.json') as fil:
    first_names = json.loads(fil.read())

with open('resource/last-names.json') as fil:
    last_names = json.loads(fil.read())

with open('resource/middle-names.json') as fil:
    middle_names = json.loads(fil.read())

with open('resource/positions.json') as fil:
    positions = json.loads(fil.read())

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def date_str(date):
    return str(date.year) + '-' + str(date.month).zfill(2) + '-' + str(date.day).zfill(2)

def random_date(start, end):
    start = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    diff = end - start
    int_diff = (diff.days * 24 * 60 * 60) + diff.seconds
    random_second = randrange(int_diff)
    date = start + datetime.timedelta(seconds=random_second)
    return date_str(date)

def fake_employee_number(list_empl):
    if(len(list_empl) > 0):
        fk_id = random_with_N_digits(SIZE)
        while fk_id in (empl.employee_number for empl in list_empl):
            fk_id = random_with_N_digits(SIZE)
        return fk_id
    else:
        return  random_with_N_digits(SIZE)

def fake_employee_name():
    return first_names[randrange(len(first_names))], middle_names[randrange(len(middle_names))], last_names[randrange(len(last_names))]

def fake_telephone():
	return str("61 9" + str(random_with_N_digits(4)) + '-' + str(random_with_N_digits(4)))

def fake_salary():
    return round(uniform(30.0, 90.0),2)
    
def fake_position():
    title = positions[randrange(len(positions))]
    tmp_h = int(randrange(5))
    if(tmp_h == 0):
        hour = 20
    elif(tmp_h == 1):
        hour = 25
    elif(tmp_h == 2):
        hour = 30
    elif(tmp_h == 3):
        hour = 35
    else:
        hour = 40

    #dt_of_empl = str(randrange(2005,2019))+ '-' + str(randrange(1,12)).zfill(2) + '-' + str(randrange(1,28)).zfill(2)
    dt_of_empl = random_date('2005-01-01','2019-12-31')
    
    return title, hour, dt_of_empl

def fake_address():
    desc = "Rua " + str(random_with_N_digits(2)) + ", Lote " + str(random_with_N_digits(2))
    city = "Brasilia"
    state = "DF"
    zip = "7" + str(random_with_N_digits(4)) + "-" + str(random_with_N_digits(3))
    return desc, city, state, zip

def fake_absences(date_of_empl):
    init_date = random_date(date_of_empl, date_str(datetime.date.today()))
    init_date = datetime.datetime.strptime(init_date, '%Y-%m-%d')
    if(randrange(1) == 0):
        # 30 dias
        end_date = init_date + datetime.timedelta(days=30)
    else:
        # 15 dias
        end_date = init_date + datetime.timedelta(days=15)
    return date_str(init_date), date_str(end_date) 
    
empl_list = []

for i in range(AMOUNT):
    empl = Employee(fake_employee_number(empl_list))

    empl.set_telephone(fake_telephone())
    
    f_name, m_name, l_name = fake_employee_name()
    empl.set_name(f_name, m_name, l_name)

    addr_desc, addr_city, addr_state, addr_zip = fake_address()
    empl.set_address(addr_desc, addr_city, addr_state, addr_zip)
    
    pos_title, pos_hours, pos_dt = fake_position()
    pos_salary = fake_salary()
    empl.set_position(pos_title, pos_salary, pos_hours, pos_dt)

    for i in range(randrange(3)):
        ab_init, ab_end = fake_absences(empl.position['date_of_employment'])
        empl.add_absences(ab_init, ab_end, "vacation")

    empl_list.append(empl)

json_data = json.dumps([empl.to_dict() for empl in empl_list],indent=4)
print(json_data)

if( len(sys.argv) == 3 ):
    with open(sys.argv[2],'w') as outfile:
        outfile.write(json_data)