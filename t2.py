from main_read_files import read_files
from constent import MappingIndex

file_values = read_files()

temp_high_sum = 0
temp_low_sum = 0
humidity_sum = 0
count = 0

for file_value in file_values:
    if file_value and len(file_value) >= 6:
        temp_high_str = file_value[1]
        if temp_high_str:
            temp_high = float(temp_high_str)
            temp_high_sum += temp_high

        temp_low_str = file_value[MappingIndex.minimum_temperature]
        if temp_low_str:
            temp_low = float(temp_low_str)
            temp_low_sum += temp_low

        humidity_str = file_value[MappingIndex.humidity]
        if humidity_str:
            humidity = float(humidity_str)
            humidity_sum += humidity

        count += 1

if count > 0:
    temp_high_avg = temp_high_sum / count
    temp_low_avg = temp_low_sum / count
    humidity_avg = humidity_sum / count

    print("Average Highest Temperature:", temp_high_avg, "C")
    print("Average Lowest Temperature:", temp_low_avg, "C")
    print("Average Mean Humidity:", humidity_avg, "%")
else:
    print("No data available.")

