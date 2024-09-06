import re
import csv

def read_locations_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_location_data(locations):
    title_pattern = re.compile(r'title: "(.+?)"')
    address_pattern = re.compile(r'address: "(.+?)"')
    cep_pattern = re.compile(r'cep: "(.+?)"')
    city_pattern = re.compile(r'city: "(.+?)"')
    state_pattern = re.compile(r'state: "(.+?)"')
    country_pattern = re.compile(r'country: "(.+?)"')
    lat_pattern = re.compile(r'lat: ([\d\.-]+)')
    lng_pattern = re.compile(r'lng: ([\d\.-]+)')

    titles = title_pattern.findall(locations)
    addresses = address_pattern.findall(locations)
    ceps = cep_pattern.findall(locations)
    cities = city_pattern.findall(locations)
    states = state_pattern.findall(locations)
    countries = country_pattern.findall(locations)
    lats = lat_pattern.findall(locations)
    lngs = lng_pattern.findall(locations)

    formatted_data = []
    for i in range(len(titles)):
        formatted_data.append({
            "Nome": titles[i],
            "Endereço": addresses[i],
            "CEP": ceps[i],
            "Cidade": cities[i],
            "Estado": states[i],
            "País": countries[i],
            "lat": lats[i],
            "lng": lngs[i]
        })

    return formatted_data

def write_to_csv(file_path, data):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Nome", "Endereço", "CEP", "Cidade", "Estado", "País", "lat", "lng"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    file_path = './get_info_site/locations.txt'
    
    locations = read_locations_file(file_path)
    
    formatted_data = extract_location_data(locations)
    
    output_csv = './get_info_site/formatted_locations.csv'
    write_to_csv(output_csv, formatted_data)
    
    print(f"✅ Dados formatados foram gerados e salvos em {output_csv}")

if __name__ == "__main__":
    main()
