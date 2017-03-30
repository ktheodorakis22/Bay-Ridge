import csv

calls = {}

f = open('311_Service_Requests_from_2010.csv')
reader = csv.DictReader(f)

for row in reader:
        complaints = row["Complaint Type"]
        calls[complaints] = calls.get(complaints, 0) + 1

worst = sorted(calls, key = calls.__getitem__, reverse=True)

for i in range(10):
    print(worst[i], "has", calls[worst[i]], "complaints.")
