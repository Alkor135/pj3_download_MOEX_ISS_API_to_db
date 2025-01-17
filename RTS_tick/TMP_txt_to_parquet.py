import pandas as pd


# Чтение файла
df = pd.read_csv(
    r'C:\Users\Alkor\gd\data_ticks_finam\RTS_240905_240905.txt', 
    delimiter=','
    )
print(df)

# Сохранение DataFrame в файл .parquet
df.to_parquet(r'C:\Users\Alkor\gd\data_ticks_finam\RTS_240905_240905.parquet')

# Чтение файла .parquet
df_parquet = pd.read_parquet(r'C:\Users\Alkor\gd\data_ticks_finam\RTS_240905_240905.parquet')

# Вывод
print(df_parquet)
