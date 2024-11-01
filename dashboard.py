from flask import Flask, render_template  
import mysql.connector  

app = Flask(__name__)  

# MySQL configuration  
MYSQL_HOST = 'localhost'  
MYSQL_USER = 'root'  # Your MySQL username  
MYSQL_PASSWORD = ''   # Your MySQL password  
MYSQL_DATABASE = 'battery_monitoring'  

def get_latest_battery_data():  
    conn = mysql.connector.connect(  
        host=MYSQL_HOST,  
        user=MYSQL_USER,  
        password=MYSQL_PASSWORD,  
        database=MYSQL_DATABASE  
    )  
    cursor = conn.cursor(dictionary=True)  
    cursor.execute("SELECT * FROM battery_data ORDER BY timestamp DESC LIMIT 1")  
    data = cursor.fetchone()  
    cursor.close()  
    conn.close()  
    return data  

@app.route('/')  
def index():  
    battery_data = get_latest_battery_data()  
    return render_template('dashboard.html', battery_data=battery_data)  # Passing battery data to the template  

if __name__ == '__main__':  
    app.run(debug=True)