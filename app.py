from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample customer data
customers = [
    {"id": 1, "name": "John Doe", "subscription": "Premium", "billing": 50},
    {"id": 2, "name": "Jane Smith", "subscription": "Basic", "billing": 20}
]

@app.route('/customers', methods=['GET'])
def get_customers_json():
    return jsonify(customers)

@app.route('/notify', methods=['GET'])
def show_notifications():
    return render_template("notifications.html", customers=customers)

@app.route('/customers', methods=['POST'])
def add_customer():
    new_customer = request.json
    customers.append(new_customer)
    return jsonify({"message": "Customer added successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)