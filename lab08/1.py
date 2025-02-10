import glob
import numpy
import string
import matplotlib.pyplot as plt

#1
print('Zadanie 1:')

def read_n(name, n):
    with open(name) as file:
        lines = file.readlines()
        print(lines[:n])
        print()
        print(lines[-n:])
        print()
        print(lines[::n])
        print()
        print([line.split()[n - 1] for line in lines if n <= len(line.split())])
        print()
        print([line[n - 1] for line in lines if n <= len(line)])
        print()

read_n("rank/2000.txt", 2)

#2
print('Zadanie 2:')

files = glob.glob("data/data*in")

all_data = []

for filename in files:
    with open(filename) as file:
        values = [float(value) for value in file.readlines()]
        all_data.append(values)

ave = list(map(numpy.average, zip(*all_data)))
od = list(map(numpy.std, zip(*all_data)))

with open("data.out", "w") as file:
    for i in range(len(ave)):
        file.write(f"{i + 1}\t{ave[i]}\t{od[i]}\n")

#3
print('Zadanie 3:')

def gen_plot(filename):
    content = """import matplotlib.pyplot as plt
import numpy
import glob

x1, y1, z1 = numpy.loadtxt("data.out", unpack=True)

for file in glob.glob("data/data*in"):
    y = numpy.loadtxt(file, unpack=True)
    plt.plot(x1, y, 'o', ms = 4)

plt.errorbar(x1, y1, marker='*', yerr=z1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres')
plt.savefig('res.png', dpi=300)
"""
    with open(filename, "w") as file:
        file.write(content)

gen_plot("plot.py")

#4
print('Zadanie 4:')
files = glob.glob("rank/*.txt")

data = {}
years = [year for year in range(2000,2021)]

for filename in files:
    with open(filename) as file:
        all_data = file.readlines()
        for line in all_data:
            if len(line.split()) == 2:
                name, rank  = line.split()
                rank = int(rank)
                year = int(filename[5:9])
                if name in data:
                    data[name].extend([(year, rank)])
                else:
                    data[name] = [(year, rank)]

with open("rank.out", "w") as file:
    headers = ["Nazwisko"] + [str(year) for year in years]
    file.write("\t".join(header for header in headers) + "\n")
    for name, values in sorted(data.items()): 
        line_data = [name]
        year_rank = {year : rank for year, rank in values}
        for year in years:
            if year in year_rank:
                rank = str(year_rank[year])
            else:
                rank = "-"
            line_data.append(rank)
        file.write("\t".join(line_data) + "\n")

#5
print('Zadanie 5:')

def generate_histogram(files, sortuj = True):
    letters = {}
    
    for filename in glob.glob(files):
        with open(filename) as file:
            text = file.read()
            for word in text.split():
                word = word.upper()
                if word[0] in string.ascii_uppercase:
                    if word[0] in letters:
                        letters[word[0]] += 1
                    else:
                        letters[word[0]] = 1

    if sortuj:
        letters_s = sorted(letters.items())
    else:
        letters_s = sorted(letters.items(), key = lambda item: item[1], reverse = True)
    
    plt.bar([x[0] for x in letters_s], [x[1] for x in letters_s])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Wykres')
    plt.grid(True)

    if sortuj:
        plt.title('Histogram sortowany alfabetycznie')
        plt.savefig('alfabetycznie.png')
    else:
        plt.title('Histogram sortowany po liczbie słów')
        plt.savefig('liczbowo.png')
    plt.close()

generate_histogram('zad5*in')
generate_histogram('zad5*in', sortuj = False)