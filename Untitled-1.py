import pandas as pd

def load_data(file_path):
    """Загрузить данные из CSV файла."""
    return pd.read_csv(file_path)

def parse_data(df):
    """Преобразовать данные в нужный формат."""
    descriptions = []
    for _, row in df.iterrows():
        description = (
            f"Пользователь {row['name']} {row['sex']} пола, {row['age']} лет "
            f"совершила покупку на {row['bill']} у.е. с мобильного браузера {row['browser']}. "
            f"Регион, из которого совершалась покупка: {row['region']}"
        )
        descriptions.append(description)
    return descriptions

def save_descriptions(descriptions, output_file):
    """Сохранить описания в TXT файл."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for description in descriptions:
            f.write(description + '\n')

def main(input_file, output_file):
    """Основная функция для обработки данных."""
    data = load_data(input_file)
    descriptions = parse_data(data)
    save_descriptions(descriptions, output_file)

# Пример использования
input_csv = '/home/rnaneru/Документы/учёба/dz8/web_clients_correct.csv'  # Полный путь к входному CSV файлу
output_txt = '/home/rnaneru/Документы/учёба/dz8/descriptions.txt'          # Полный путь к выходному TXT файлу
main(input_csv, output_txt)