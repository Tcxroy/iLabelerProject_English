import csv

def read_csv(csv_file_path):
    with open(csv_file_path, "r", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data_list = []
        for row in reader:
            data_list.append(row)
            #print(data_list)
    return data_list