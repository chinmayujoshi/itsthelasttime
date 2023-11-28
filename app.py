import os
from flask import Flask, render_template, jsonify,session, request, url_for, flash, redirect
from database import * 
from datetime import datetime
import pytz

app = Flask(__name__)
app.secret_key=os.urandom(24)

# Custom error handler for 405 (Method Not Allowed) error
@app.errorhandler(405)
def method_not_allowed_error(e):
    return render_template('error.html', error_code=405), 405

# Custom error handler for 404 (Not Found) error
@app.errorhandler(404)
def not_found_error(e):
    return render_template('error.html', error_code=404), 404

# Custom error handler for 500 (Server error) error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error_code=500), 500

@app.route("/")
def index_page():
    return render_template('index.html', current_page='index')

@app.route("/validate")
def validate_page():
    return render_template('validate.html', current_page='validate')
@app.route("/validate/true")
def post_validate_page_success():
    return render_template('validate_success.html', current_page='validate_success')

@app.route("/validate/true", methods=['post'])
def actual_page():
    username=request.form['name']
    if(username=="shreya"):
        return render_template('actual.html', current_page='actual_page')
    else:
        return render_template('index.html', current_page='index')
    
@app.route("/validate/score", methods=['POST'])
def save_score():
    data = request.get_json()

    # Extract timestamp and score from the JSON data
    timestamp_str = data.get('timestamp')
    score_value = data.get('score')

    # Convert timestamp to the correct format
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Set timezone to Indian Standard Time (IST)
    ist_timezone = pytz.timezone('Asia/Kolkata')
    timestamp = ist_timezone.localize(timestamp)

    addScore(timestamp, score_value)

    return jsonify({'message': 'Score added successfully'})

@app.route('/handle_button_click/sad', methods=['GET', 'POST'])
def sad_page():
    method = request.args.get('_method', 'GET')

    if method == 'POST':
        return render_template('sad.html', current_page='sad_page')
    else:
        return render_template('sad.html', current_page='sad_page')

@app.route('/handle_button_click/date', methods=['GET', 'POST'])
def date_page():
    method = request.args.get('_method', 'GET')

    if method == 'POST':
        return render_template('date.html', current_page='date_page')
    else:
        return render_template('date.html', current_page='date_page')

@app.route('/handle_button_click', methods=['POST'])
def handle_button_click():
    # data = request.get_json()
    # selected_value = data.get('value')
    selected_value=request.form['btn']
    # print("Selected Value:", selected_value)

    if selected_value == "yes":
        return redirect(url_for('date_page', _method='POST'))
    else:
        return redirect(url_for('sad_page', _method='POST'))
    
@app.route('/date/clicked', methods=['POST'])
def date_button_click():
    # data = request.get_json()
    # selected_value = data.get('value')
    selected_value=request.form['date']
    its_a_date(selected_value)
    return redirect(url_for('thanks_page'))

@app.route('/date/thanks')
def thanks_page():
    return render_template('thanks.html', current_page='date_page')

# api routes


if __name__ == '__main__':
    # app.run(host='192.168.0.107', port=5000, debug=True)
    # app.run(host='localhost',debug=True)
    app.run(host='192.168.1.2', port=5000, debug=True)
