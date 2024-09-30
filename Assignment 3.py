import csv
from statistics import mean, median

def read_airport_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        airport_data = {}
        for row in reader:
            airport = row[0]
            passengers = int(row[1])
            if airport not in airport_data:
                airport_data[airport] = []
            airport_data[airport].append(passengers)
    return airport_data

def calculate_statistics(airport_data):
    statistics = {}
    for airport, passengers in airport_data.items():
        statistics[airport] = {
            'mean': mean(passengers),
            'median': median(passengers)
        }
    return statistics

def print_statistics(statistics):
    for airport, stats in statistics.items():
        print(f"Airport: {airport}, Mean Passengers: {stats['mean']}, Median Passengers: {stats['median']}")

# Main execution
airport_data = read_airport_data('Airports2.csv')
statistics = calculate_statistics(airport_data)
print_statistics(statistics)