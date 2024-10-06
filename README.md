
# Air Quality Monitoring Application

This project is an **Air Quality Monitoring Application** built using Python. The app allows users to register, log in, recover passwords, and fetch real-time air quality data for a given city. It uses the **OpenWeather API** to gather information about air quality and pollutants like carbon monoxide (CO), nitrogen dioxide (NO₂), ozone (O₃), and particulate matter (PM2.5, PM10), among others.

## Features

- **User Authentication**: Users can register with email, hashed passwords, and security questions for password recovery.
- **Secure Login**: Users log in with a limit of 5 login attempts.
- **Password Recovery**: Users can recover forgotten passwords by answering security questions.
- **Real-Time Air Quality Data**: Fetches and displays real-time air quality and pollutant data for any city using coordinates from the OpenWeather API.
- **Data Beautification**: Pollutant data is presented in a clean and readable format.

## Technology Stack

- **Python**: The main programming language used for this application.
- **bcrypt**: For password hashing and validation.
- **re**: For validating email and password formats.
- **CSV**: To store user registration data.
- **requests**: For API calls to fetch air quality and geolocation data.
- **OpenWeather API**: Used to get the city's air quality data.
- **PrettyTable**: Optional (for beautifying the display of pollutant data).

## Prerequisites

Before running the project, ensure that you have the following:

- Python 3.x installed.
- The following Python libraries installed:
  - bcrypt
  - requests
  - PrettyTable (optional, for a tabular display of pollutant data)

To install these libraries, run:
```bash
pip install bcrypt requests prettytable
```

## API Key

To fetch real-time air quality data, you will need to sign up on [OpenWeather](https://home.openweathermap.org/users/sign_up) and get an API key.

Once you have the API key, you can use it in the code to get city coordinates and air quality data.

## Setup and Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/air-quality-monitoring-app.git
   cd air-quality-monitoring-app
   ```
   
2. Run the application:
   ```bash
   python Project1.py
   ```

## Application Flow

1. **Register**: 
   - Enter a valid email and password.
   - Answer a security question that will be used for password recovery.
   
2. **Login**: 
   - Enter your registered email and password.
   - After 5 failed login attempts, you will be locked out temporarily.

3. **Forgot Password**: 
   - If you forget your password, you can reset it by answering the security question.

4. **Air Quality Data**:
   - After successful login, enter the name of the city to get real-time air quality and pollutant levels.
   - Data is fetched using the OpenWeather API and displayed in a user-friendly format.

## Example Output

Here’s a sample of the air quality data the app will provide:

```
Air Quality Index (AQI): 4

Pollutants Levels (in µg/m³):
Pollutant      Level
----------------------
co           1108.17
no              0.00
no2            26.39
o3             59.37
so2             8.58
pm2_5          59.22
pm10           76.92
nh3            30.15
```

## Future Improvements

- Add a frontend for a more user-friendly interface.
- Integrate more environmental data (e.g., weather, pollen count).
- Implement a user session feature for better login management.
- Use a database (e.g., SQLite, MySQL) instead of CSV for more scalable data storage.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

