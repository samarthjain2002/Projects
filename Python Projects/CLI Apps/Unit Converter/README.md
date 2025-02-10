# Unit Converter

This Python-based unit converter allows users to convert measurements between different units for height, mass, temperature, and currency exchange.

## Features
- Convert **Height** between centimeters, meters, feet, and feet-inches.
- Convert **Mass** between grams, kilograms, and pounds.
- Convert **Temperature** between Celsius, Fahrenheit, and Kelvin.
- Convert **Currency** using real-time exchange rates from an external API.

## Requirements
- Python 3.x
- `requests` library
- `python-dotenv` library
- A valid API key for exchange rates from [ExchangeRate-API](https://www.exchangerate-api.com/)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/unit-converter.git
   cd unit-converter
   ```
2. Install required dependencies:
   ```sh
   pip install requests python-dotenv
   ```
3. Create a `.env` file and add your API key:
   ```
   api_key=YOUR_EXCHANGE_RATE_API_KEY
   ```

## Usage
Run the script:
```sh
python unit_converter.py
```
Choose the type of conversion from the menu and enter the required values.

## Example Usage
```
Unit Converter
Enter your choice
1. Height, 2. Mass, 3. Temperature, 4. Currency, 5. Exit
> 1
Enter the medium of height
1. centimeter, 2. meter, 3. feet, 4. feet and inches:	3
Enter the height in feet	5
Height in centimeters: 152.40 cm
Height in meters: 1.52 m
Height in feet and inches (ft' in''): 5' 0.0''
```

## Future Enhancements
- Add more unit categories such as speed, volume, and time.
- Implement a graphical user interface (GUI).
- Support offline currency conversion with locally cached exchange rates.

## License
This project is open-source and available under the MIT License.

Happy Converting! 🚀

