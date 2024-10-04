import re

# Insira os INSERTs que deseja tranformar em UPDATE
insert_statements = """
Insira os INSERTs aqui
"""

def convert_insert_to_update(insert_statements):
    table_name = re.search(r"INSERT INTO (\w+)", insert_statements).group(1)
    columns = re.search(r"\((.+?)\)", insert_statements).group(1).split(',')
    columns = [col.strip() for col in columns]

    insert_blocks = re.findall(r"\((.+?)\)", insert_statements, flags=re.DOTALL)

    updates = []
    for block in insert_blocks:
        value_list = []
        in_string = False
        value = ""
        for char in block:
            if char == "'":
                in_string = not in_string
            if char == "," and not in_string:
                value_list.append(value.strip())
                value = ""
            else:
                value += char
        value_list.append(value.strip())

        set_clause = ', '.join([f"{col} = {val}" for col, val in zip(columns, value_list) if col != 'id'])
        id_value = value_list[0]
        update_statement = f"UPDATE {table_name} SET {set_clause} WHERE id = {id_value};"
        updates.append(update_statement)

    return updates

def write_array_to_file_as_generic_type(file_path, array_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in array_data:
            file.write(f"{item}\n")

def main():
    update_statements = convert_insert_to_update(insert_statements)
    file_name = 'transform-update.sql'
    write_array_to_file_as_generic_type(file_name, update_statements)
    print(f"✅ UPDATE statements have been generated and saved in {file_name}")

if __name__ == "__main__":
    main()
