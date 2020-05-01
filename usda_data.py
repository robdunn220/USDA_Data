import csv


def csv_read():
    with open('USDA_Data_Refactored.csv', 'r') as csv_in, open('USDA_Data_Final.csv', 'w', newline='') as csv_out:
        data = list(csv.reader(csv_in))

        writer = csv.writer(csv_out)
        header = False
        for row in data:
            if not header:
                writer.writerow(row)
                header = True

            if row[5] == 'GA':
                writer.writerow(row)


csv_read()
