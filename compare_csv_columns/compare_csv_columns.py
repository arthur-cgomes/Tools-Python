import csv

def compare_columns(file_path, column_a, column_b):
    differences = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for i, row in enumerate(csv_reader, start=2):
            val_a = row.get(column_a, '')
            val_b = row.get(column_b, '')
            if val_a != val_b:
                differences.append(
                    f"Linha {i}: '{column_a}' = '{val_a}' | '{column_b}' = '{val_b}'"
                )
    return differences

def write_array_to_file_as_generic_type(file_path, array_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in array_data:
            file.write(f"{item}\n")

def main():
    # Insira o nome do arquivo CSV de entrada
    csv_filename = 'arquivo.csv'

    # Insira o nome da coluna A para comparação
    column_a = 'coluna_a'

    # Insira o nome da coluna B para comparação
    column_b = 'coluna_b'

    differences = compare_columns(csv_filename, column_a, column_b)
    file_name = 'compare_csv_columns_output.txt'

    if not differences:
        differences = ['Nenhuma diferença encontrada entre as colunas.']

    write_array_to_file_as_generic_type(file_name, differences)
    print(f'✅Arquivo salvo com sucesso, verifique o arquivo "{file_name}"')

if __name__ == "__main__":
    main()
