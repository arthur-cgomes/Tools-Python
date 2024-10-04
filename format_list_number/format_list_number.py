import csv

def read_csv_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            numbers.extend(row)
    return numbers

def format_numbers(numbers):
    formatted_numbers = []
    
    for i, number in enumerate(numbers):
        if i == len(numbers) - 1:
            formatted_numbers.append(f"'{number}'")
        else:
            formatted_numbers.append(f"'{number}',")
    
    return '\n'.join(formatted_numbers)

def save_to_file(formatted_output, filename="format_list_number.txt"):
    with open(filename, 'w') as file:
        file.write(formatted_output)

csv_filename = 'csv_filename.csv'

numbers = read_csv_file(csv_filename)

formatted_output = format_numbers(numbers)

save_to_file(formatted_output)

print('✅Arquivo salvo com sucesso, verifique o arquivo "format_list_number.txt"')
