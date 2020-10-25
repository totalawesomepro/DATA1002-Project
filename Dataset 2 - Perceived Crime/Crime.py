import csv
crime = csv.reader(open("Dataset 2 - Perceived Crime\\Crime.csv", encoding="utf-8-sig"))

def clean():
    clean = True
    for i in crime:
        if i == "":
            clean = False
            print("There is an empty entry")
    if clean:
        print("The dataset is clean")

def header():
    first = True
    for i in crime:
        if first:
            header = i
            first = False
    return header

def unique_years():
    first = True
    years = []
    for i in crime:
        if first:
            first = False
        else:
            if i[0] not in years:
                years.append(i[0])
    return years

def unique_countries():
    first = True
    countries = []
    for i in crime:
        if first:
            first = False
        else:
            if i[2] not in countries:
                countries.append(i[2])
    return countries