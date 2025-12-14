import csv
import os

FILE_NAME = "employee_reviews.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "EmployeeID", "Name",
                "Punctuality", "Teamwork",
                "WorkQuality", "Communication",
                "Average"
            ])

def read_data():
    data = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        try:
            next(reader)   
        except StopIteration:
            return data    

        for row in reader:
            data.append(row)

    return data

def write_data(data):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "EmployeeID", "Name",
            "Punctuality", "Teamwork",
            "WorkQuality", "Communication",
            "Average"
        ])
        for row in data:
            writer.writerow(row)

