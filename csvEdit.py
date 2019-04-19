import csv

def csvWriteRow(filename, data):
	with open((filename + ".csv"), mode="a", newline="") as csv_file:
		writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(data)

def csvWrite(filename, data):
	with open((filename + ".csv"), mode="w", newline="") as csv_file:
		writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerows(data)

def csvReadRow(filename, row):
	with open((filename + ".csv")) as csv_file:
		data = list(csv.reader(csv_file, delimiter=','))
		if row > len(data):
			return ["No data, out of range"]
		else:
			return data[row]

def csvRead(filename):
	with open((filename + ".csv")) as csv_file:
		data = list(csv.reader(csv_file, delimiter=','))
		return data