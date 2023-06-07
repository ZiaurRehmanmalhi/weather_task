from main_read_files import read_files

file_values = read_files()
input_year = input("Enter the year: ")

highest_temp = float("-inf")
lowest_temp = float("inf")
most_humidity = float("-inf")
highest_temp_day = ""
lowest_temp_day = ""
most_humidity_day = ""

for file_value in file_values:
    year = file_value[0].split("-")[0]
    if year == input_year:
        temperatures = [float(temp) for temp in file_value[1]]
        humidities = [float(humidity) for humidity in file_value[2]]
        days = file_value[3]

        if temperatures:
            max_temp_index = temperatures.index(max(temperatures))
            if temperatures[max_temp_index] > highest_temp:
                highest_temp = temperatures[max_temp_index]
                highest_temp_day = days[max_temp_index]

            min_temp_index = temperatures.index(min(temperatures))
            if temperatures[min_temp_index] < lowest_temp:
                lowest_temp = temperatures[min_temp_index]
                lowest_temp_day = days[min_temp_index]

        if humidities:
            max_humidity_index = humidities.index(max(humidities))
            if humidities[max_humidity_index] > most_humidity:
                most_humidity = humidities[max_humidity_index]
                most_humidity_day = days[max_humidity_index]

print(f"Highest: {highest_temp}C on {highest_temp_day}")
print(f"Lowest: {lowest_temp}C on {lowest_temp_day}")
if most_humidity_day != "":
    print(f"Humidity: {most_humidity}% on {most_humidity_day}")
else:
    print("No humidity data available for the given year.")
