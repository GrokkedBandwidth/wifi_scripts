import csv

with open('probes2.csv', mode='r') as file1:
    reader = csv.reader(file1)
    with open('normal_mac.csv', mode='a', encoding='utf8') as file2:
        writer = csv.writer(file2)
        for item in reader:
            print(item[0])
            if item[0][1] != '2' and item[0][1] != '6' and item[0][1] != 'a' and item[0][1] != 'e':
                writer.writerow(item)

