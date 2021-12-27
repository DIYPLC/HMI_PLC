import csv

def Write_csv_file():
    with open('Trend.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['SP', 'PV', 'OP'])
        writer.writerow(['0.0', '0.0', '0.0'])
        writer.writerow(['50.0', '49.9', '25.0'])
    return

def Read_csv_file():
    with open('Trend.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
    return

Write_csv_file()
Read_csv_file()
input()



