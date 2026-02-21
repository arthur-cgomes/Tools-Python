import re

# Insira os INSERTs que deseja transformar em DELETE
insert_statements = """
Insira os INSERTs aqui
"""

def extract_ids_from_inserts(insert_statements):
    table_name = re.search(r"INSERT INTO (\w+)", insert_statements).group(1)
    blocks = re.findall(r"\((.+?)\)", insert_statements, flags=re.DOTALL)
    ids = []
    for block in blocks:
        first_value = block.split(',')[0].strip()
        ids.append(first_value)
    return table_name, ids

def generate_delete_statements(table_name, ids):
    deletes = []
    for id_value in ids:
        deletes.append(f"DELETE FROM {table_name} WHERE id = {id_value};")
    return deletes

def write_array_to_file_as_generic_type(file_path, array_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in array_data:
            file.write(f"{item}\n")

def main():
    table_name, ids = extract_ids_from_inserts(insert_statements)
    delete_statements = generate_delete_statements(table_name, ids)
    file_name = 'transform-delete.sql'
    write_array_to_file_as_generic_type(file_name, delete_statements)
    print(f'✅Arquivo salvo com sucesso, verifique o arquivo "{file_name}"')

if __name__ == "__main__":
    main()
