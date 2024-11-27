import math

from dotenv import load_dotenv
import os

import requests



def height():
    print("Enter the medium of height")
    med = int(input("1. centimeter, 2. meter, 3. feet, 4. feet and inches:\t"))
    if med == 1:
        cm = float(input("Enter the height in centimeters\t"))
    elif med == 2:
        h = float(input("Enter the height in meters\t"))
        cm = h * 100
    elif med == 3:
        h = float(input("Enter the height in feet\t"))
        cm = h * 30.48
    elif med == 4:
        ft, inches = map(float, input("Enter the height in feet and inches\t").split())
        cm = (ft * 30.48) + (inches * 2.54)
    else:
        print("Invalid choice")
        return

    m = cm / 100
    total_ft = cm / 30.48
    ft = math.floor(total_ft)
    inches = (total_ft - ft) * 12

    if med != 1:
        print(f"Height in centimeters: {cm:.2f} cm")
    if med != 2:
        print(f"Height in meters: {m:.2f} m")
    if med != 3:
        print(f"Height in feet: {total_ft:.2f} ft")
    if med != 4:
        print(f"Height in feet and inches (ft' in''): {ft}' {inches:.1f}''")


def mass():
    print("Enter the medium of mass")
    med = int(input("1. grams, 2. kilograms, 3. pounds:\t"))
    if med == 1:
        g = float(input("Enter the mass in grams\t"))
    elif med == 2:
        kg = float(input("Enter the mass in kilograms\t"))
        g = kg * 1000
    elif med == 3:
        p = float(input("Enter the mass in pounds\t"))
        g = p * 453.59237
    else:
        print("Invalid choice")
        return

    kg = g / 1000
    p = g / 453.59237

    if med != 1:
        print(f"Mass in grams: {g} grams")
    if med != 2:
        print(f"Mass in kilograms: {kg:.2f} kg")
    if med != 3:
        print(f"Mass in pounds: {p:.2f} pounds")


def temperature():
    print("Enter the medium of temperature")
    med = int(input("1. Celcius, 2. Fahrenheit, 3. Kelvin:\t"))
    if med == 1:
        c = float(input("Enter the temperature in celsius\t"))
    elif med == 2:
        f = float(input("Enter the temperature in fahrenheit\t"))
        c = (f - 32) * 5 / 9
    elif med == 3:
        k = float(input("Enter the temperature in kelvin\t"))
        c = k - 273.15
    else:
        print("Invalid choice")
        return

    f = (c * 9 / 5) + 32
    k = c + 273.15

    if med != 1:
        print(f"Temperature in celsius: {c:.2f} °C")
    if med != 2:
        print(f"Temperature in fahrenheit: {f:.2f} °F")
    if med != 3:
        print(f"Temperature in Kelvin: {k:.2f} K")


def currency():
    api_key = os.getenv("api_key")
    if not api_key:
        print("API key is not found in environment variables")
        return

    src_cur = input("Enter the source currency code:\t")
    tar_cur = input("Enter the target currency code:\t")
    amount = float(input("Enter the currency amount:\t"))

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{src_cur}/{tar_cur}/{amount}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["result"] == "success":
            print(data["conversion_result"])
        else:
            raise ValueError("Failed to fetch conversion rate: " + data.get("error-type", "Unknown_error"))
    except requests.RequestException as e:
        raise RuntimeError(f"Error: {e}")
    



if __name__ == "__main__":

    load_dotenv()

    while True:
        print("\n\nUnit Converter")
        print("Enter your choice")
        choice = int(input("1. Height, 2. Mass, 3. Temperature, 4. Currency, 5. Exit\n"))
        match choice:
            case 1:
                height()
            case 2:
                mass()
            case 3:
                temperature()
            case 4:
                currency()
            case 5:
                exit()
            case _:
                print("Invalid choice")