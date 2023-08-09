# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"225K.00","system":"readv2"},{"code":"8G94.00","system":"readv2"},{"code":"8HHp.00","system":"readv2"},{"code":"9N54.00","system":"readv2"},{"code":"E200200","system":"readv2"},{"code":"E200400","system":"readv2"},{"code":"E200500","system":"readv2"},{"code":"E202900","system":"readv2"},{"code":"E202A00","system":"readv2"},{"code":"E202D00","system":"readv2"},{"code":"E202E00","system":"readv2"},{"code":"Eu41100","system":"readv2"},{"code":"Eu41112","system":"readv2"},{"code":"Eu41y11","system":"readv2"},{"code":"Eu41z11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anxiety-disorders---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anxiety-disorders---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anxiety-disorders---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
