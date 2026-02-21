def generate_select_statement(ids, table_name, columns):
    ids_formatted = ', '.join([str(id) for id in ids])
    columns_formatted = ', '.join(columns)
    return f"SELECT {columns_formatted} FROM {table_name} WHERE id IN ({ids_formatted});"

def write_array_to_file_as_generic_type(file_path, array_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in array_data:
            file.write(f"{item}\n")

def main():
    # Insira os IDs que deseja consultar
    ids = [1, 2, 3, 4, 5]

    # Insira o nome da tabela
    table_name = 'table_name'

    # Insira as colunas que deseja selecionar (use ['*'] para todas)
    columns = ['*']

    select_statement = generate_select_statement(ids, table_name, columns)
    file_name = 'generate_select.sql'
    write_array_to_file_as_generic_type(file_name, [select_statement])
    print(f'✅Arquivo salvo com sucesso, verifique o arquivo "{file_name}"')

if __name__ == "__main__":
    main()
