# Zad.1
import random
from collections import Counter

class Stack:
    def __init__(self, *args):
        self.elements = []
        if len(args) == 1:
            match args[0]:
                case list():
                    self.elements = args[0]
                case Stack():
                    self.elements = args[0].elements
                case _:
                    raise ValueError
        else:
            self.elements.extend(args)

    def push(self, item):
        self.elements.append(item)

    def __str__(self):
        return " ".join(str(element) for element in self.elements)
    
stack1 = Stack(5, 2, 3)
stack2 = Stack([1, 2, 3])
stack3 = Stack(stack1)

stack1.push(4)

print(stack1)
print(stack2)
print(stack3)

class SortedStack(Stack):
    def __init__(self, *args):
        super().__init__(*args)
        self.elements = self.sort_stack(self.elements)

    def sort_stack(self, stack):
        if not stack:
            return stack
        type_count = Counter(map(type, stack))
        most_common_type = type_count.most_common(1)[0][0]
        filtered_stack = [item for item in stack if isinstance(item, most_common_type)]
        return sorted(filtered_stack)

    def push(self, item):
        if not self.elements or self.elements[-1] < item:
            self.elements.append(item)

sorted_stack_test = SortedStack(stack1)
sorted_stack_test.push(2)
sorted_stack_test.push(8)
print(sorted_stack_test)

sizes = []
for _ in range(100):
    sorted_stack = SortedStack()
    for _ in range(100):
        sorted_stack.push(random.randint(0,100))
    sizes.append(len(sorted_stack.elements))

average = sum(sizes)/len(sizes)
print(average)

# Zad.2
import dataclasses
import json
import os

@dataclasses.dataclass
class Employee:
    name : str
    age : int
    education : str

@dataclasses.dataclass
class JobOffer:
    description : str
    age : int
    education : str

class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

def read_or_update_database(filename, cls):
    if os.path.isfile(filename):
        with open(filename) as file:
            data = json.load(file)
            return [cls(**item) for item in data]
    else:
        return []

def save_database(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, cls=EnhancedJSONEncoder)

employees = read_or_update_database('employees.json', Employee)
job_offers = read_or_update_database('job_offers.json', JobOffer)

employee1 = Employee(name="Jan Kowalski", age=30, education="X")
employee2 = Employee(name="Anna Nowak", age=27, education="Y")
employee3 = Employee(name="Jan Kowalski", age=42, education="Z")
employees.append(employee1)
employees.append(employee2)
employees.append(employee3)

job_offers.append(JobOffer(description="Programmer", age=30, education="X"))
job_offers.append(JobOffer(description="Programmer", age=27, education="X"))

save_database('employees.json', employees)
save_database('job_offers.json', job_offers)


def match_offers_to_employee(employee, job_offers):
    matches = [offer for offer in job_offers if offer.age == employee.age and offer.education == employee.education]
    return matches


matching_offers = match_offers_to_employee(employee1, job_offers)
matching_offers2 = match_offers_to_employee(employee2, job_offers)

print("Oferr for", employee1.name, ":", matching_offers)
print("Oferr for", employee2.name, ":", matching_offers2)