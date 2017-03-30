#Bay Ridge is under the jurisdiction of Precinct 68

import csv

tickets = {}

f = open('bay_ridge_tickets_months.csv')
reader = csv.DictReader(f)

for row in reader:
        place = row["Plate ID"]
        tickets[place] = tickets.get(place, 0) + 1

worst = sorted(tickets, key = tickets.__getitem__, reverse=True)

for i in range(10):
    print("Plate", worst[i], "has", tickets[worst[i]], "tickets.")
