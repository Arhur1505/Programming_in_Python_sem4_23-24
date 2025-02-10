from collections import Counter
import random
import json
import dataclasses
import os

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
    
stack1 = Stack(1, 2, 3, 8, 9, 3, 2, 1, 5, 6)
stack2 = Stack(stack1)
stack3 = Stack([5, 4, 6])
stack3.push(1)
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
    def __len__(self):
        return len(self.elements)

sort1 = SortedStack(stack1)
sort1.push(5)
sort1.push(3)
print(sort1)

sizes = []
for _ in range(100):
    sorted_stack = SortedStack()
    for _ in range(100):
        sorted_stack.push(random.randint(0,100))
    sizes.append(len(sorted_stack))

average = sum(sizes)/len(sizes)
print(average)

@dataclasses.dataclass
class Pracownik:
    nazwisko: str
    wiek: int
    wyksztalcenie: str

@dataclasses.dataclass
class Oferta:
    opis: str
    wiek: int
    wyksztalcenie: str

class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

def read(filename, cls):
    if os.path.isfile(filename):
        with open(filename) as file:
            data = json.load(file)
            return [cls(**item) for item in data]
    else:
        return []

def save(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, cls=EnhancedJSONEncoder)

pracownicy = read('pracownicy.json', Pracownik)
oferty = read('oferty.json', Oferta)

p1 = Pracownik('Andrzej', 30, 'inżynier')
p2 = Pracownik('Denis', 35, 'doktor')
p3 = Pracownik('Aleksander', 40, 'licencjat')
p4 = Pracownik('Kamil', 45, 'profesor')
p5 = Pracownik('Grzegorz', 50, 'inżynier')
p6 = Pracownik('Mateusz', 55, 'liceum')
p7 = Oferta('opis1', 35, 'doktor')
p8 = Oferta('opis2', 40, 'licencjat')
p9 = Oferta('opis3', 35, 'profesor')

pracownicy.append(p1)
pracownicy.append(p2)
pracownicy.append(p3)
pracownicy.append(p4)
pracownicy.append(p5)
pracownicy.append(p6)
oferty.append(p7)
oferty.append(p8)
oferty.append(p9)

save('pracownicy.json', pracownicy)
save('oferty.json', oferty)

def znajdz(pracownik, oferty):
    dobre = [oferta for oferta in oferty if oferta.wiek == pracownik.wiek and oferta.wyksztalcenie == pracownik.wyksztalcenie]
    return dobre

z1 = znajdz(p2, oferty)
z2 = znajdz(p4, oferty)

print("Oferta dla", p2.nazwisko, ":", z1)
print("Oferta dla", p4.nazwisko, ":", z2)

