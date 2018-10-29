import argparse
import csv

parser = argparse.ArgumentParser(description='Generate a purely text document from the wikidump xml')
parser.add_argument('h1b', metavar='h', type=str, nargs=1, help='The address for the dump file')
parser.add_argument('occupations', metavar='o', type=str, nargs=1, help='The address in which to place.')
parser.add_argument('states', metavar='s', type=str, nargs=1, help='The address in which to place.')
args = parser.parse_args()


inp = args.h1b[0]
outo = args.occupations[0]
outs = args.states[0]


print(inp)
print(outo)
print(outs)

with open(inp, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    i = 0
    for row in spamreader:
        if i == 2:
            break

        print(', '.join(row))
        i += 1