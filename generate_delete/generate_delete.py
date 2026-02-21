def generate_delete_statement(ids, table_name):
    ids_formatted = ', '.join([str(id) for id in ids])
    return f"DELETE FROM {table_name} WHERE id IN ({ids_formatted});"

def write_array_to_file_as_generic_type(file_path, array_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in array_data:
            file.write(f"{item}\n")

def main():
    # Insira os IDs que deseja deletar
    ids = [1, 2, 3, 4, 5]

    # Insira o nome da tabela
    table_name = 'table_name'

    delete_statement = generate_delete_statement(ids, table_name)
    file_name = 'generate_delete.sql'
    write_array_to_file_as_generic_type(file_name, [delete_statement])
    print(f'✅Arquivo salvo com sucesso, verifique o arquivo "{file_name}"')

if __name__ == "__main__":
    main()
