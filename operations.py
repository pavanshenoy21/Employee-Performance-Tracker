from file_handler import read_data, write_data

def calculate_average(p, t, w, c):
    return round((p + t + w + c) / 4, 2)

def add_record(emp_id, name, p, t, w, c):
    avg = calculate_average(p, t, w, c)
    data = read_data()
    data.append([emp_id, name, p, t, w, c, avg])
    write_data(data)

def update_record(emp_id, name, p, t, w, c):
    data = read_data()
    avg = calculate_average(p, t, w, c)

    for row in data:
        if row[0] == emp_id:
            row[1] = name
            row[2] = p
            row[3] = t
            row[4] = w
            row[5] = c
            row[6] = avg
            break

    write_data(data)

def delete_record(emp_id):
    data = read_data()
    new_data = []

    for row in data:
        if row[0] != emp_id:
            new_data.append(row)

    write_data(new_data)

def search_record(keyword):
    results = []
    data = read_data()

    for row in data:
        if keyword.lower() in row[0].lower() or keyword.lower() in row[1].lower():
            results.append(row)

    return results
