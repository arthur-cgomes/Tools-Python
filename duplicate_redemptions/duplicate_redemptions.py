import csv
import os
from collections import defaultdict

def load_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        rows = [row for row in csv_reader]
    return rows

def find_duplicate_redeems(data):
    redeem_subtractions = defaultdict(float)
    redeem_additions = defaultdict(float)
    
    for row in data:
        if row['type'] == 'subtraction' and row['pointOrigin'] == 'redeem':
            redeem_subtractions[row['redeemId']] += float(row['value'])
        elif row['type'] == 'addition' and row['pointOrigin'] == 'redeem_refund':
            redeem_additions[row['redeemId']] += float(row['value'])
    
    duplicates = {}
    for redeem_id, total_addition in redeem_additions.items():
        total_subtraction = redeem_subtractions.get(redeem_id, 0)
        if total_addition > total_subtraction:
            excess = total_addition - total_subtraction
            duplicates[redeem_id] = (total_addition, total_subtraction, excess)
    
    return duplicates

# Define o diretório atual e caminho do CSV
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, '5a4d5616-5022-4851-abc1-6aa808e15770.csv')

# Extrai o nome do arquivo CSV (sem a extensão .csv)
csv_file_name = os.path.splitext(os.path.basename(csv_file_path))[0]

# Carrega os dados do CSV
data = load_csv(csv_file_path)

# Identifica devoluções duplicadas e calcula excessos
duplicates = find_duplicate_redeems(data)

# Caminho do arquivo de saída com o nome do arquivo CSV lido
output_file_path = os.path.join(current_dir, f'excess_points_report_{csv_file_name}.txt')

# Grava o resultado no arquivo txt
with open(output_file_path, mode='w') as file:
    for redeem_id, (total_addition, total_subtraction, excess) in duplicates.items():
        file.write(f"RedeemId: {redeem_id}, Total devolvido: {total_addition}, Resgatado: {total_subtraction}, Excesso de pontos devolvidos: {excess}\n")

print(f"Relatório gravado com sucesso em: {output_file_path}")
