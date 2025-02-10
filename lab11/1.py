import abc
import math
import numpy as np

#1
print('Zadanie 1')

class PrimeNumber1:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def isPrime(a):
        flag = 0

        if(a > 1):
            for i in range(2, int(math.sqrt(a)) + 1):
                if (a % i == 0):
                    flag = 1
                    break
            if (flag == 0):
                return True
            else:
                return False
        else:
            return False
    
    def __iter__(self):
        return PrimeNumber1(self.start, self.end)

    def __next__(self):
        while self.current <= self.end:
            candidate = self.current
            self.current += 1
            if PrimeNumber1.isPrime(candidate):
                return candidate
        raise StopIteration

series1 = PrimeNumber1(2,10)
for i in series1:
	for j in series1:
		print(f'({i},{j})', end = ' ')
	print()
print()

class PrimeNumber2:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def isPrime(a):
        flag = 0

        if(a > 1):
            for i in range(2, int(math.sqrt(a)) + 1):
                if (a % i == 0):
                    flag = 1
                    break
            if (flag == 0):
                return True
            else:
                return False
        else:
            return False
    
    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.end:
            candidate = self.current
            self.current += 1
            if PrimeNumber2.isPrime(candidate):
                return candidate
        raise StopIteration

series1 = PrimeNumber2(2,10)
for i in series1:
	for j in series1:
		print(f'({i},{j})', end = ' ')
	print()
print()

#2
print('Zadanie 2')

class Automat(abc.ABC):
    @abc.abstractmethod
    def __iter__(self):
        pass
    @abc.abstractmethod
    def __next__(self):
        pass

#3
print('Zadanie 3')

class Automat1D(Automat):
    def __init__(self, rule_number, initial_state):
        self.rule_number = rule_number
        self.state = initial_state
        self.size = len(initial_state)
        self.rule = self._rule_to_dict(rule_number)

    def __iter__(self):
        return self

    def __next__(self):
        new_state = []
        for i in range(self.size):
            left = self.state[(i - 1) % self.size]
            center = self.state[i]
            right = self.state[(i + 1) % self.size]
            neighborhood = (left << 2) | (center << 1) | right
            new_state.append(self.rule[neighborhood])
        self.state = new_state
        return self._state_to_str(new_state)

    def _rule_to_dict(self, rule_number):
        rule_str = f'{rule_number:08b}'
        return {i: int(bit) for i, bit in enumerate(reversed(rule_str))}

    def _state_to_str(self, state):
        return ''.join('*' if cell else ' ' for cell in state)

#Test
initial_state = [0] * 15 + [1] + [0] * 15
rules = [90, 94, 182]
iterations = 16

for rule in rules:
    print(f"Rule {rule}:")
    automaton = Automat1D(rule, initial_state.copy())
    for i, state in enumerate(automaton):
        if i < iterations - 1:
            print(f"Iteration {i}: {state}")
        if i >= iterations - 1:
            break
    print()

#4
print('Zadanie 4')

class Automat2D(Automat):
    def __init__(self, size, live_area):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        start = (size - live_area) // 2
        end = start + live_area
        self.grid[start:end, start:end] = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        new_grid = np.copy(self.grid)

    def _count_live_neighbors(self, x, y):
        neighbors = [
            (x-1, y-1), (x-1, y), (x-1, y+1),
            (x, y-1),           (x, y+1),
            (x+1, y-1), (x+1, y), (x+1, y+1)
        ]
        count = 0
        for nx, ny in neighbors:
            count += self.grid[nx % self.size, ny % self.size]
        return count

    def _grid_to_str(self, grid):
        return '\n'.join(''.join('*' if cell else ' ' for cell in row) for row in grid)

# Test dla automatu 2D
size = 30
live_areas = [10, 11]
iterations = 16

for live_area in live_areas:
    print(f"Live area {live_area}x{live_area}:")
    automaton = Automat2D(size, live_area)
    for i, state in enumerate(automaton):
        if i < iterations - 1:
            print(f"Iteration {i}:\n{state}\n")
        if i >= iterations - 1:
            break
    print()