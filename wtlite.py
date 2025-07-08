import requests, sys

# ANSI escape codes
colorYellow = "\x1b[33m"
colorBlue = "\x1b[34m"
colorWhite = "\x1b[37m"
colorReset = "\x1b[0m"

# Global flags
includeTemperature = False
includeRain = False
includeWind = False
location = "London"

def printBanner():
    print(""" _      ____  __   _ __
| | /| / / /_/ /  (_) /____
| |/ |/ / __/ /__/ / __/ -_)
|__/|__/\__/____/_/\__/\__/ """)
    return

def fetchWeatherData():
    url = f"https://wttr.in/{location}?format="
    if includeTemperature: url += "%t "
    if includeRain:        url += "%p "
    if includeWind:        url += "%w "

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        sys.exit(1)

def printWeatherData(weatherData):
    tokens = weatherData.text.strip().split(" ")
    i = 0

    if includeTemperature:
        print(f"{colorYellow}[*]{colorReset} Temperature: {colorYellow}{tokens[i]}{colorReset}")
        i += 1

    if includeRain:
        print(f"{colorBlue}[\\]{colorReset} Rain: {colorBlue}{tokens[i]}{colorReset}")
        i += 1

    if includeWind:
        print(f"{colorWhite}[~]{colorReset} Wind: {colorWhite}{tokens[i]}{colorReset}")

if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        print("Usage: python wtlite.py <location> [-temp] [-rain] [-wind]")
        sys.exit(1)

    # First non-flag argument is location
    for arg in args:
        if not arg.startswith("-"):
            location = arg
            break

    # Flags
    for arg in args:
        if arg == "-temp":
            includeTemperature = True
        elif arg == "-rain":
            includeRain = True
        elif arg == "-wind":
            includeWind = True

    printBanner()
    data = fetchWeatherData()
    printWeatherData(data)
