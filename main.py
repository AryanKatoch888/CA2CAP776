import csv
import hashlib
import bcrypt
import requests
import re
import time

LOGIN_ATTEMPTS_LIMIT = 5

def load_users_from_csv():
    users = {}
    try:
        with open('regno.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users[row['email']] = {
                    'hashed_password': row['hashed_password'],
                    'security_question': row['security_question'],
                    'security_answer': row['security_answer']
                }
    except FileNotFoundError:
        print("User data file not found.")
    return users

def save_user_to_csv(email, hashed_password, security_question, security_answer):
    with open('regno.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, hashed_password, security_question, security_answer])

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_password(password):
    return (len(password) >= 8 and re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

def sign_up_user(users):
    email = input("Enter your email: ")
    if email in users:
        print("Email already registered. Please login.")
        return False

    if not validate_email(email):
        print("Invalid email format.")
        return False

    password = input("Enter your password: ")
    while not validate_password(password):
        print("Password must be at least 8 characters long and contain one special character.")
        password = input("Enter your password: ")

    security_question = input("Enter a security question: ")
    security_answer = input("Enter the answer to your security question: ")

    hashed_password = hash_password(password)
    save_user_to_csv(email, hashed_password, security_question, security_answer)
    users[email] = {
        'hashed_password': hashed_password,
        'security_question': security_question,
        'security_answer': security_answer
    }
    print("Sign-up successful!")
    return True

def login_user(users):
    attempts = 0
    while attempts < LOGIN_ATTEMPTS_LIMIT:
        email = input("Enter your email: ")
        if email not in users:
            print("Email not found. Try again.")
            attempts += 1
            continue
        
        password = input("Enter your password: ")
        hashed_password = users[email]['hashed_password']
        
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            print("Login successful!")
            return email  
        else:
            print("Incorrect password. Try again.")
            attempts += 1
    
    print("Too many failed login attempts. Please try later.")
    return False

def reset_password(users):
    email = input("Enter your registered email for password reset: ")
    if email not in users:
        print("Email not found.")
        return

    security_question = users[email]['security_question']
    print(f"Security Question: {security_question}")
    security_answer = input("Answer: ")
    
    if security_answer == users[email]['security_answer']:
        new_password = input("Enter new password: ")
        while not validate_password(new_password):
            print("Password must be at least 8 characters long and contain one special character.")
            new_password = input("Enter new password: ")
        
        users[email]['hashed_password'] = hash_password(new_password)
        print("Password reset successfully!")
        return True
    else:
        print("Incorrect security answer.")
        return False
    

def get_city_coordinates(city, api_key):
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    response = requests.get(geocode_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['lat'], data[0]['lon']
        else:
            print("City not found.")
            return None
    else:
        print("Failed to fetch city coordinates.")
        return None

def beautify_air_quality(aqi, pollutants):
    print("\nAir Quality Index (AQI):", aqi)
    print("\nPollutants Levels (in µg/m³):")
    print(f"{'Pollutant':<10}{'Level':>10}")
    print("-" * 22)
    
    for pollutant, level in pollutants.items():
        print(f"{pollutant:<10}{level:>10.2f}")

def get_air_quality(city):
    api_key = "e4195c33699f1690a4e1d976e459c966"
    
    
    coordinates = get_city_coordinates(city, api_key)
    if coordinates:
        lat, lon = coordinates
        
        
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'list' in data and data['list']:
                aqi = data['list'][0]['main']['aqi']
                pollutants = data['list'][0]['components']
                beautify_air_quality(aqi, pollutants)
            else:
                print("No air quality data available.")
        else:
            print("Failed to fetch air quality data.")
    else:
        print("Could not get air quality data due to missing coordinates.")


def logged_in_menu():
    while True:
        print("\nLogged In - Select an option:")
        print("1. Check city weather")
        print("2. Log out")
        choice = input("Choose an option: ")

        if choice == '1':
            city_name = input("Enter city name: ")
            if(len(city_name) < 3):
                print("City name must be atleast 3 letters long")
                break
            get_air_quality(city_name)
        elif choice == '2':
            print("Logging out.")
            break
        else:
            print("Invalid option. Please try again.")

def main():
    users = load_users_from_csv()
    
    print("AIR QUALITY FOR CITY")
    
    while True:
        print("\n1. Login")
        print("2. Sign Up")
        print("3. Forgot Password")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            user_email = login_user(users)
            if user_email:
                logged_in_menu()
        elif choice == '2':
            sign_up_user(users)
        elif choice == '3':
            reset_password(users)
        elif choice == '4':
            print("Exiting application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()