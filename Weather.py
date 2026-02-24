# lab Bonus - Weather

'''
Weather Data Aggregation Program
This program stores and manages weather data for cities
Users can add, view, update, and delete weather information
'''

weather = {}

def add_weather():
    city = input("City name: ")
    date = input("Date: ")
    temp = input("Temperature: ")
    humidity = input("Humidity: ")
    condition = input("Weather condition: ")

    # إنشاء المدينة إذا لم تكن موجودة
    if city not in weather:
        weather[city] = {}

    # إضافة بيانات الطقس
    weather[city][date] = {
        "temperature": temp,
        "humidity": humidity,
        "condition": condition
    }

    print("Weather data added successfully")


def show_city_weather():
    city = input("Enter city name: ")

    if city in weather:
        for date, info in weather[city].items():
            print(date, info)
    else:
        print("City not found")


def update_weather():
    city = input("City name: ")
    date = input("Date: ")

    if city in weather and date in weather[city]:
        weather[city][date]["temperature"] = input("New temperature: ")
        weather[city][date]["humidity"] = input("New humidity: ")
        weather[city][date]["condition"] = input("New condition: ")
        print("Weather data updated")
    else:
        print("Data not found")


def delete_weather():
    city = input("City name: ")
    date = input("Date: ")

    if city in weather and date in weather[city]:
        del weather[city][date]
        print("Weather data deleted")
    else:
        print("Date not found")

while True:
    print("\n1- Add weather data")
    print("2- Show city weather")
    print("3- Update weather data")
    print("4- Delete weather data")
    print("5- Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_weather()
    elif choice == "2":
        show_city_weather()
    elif choice == "3":
        update_weather()
    elif choice == "4":
        delete_weather()
    elif choice == "5":
        print("Program closed")
        break
    else:
        print("Invalid choice")