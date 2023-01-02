import csv

filename = "./data/2022-04-24T08.50.27-140c.obsdata.csv"

with open(filename, newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=";", quotechar="|")
    row_count = 0
    for row in spamreader:
        if row_count > 2:
            if row[14] != "0":
                print(row[12])
        else:
            row_count += 1
