import csv
import json

def read_csv_as_dicts(file_path):
    rows = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            rows.append(dict(row))
    return rows

def save_to_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    # Insira o nome do arquivo CSV de entrada
    csv_filename = 'csv_filename.csv'

    file_name = 'csv_to_json.json'
    rows = read_csv_as_dicts(csv_filename)
    save_to_file(rows, file_name)
    print(f'✅Arquivo salvo com sucesso, verifique o arquivo "{file_name}"')

if __name__ == "__main__":
    main()
