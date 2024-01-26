from google.cloud import bigquery

# Задайте свои данные для авторизации в BigQuery
project_id = 'awesome-ridge-411708'
dataset_id = 'datasetedem'
table_id = 'route car'  # Замените на имя вашей таблицы

# Инициализация клиента BigQuery
client = bigquery.Client(project=project_id)

# Пример данных для внесения в таблицу
""" data_to_insert = [
    {"car_id": 1, "lat": 39.47328, "lon": -0.37298},
    {"car_id": 1, "lat": 39.47328, "lon": -0.373},
    {"car_id": 1, "lat": 39.47332, "lon": -0.3732},
    {"car_id": 1, "lat": 39.47339, "lon": -0.37357},
    {"car_id": 1, "lat": 39.47344, "lon": -0.37382},
    {"car_id": 1, "lat": 39.47346, "lon": -0.37389},
    {"car_id": 1, "lat": 39.47346, "lon": -0.3739},
    {"car_id": 1, "lat": 39.47354, "lon": -0.37423},
    {"car_id": 1, "lat": 39.47355, "lon": -0.37431},
    {"car_id": 1, "lat": 39.47322, "lon": -0.37431},
    {"car_id": 1, "lat": 39.47299, "lon": -0.37437},
    {"car_id": 1, "lat": 39.47274, "lon": -0.37444},
    {"car_id": 1, "lat": 39.47256, "lon": -0.37446},
    {"car_id": 1, "lat": 39.47234, "lon": -0.37442},
    {"car_id": 1, "lat": 39.47189, "lon": -0.37434},
    {"car_id": 1, "lat": 39.47186, "lon": -0.37433},
    {"car_id": 1, "lat": 39.47184, "lon": -0.37433},
    {"car_id": 1, "lat": 39.47118, "lon": -0.37425},
    {"car_id": 1, "lat": 39.47064, "lon": -0.37419},
    {"car_id": 1, "lat": 39.47061, "lon": -0.37419},
    {"car_id": 1, "lat": 39.47059, "lon": -0.37418},
    {"car_id": 1, "lat": 39.47056, "lon": -0.37417},
    {"car_id": 1, "lat": 39.47054, "lon": -0.37415},
    {"car_id": 1, "lat": 39.47052, "lon": -0.37413},
    {"car_id": 1, "lat": 39.47048, "lon": -0.37409},
    {"car_id": 1, "lat": 39.47042, "lon": -0.374},
    {"car_id": 1, "lat": 39.47034, "lon": -0.37394},
    {"car_id": 1, "lat": 39.4702, "lon": -0.37392},
    {"car_id": 1, "lat": 39.46982, "lon": -0.37389},
    {"car_id": 1, "lat": 39.46916, "lon": -0.3739},
    {"car_id": 1, "lat": 39.46881, "lon": -0.37387},
    {"car_id": 1, "lat": 39.46822, "lon": -0.37386},
    {"car_id": 1, "lat": 39.46803, "lon": -0.37386},
    {"car_id": 1, "lat": 39.46799, "lon": -0.37385},
    {"car_id": 1, "lat": 39.46796, "lon": -0.37383},
    {"car_id": 1, "lat": 39.46789, "lon": -0.37376},
    {"car_id": 1, "lat": 39.46732, "lon": -0.37457},
    {"car_id": 1, "lat": 39.46722, "lon": -0.37472},
    {"car_id": 1, "lat": 39.46719, "lon": -0.37478},
    {"car_id": 1, "lat": 39.46715, "lon": -0.37493},
    {"car_id": 1, "lat": 39.46714, "lon": -0.37497},
    {"car_id": 1, "lat": 39.46713, "lon": -0.37503},
    {"car_id": 1, "lat": 39.46712, "lon": -0.37509},
] """

data_to_insert = [
    {"car_id": 1, "lat": 39.47328, "lon": -0.37298},
    {"car_id": 1, "lat": 39.47328, "lon": -0.373},
    {"car_id": 1, "lat": 39.47332, "lon": -0.3732},
    {"car_id": 1, "lat": 39.47339, "lon": -0.37357},
    {"car_id": 1, "lat": 39.47344, "lon": -0.37382},
    {"car_id": 1, "lat": 39.47346, "lon": -0.37389},
    {"car_id": 1, "lat": 39.47346, "lon": -0.3739},
    {"car_id": 1, "lat": 39.47354, "lon": -0.37423},
    {"car_id": 1, "lat": 39.47355, "lon": -0.37431},
    {"car_id": 1, "lat": 39.47322, "lon": -0.37431},
    {"car_id": 1, "lat": 39.47299, "lon": -0.37437},
    {"car_id": 1, "lat": 39.47274, "lon": -0.37444},
    {"car_id": 1, "lat": 39.47256, "lon": -0.37446},
    {"car_id": 1, "lat": 39.47234, "lon": -0.37442},
    {"car_id": 1, "lat": 39.47189, "lon": -0.37434},
    {"car_id": 1, "lat": 39.47186, "lon": -0.37433},
    {"car_id": 1, "lat": 39.47184, "lon": -0.37433},
    {"car_id": 1, "lat": 39.47118, "lon": -0.37425},
    {"car_id": 1, "lat": 39.47064, "lon": -0.37419},
    {"car_id": 1, "lat": 39.47061, "lon": -0.37419},
    {"car_id": 1, "lat": 39.47059, "lon": -0.37418},
    {"car_id": 1, "lat": 39.47056, "lon": -0.37417},
    {"car_id": 1, "lat": 39.47054, "lon": -0.37415},
    {"car_id": 1, "lat": 39.47052, "lon": -0.37413},
    {"car_id": 1, "lat": 39.47048, "lon": -0.37409},
    {"car_id": 1, "lat": 39.47042, "lon": -0.374},
    {"car_id": 1, "lat": 39.47034, "lon": -0.37394},
    {"car_id": 1, "lat": 39.4702, "lon": -0.37392},
    {"car_id": 1, "lat": 39.46982, "lon": -0.37389},
    {"car_id": 1, "lat": 39.46916, "lon": -0.3739},
    {"car_id": 1, "lat": 39.46881, "lon": -0.37387},
    {"car_id": 1, "lat": 39.46822, "lon": -0.37386},
    {"car_id": 1, "lat": 39.46803, "lon": -0.37386},
    {"car_id": 1, "lat": 39.46799, "lon": -0.37385},
    {"car_id": 1, "lat": 39.46796, "lon": -0.37383},
    {"car_id": 1, "lat": 39.46789, "lon": -0.37376},
    {"car_id": 1, "lat": 39.46732, "lon": -0.37457},
    {"car_id": 1, "lat": 39.46722, "lon": -0.37472},
    {"car_id": 1, "lat": 39.46719, "lon": -0.37478},
    {"car_id": 1, "lat": 39.46715, "lon": -0.37493},
    {"car_id": 1, "lat": 39.46714, "lon": -0.37497},
    {"car_id": 1, "lat": 39.46713, "lon": -0.37503},
    {"car_id": 1, "lat": 39.46712, "lon": -0.37509},
    {"car_id": 1, "lat": 39.46711, "lon": -0.37515},
    {"car_id": 1, "lat": 39.46711, "lon": -0.3752},
    {"car_id": 1, "lat": 39.46711, "lon": -0.37524},
    {"car_id": 1, "lat": 39.46711, "lon": -0.3753},
    {"car_id": 1, "lat": 39.46729, "lon": -0.37595},
    {"car_id": 1, "lat": 39.46733, "lon": -0.37612},
    {"car_id": 1, "lat": 39.46744, "lon": -0.37649},
    {"car_id": 1, "lat": 39.46752, "lon": -0.37681},
    {"car_id": 1, "lat": 39.46756, "lon": -0.37697},
    {"car_id": 1, "lat": 39.46759, "lon": -0.37709},
    {"car_id": 1, "lat": 39.46764, "lon": -0.37733},
    {"car_id": 1, "lat": 39.46766, "lon": -0.37741},
    {"car_id": 1, "lat": 39.46768, "lon": -0.37748},
    {"car_id": 1, "lat": 39.46771, "lon": -0.3776},
    {"car_id": 1, "lat": 39.46776, "lon": -0.37786},
    {"car_id": 1, "lat": 39.46783, "lon": -0.37817},
    {"car_id": 1, "lat": 39.46798, "lon": -0.37886},
    {"car_id": 1, "lat": 39.4681, "lon": -0.37935},
    {"car_id": 1, "lat": 39.46819, "lon": -0.37974},
    {"car_id": 1, "lat": 39.46821, "lon": -0.37981},
    {"car_id": 1, "lat": 39.46822, "lon": -0.37986},
    {"car_id": 1, "lat": 39.46828, "lon": -0.38007},
    {"car_id": 1, "lat": 39.46828, "lon": -0.38009},
    {"car_id": 1, "lat": 39.46843, "lon": -0.38052},
    {"car_id": 1, "lat": 39.46848, "lon": -0.38065},
    {"car_id": 1, "lat": 39.46853, "lon": -0.38076},
    {"car_id": 1, "lat": 39.46858, "lon": -0.38087},
    {"car_id": 1, "lat": 39.46874, "lon": -0.38123},
    {"car_id": 1, "lat": 39.46876, "lon": -0.38129},
    {"car_id": 1, "lat": 39.46879, "lon": -0.38131},
    {"car_id": 1, "lat": 39.46882, "lon": -0.38133},
    {"car_id": 1, "lat": 39.46893, "lon": -0.38146},
    {"car_id": 1, "lat": 39.46902, "lon": -0.38157},
    {"car_id": 1, "lat": 39.46903, "lon": -0.38159},
    {"car_id": 1, "lat": 39.46913, "lon": -0.38172},
    {"car_id": 1, "lat": 39.46944, "lon": -0.38212},
    {"car_id": 1, "lat": 39.46967, "lon": -0.38243},
    {"car_id": 1, "lat": 39.46973, "lon": -0.3825},
    {"car_id": 1, "lat": 39.47024, "lon": -0.3832},
    {"car_id": 1, "lat": 39.47033, "lon": -0.38334},
    {"car_id": 1, "lat": 39.47034, "lon": -0.38335},
    {"car_id": 1, "lat": 39.47035, "lon": -0.38337},
    {"car_id": 1, "lat": 39.47037, "lon": -0.38341}
]
# Определение схемы таблицы
schema = [
    bigquery.SchemaField("car_id", "INTEGER"),
    bigquery.SchemaField("lat", "FLOAT64"),
    bigquery.SchemaField("lon", "FLOAT64"),
]

# Определение таблицы
table_ref = client.dataset(dataset_id).table(table_id)
table = bigquery.Table(table_ref, schema=schema)

# Создание таблицы, если она не существует
try:
    table = client.create_table(table)  # Создаем таблицу, если её нет
    print(f"Создана таблица {table_id}")
except Exception as e:
    print(f"Таблица {table_id} уже существует")

# Внесение данных в таблицу
errors = client.insert_rows(table, data_to_insert)

if errors == []:
    print("Данные успешно внесены в таблицу.")
else:
    print(f"Произошла ошибка при внесении данных: {errors}")
