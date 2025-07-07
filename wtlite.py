import requests, sys

# Global data for what to fetch and print
includeTemperature = False
includeRain = False
includeWind = False
location = "London"

def printBanner():
    print(""" _       ____  __    _ __
| |     / / /_/ /   (_) /____
| | /| / / __/ /   / / __/ _ \\
| |/ |/ / /_/ /___/ / /_/  __/
|__/|__/\__/_____/_/\__/\___/ """)
    return

def fetchWeatherData():
    # Base URL for wttr.in
    fullRequest = f"https://wttr.in/{location}?format="

    # Add parts to the URL
    if includeTemperature:
        fullRequest += "%t "

    if includeRain:
        fullRequest += "%p "

    if includeWind:
        fullRequest += "%w "
  
    # Perform the request
    try:
        response = requests.get(fullRequest)
        response.raise_for_status()  # Check if the request was successful
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        sys.exit(1)

def printWeatherData(weatherData):
    weatherTokens = weatherData.text.split(" ")

    # Printing temperature
    if includeTemperature:
        print(f"Temperature: {weatherTokens[0]}")

    # Printing rain
    if includeRain:
        print(f"Rain: {weatherTokens[1]}")

    if includeWind:
        print(f"Wind: {weatherTokens[2]}")

if __name__ == "__main__":
    tokenList = sys.argv[1:]

    # Parse command-line arguments
    for i, token in enumerate(tokenList):
        if token == "-temp":
            includeTemperature = True
        elif token == "-rain":
            includeRain = True
        elif token == "-wind":
            includeWind = True

    location = tokenList[0]

    # Print banner
    printBanner()

    # Fetch and print weather data
    weatherData = fetchWeatherData()
    printWeatherData(weatherData)
