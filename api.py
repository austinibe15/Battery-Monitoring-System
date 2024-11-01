from flask import Flask, jsonify  
import random  

app = Flask(__name__)  

@app.route('/api/battery', methods=['GET'])  
def get_battery_data():  
    battery_data = {  
        'current': random.uniform(-100, 100),  # in Amperes  
        'voltage': random.uniform(10, 15),     # in Volts  
        'temperature': random.uniform(-20, 60), # in Celsius  
        'soc': random.uniform(0, 100)           # State of Charge in %  
    }  
    return jsonify(battery_data)  

if __name__ == '__main__':  
    app.run(debug=True)