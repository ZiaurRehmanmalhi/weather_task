from main_read_files import read_files
from constent import MappingIndex


file_values = read_files()

for file_value in file_values:
    date = file_value[MappingIndex.date]
    sliced_date = date.split('-')
    maximum_temperature = file_value[MappingIndex.maximum_temperature]
    minimum_temperature = file_value[MappingIndex.minimum_temperature]

    if maximum_temperature and minimum_temperature is not None:
        print(f"{sliced_date}{'+' * int(maximum_temperature)} {maximum_temperature}C")
        print(f"{sliced_date}{'+' * int(minimum_temperature)} {minimum_temperature}C")

