import json

# Путь к вашему JSON-файлу
file_path = 'config.json'

# Чтение текущего содержимого JSON-файла
with open(file_path, 'r') as file:
    data = json.load(file)

# Обновление данных
data['score'] += 31  # Например, обновляем возраст на 31

with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

# Вывод обновленных данных
print("Обновленные данные:")
print(json.dumps(data["score"], indent=4))