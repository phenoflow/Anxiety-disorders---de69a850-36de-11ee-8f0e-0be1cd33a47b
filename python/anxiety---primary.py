# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"10344.0","system":"med"},{"code":"10390.0","system":"med"},{"code":"11280.0","system":"med"},{"code":"11602.0","system":"med"},{"code":"11890.0","system":"med"},{"code":"11913.0","system":"med"},{"code":"12508.0","system":"med"},{"code":"12635.0","system":"med"},{"code":"12838.0","system":"med"},{"code":"14729.0","system":"med"},{"code":"14780.0","system":"med"},{"code":"14890.0","system":"med"},{"code":"1510.0","system":"med"},{"code":"15220.0","system":"med"},{"code":"15811.0","system":"med"},{"code":"16199.0","system":"med"},{"code":"16638.0","system":"med"},{"code":"16729.0","system":"med"},{"code":"1723.0","system":"med"},{"code":"1758.0","system":"med"},{"code":"18248.0","system":"med"},{"code":"18603.0","system":"med"},{"code":"18672.0","system":"med"},{"code":"19000.0","system":"med"},{"code":"1907.0","system":"med"},{"code":"2300.0","system":"med"},{"code":"2366.0","system":"med"},{"code":"23838.0","system":"med"},{"code":"24066.0","system":"med"},{"code":"25638.0","system":"med"},{"code":"2571.0","system":"med"},{"code":"25749.0","system":"med"},{"code":"26331.0","system":"med"},{"code":"27685.0","system":"med"},{"code":"28106.0","system":"med"},{"code":"28167.0","system":"med"},{"code":"28925.0","system":"med"},{"code":"28938.0","system":"med"},{"code":"29322.0","system":"med"},{"code":"3076.0","system":"med"},{"code":"31672.0","system":"med"},{"code":"31957.0","system":"med"},{"code":"34064.0","system":"med"},{"code":"35825.0","system":"med"},{"code":"3685.0","system":"med"},{"code":"39518.0","system":"med"},{"code":"4069.0","system":"med"},{"code":"4081.0","system":"med"},{"code":"4167.0","system":"med"},{"code":"42000.0","system":"med"},{"code":"42788.0","system":"med"},{"code":"43050.0","system":"med"},{"code":"44321.0","system":"med"},{"code":"4534.0","system":"med"},{"code":"462.0","system":"med"},{"code":"4634.0","system":"med"},{"code":"4659.0","system":"med"},{"code":"50191.0","system":"med"},{"code":"5249.0","system":"med"},{"code":"5274.0","system":"med"},{"code":"53067.0","system":"med"},{"code":"5347.0","system":"med"},{"code":"5385.0","system":"med"},{"code":"6071.0","system":"med"},{"code":"63521.0","system":"med"},{"code":"636.0","system":"med"},{"code":"6408.0","system":"med"},{"code":"655.0","system":"med"},{"code":"67898.0","system":"med"},{"code":"67965.0","system":"med"},{"code":"6939.0","system":"med"},{"code":"72171.0","system":"med"},{"code":"7222.0","system":"med"},{"code":"7737.0","system":"med"},{"code":"7749.0","system":"med"},{"code":"7999.0","system":"med"},{"code":"8205.0","system":"med"},{"code":"8584.0","system":"med"},{"code":"9125.0","system":"med"},{"code":"9386.0","system":"med"},{"code":"962.0","system":"med"},{"code":"9785.0","system":"med"},{"code":"9944.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anxiety---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anxiety---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anxiety---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
