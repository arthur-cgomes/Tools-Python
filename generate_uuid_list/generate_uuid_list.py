import uuid

def generate_uuids(quantity):
    return [str(uuid.uuid4()) for _ in range(quantity)]

def format_uuids(uuids, format_type):
    if format_type == 1:
        return uuids
    elif format_type == 2:
        formatted = []
        for i, uid in enumerate(uuids):
            if i == len(uuids) - 1:
                formatted.append(f"'{uid}'")
            else:
                formatted.append(f"'{uid}',")
        return formatted
    else:
        raise ValueError("Tipo de formato inválido. Use 1 ou 2.")

def write_array_to_file_as_generic_type(file_path, array_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in array_data:
            file.write(f"{item}\n")

def main():
    # Insira a quantidade de UUIDs a serem gerados
    quantity = 10

    # Insira o tipo de formato desejado:
    # 1 - Um UUID por linha
    # 2 - Formato SQL (com aspas simples e vírgulas, pronto para uso em IN (...))
    format_type = 1

    uuids = generate_uuids(quantity)
    formatted = format_uuids(uuids, format_type)
    file_name = 'generate_uuid_list_output.txt'
    write_array_to_file_as_generic_type(file_name, formatted)
    print(f'✅Arquivo salvo com sucesso, verifique o arquivo "{file_name}"')

if __name__ == "__main__":
    main()
