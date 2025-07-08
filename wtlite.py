import requests, sys

# Ansi escape codes for colors
colorYellow = "\x1b[33m"
colorBlue = "\x1b[34m"
colorWhite = "\x1b[37m"
colorReset = "\x1b[0m"

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
        print(f"{colorYellow}[*]{colorReset} Temperature: {colorYellow + weatherTokens[0] + colorReset}")

    # Printing rain
    if includeRain:
        print(f"{colorBlue}[\\]{colorReset} Rain: {colorBlue + weatherTokens[1] + colorReset}")

    if includeWind:
        print(f"{colorWhite}[~]{colorReset} Wind: {colorWhite + weatherTokens[2] + colorReset}")

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
