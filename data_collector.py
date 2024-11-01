import requests  
import mysql.connector  
from mysql.connector import Error  
import time  

# MySQL configuration  
MYSQL_HOST = 'localhost'  
MYSQL_USER = 'root' # Replace with your MySQL username  
MYSQL_PASSWORD = ''  # Replace with your MySQL password  
MYSQL_DATABASE = 'battery_monitoring'  

def fetch_battery_data(api_url):  
    """Fetch battery data from the API."""  
    try:  
        response = requests.get(api_url)  
        response.raise_for_status()  # Raise an error for bad responses  
        return response.json()  
    except requests.exceptions.RequestException as e:  
        print(f"Error fetching data from API: {e}")  
        return None  # Return None if there's an error  

def store_battery_data(data):  
    """Store battery data in the MySQL database."""  
    try:  
        conn = mysql.connector.connect(  
            host=MYSQL_HOST,  
            user=MYSQL_USER,  
            password=MYSQL_PASSWORD,  
            database=MYSQL_DATABASE  
        )  
        cursor = conn.cursor()  
        cursor.execute("INSERT INTO battery_data (current, voltage, temperature, soc) VALUES (%s, %s, %s, %s)",  
                       (data['current'], data['voltage'], data['temperature'], data['soc']))  
        conn.commit()  
        print("Data stored successfully.")  
    except Error as e:  
        print(f"Error storing data: {e}")  
    finally:  
        if cursor:  
            cursor.close()  
        if conn:  
            conn.close()  

def main():  
    api_url = 'http://127.0.0.1:5000/api/battery'  # URL of your local API  

    while True:  
        battery_data = fetch_battery_data(api_url)  
        if battery_data:  # Proceed only if data is fetched successfully  
            print(f"Current SOC: {battery_data['soc']}%")  
            store_battery_data(battery_data)  
        time.sleep(2)  # Fetch data every 2 seconds  

if __name__ == '__main__':  
    main()