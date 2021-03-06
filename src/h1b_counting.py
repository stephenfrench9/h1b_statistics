import argparse
import csv

parser = argparse.ArgumentParser(description='anaylze h1b information')
parser.add_argument('h1b', metavar='h', type=str, nargs=1,
                    help='the raw data')
parser.add_argument('occupations', metavar='o', type=str, nargs=1,
                    help='results for top occupations')
parser.add_argument('states', metavar='s', type=str, nargs=1,
                    help='results for top states')
args = parser.parse_args()


"""
increment dictionary by 1 at key k
"""
def incrementK(k, dictionary):
    if k in dictionary.keys():
        dictionary[k] += 1
    else:
        dictionary[k] = 1


# read and parse the prepared csv file
with open(args.h1b[0], newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    certified = 0
    states = {}
    occupations = {}
    headerExists = True

    for row in spamreader:
        if headerExists:
            header = row
            headerExists = False
        if row[header.index('CASE_STATUS')] == "CERTIFIED":
            certified += 1
            incrementK(row[header.index('EMPLOYER_STATE')], states)
            incrementK(row[header.index('SOC_NAME')], occupations)


# Write Top States to file
if '' in states.keys():
    del states['']
results = sorted(states.items(), key=lambda x: (x[1],-ord(x[0][0]), -ord(x[0][1])), reverse=True)
with open(args.states[0], mode='w') as f:
    f.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    for count in results[0:10]:
        percent = str(round(100*count[1] / certified,1))+"%"
        f.write(str(count[0])+";" + str(count[1]) + ";" + percent+"\n")

# Write Top Occupations to file
results = sorted(occupations.items(), key=lambda x: (-x[1], x[0]), reverse=False)
with open(args.occupations[0], mode='w') as f:
    f.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    for count in results[0:10]:
        percent = str(round(100*count[1] / certified,1))+"%"
        f.write(str(count[0])+";" + str(count[1]) + ";" + percent+"\n")
