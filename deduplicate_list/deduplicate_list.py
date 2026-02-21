def deduplicate(input_list):
    seen = set()
    unique = []
    removed = []
    for item in input_list:
        if item in seen:
            removed.append(item)
        else:
            seen.add(item)
            unique.append(item)
    return unique, removed

def write_array_to_file_as_generic_type(file_path, array_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in array_data:
            file.write(f"{item}\n")

def main():
    # Insira a lista que deseja deduplicar
    input_list = [
        'item_1',
        'item_2',
        'item_3',
        'item_1',
    ]

    unique, removed = deduplicate(input_list)

    output_lines = []
    output_lines.append(f"Total de itens originais: {len(input_list)}")
    output_lines.append(f"Total de itens únicos: {len(unique)}")
    output_lines.append(f"Total de duplicatas removidas: {len(removed)}")
    output_lines.append("")
    output_lines.append("--- Itens únicos ---")
    output_lines.extend(unique)

    if removed:
        output_lines.append("")
        output_lines.append("--- Itens removidos (duplicatas) ---")
        output_lines.extend(removed)

    file_name = 'deduplicate_list_output.txt'
    write_array_to_file_as_generic_type(file_name, output_lines)
    print(f'✅Arquivo salvo com sucesso, verifique o arquivo "{file_name}"')

if __name__ == "__main__":
    main()
