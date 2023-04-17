import requests

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

def process_weather_information( input_text ): 
    start_ind = find_str(input_text, 'city ') 

    city_name = input_text[start_ind+len('city '):].strip()

    api_key = "c300f8e15884f0fcc93c77b210fa5f03"  # Enter the API key you got from the OpenWeatherMap website
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # This is to complete the base_url, you can also do this manually to checkout other weather data available

    complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"]
        z = x["weather"]

        current_humidity = y["humidity"]

        weather_description = z[0]["description"]

        weather_details = f"Temperature in {city_name} is (in kelvin unit) = " + str(current_temperature) + "\n Humidity = " + str(current_humidity) +  "\n description = " + str(weather_description) 
        return weather_details
    
    else:
        print(" City Not Found ")