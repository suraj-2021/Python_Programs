#Writing a function that takes input 1.City Name 2.Country Name and returns the formatted form of both country and city names.

def city_n_country(city, country):
    return f"The city {city} is in {country}"

city = input("Please enter city name: ")
country = input("Please enter which country the city is in: ")

print(city_n_country(city, country)
