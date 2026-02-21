import re

def camel_to_snake(name):
    name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
    return name.lower()

def convert_names(names_string):
    names = [line.strip() for line in names_string.strip().splitlines() if line.strip()]
    return [camel_to_snake(name) for name in names]

def write_array_to_file_as_generic_type(file_path, array_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in array_data:
            file.write(f"{item}\n")

def main():
    # Insira os nomes em camelCase ou PascalCase, um por linha
    input_names = """
myVariableName
MyClassName
HTMLParser
getHTTPResponse
userId
"""

    converted = convert_names(input_names)
    file_name = 'camel_to_snake_output.txt'
    write_array_to_file_as_generic_type(file_name, converted)
    print(f'✅Arquivo salvo com sucesso, verifique o arquivo "{file_name}"')

if __name__ == "__main__":
    main()
