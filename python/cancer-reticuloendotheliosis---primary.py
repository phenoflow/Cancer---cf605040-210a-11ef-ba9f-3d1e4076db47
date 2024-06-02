# Siobhan Reilly, Ivan Olier, Claire Planner, Tim Doran, David Reeves, Darren M Ashcroft, Linda Gask, Evangelos Kontopantelis, 2024.

import sys, csv, re

codes = [{"code":"B18y600","system":"readv2"},{"code":"B624.00","system":"readv2"},{"code":"B624.11","system":"readv2"},{"code":"ByuC300","system":"readv2"},{"code":"B58y411","system":"readv2"},{"code":"Byu4200","system":"readv2"},{"code":"ByuC400","system":"readv2"},{"code":"B624z00","system":"readv2"},{"code":"B1z..00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cancer-reticuloendotheliosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cancer-reticuloendotheliosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cancer-reticuloendotheliosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
