import re
import os

def read_sql_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def split_into_batches(sql_content, batch_size):
    statements = re.split(r'(?=INSERT INTO)', sql_content, flags=re.IGNORECASE)
    statements = [s.strip() for s in statements if s.strip()]
    batches = []
    for i in range(0, len(statements), batch_size):
        batches.append(statements[i:i + batch_size])
    return batches

def write_batch_to_file(file_path, batch):
    with open(file_path, 'w', encoding='utf-8') as file:
        for statement in batch:
            file.write(f"{statement}\n")

def main():
    # Insira o nome do arquivo SQL de entrada
    sql_filename = 'input.sql'

    # Insira a quantidade de statements por arquivo de saída
    batch_size = 1000

    sql_content = read_sql_file(sql_filename)
    batches = split_into_batches(sql_content, batch_size)

    for i, batch in enumerate(batches, start=1):
        file_name = f'batch_{i}.sql'
        write_batch_to_file(file_name, batch)
        print(f'✅Arquivo salvo com sucesso, verifique o arquivo "{file_name}"')

if __name__ == "__main__":
    main()
