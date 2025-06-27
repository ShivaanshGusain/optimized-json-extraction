from time import perf_counter
start = perf_counter()

from orjson import loads
from numpy import array, mean

with open("C:\\Users\\Yogendar\\Desktop\\PythonProgramming\\Data Science\\Retreiving data and optimizing the process\\data.json",'r') as f:
    data = loads(f.read())
    total_age = 0
    total_salary = 0
    ages = array([(person['age'],person['salary']) for person in data['people']])
    #salaries = array([person['salary'] for person in data['people']])
print(mean(ages[:,0]))
print(mean(ages[:,1]))
end = perf_counter()
print(f'Runtime: { end-start:.6f} seconds')