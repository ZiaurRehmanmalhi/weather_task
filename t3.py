from main_read_files import read_files
from constent import MappingIndex


file_values = read_files()

red_code = '\033[91m'
blue_code = '\033[34m'
reset_code = '\033[0m'

for file_value in file_values:
    date = file_value[MappingIndex.date]
    sliced_date = date.split('-')
    maximum_temperature = file_value[MappingIndex.maximum_temperature]
    minimum_temperature = file_value[MappingIndex.minimum_temperature]

    if maximum_temperature and minimum_temperature is not None:
        print(f"{sliced_date} {red_code} {'+' * int(maximum_temperature)} {reset_code}{maximum_temperature}C")
        print(f"{sliced_date} {blue_code} {'+' * int(minimum_temperature)} {reset_code} {minimum_temperature}C")

