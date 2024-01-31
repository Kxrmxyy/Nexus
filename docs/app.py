from flask import Flask, redirect, render_template, request
from datetime import datetime, timedelta
import secrets

app = Flask(__name__)

# Dictionary to store active keys and their expiration times
active_keys = {}

# Function to generate a new key
def generate_key():
    return secrets.token_urlsafe(16)

# Route for linkvertise redirection
@app.route('/linkvertise/<key>', methods=['GET'])
def linkvertise_redirect(key):
    if key in active_keys and datetime.now() < active_keys[key]:
        # If the key is valid and not expired, redirect to your app
        return redirect('https://myapp.vercel.app?key=' + key)
    else:
        # Key is invalid or expired, handle accordingly
        return render_template('invalid_key.html')

# Route for generating a new key
@app.route('/generate_key', methods=['GET'])
def generate_new_key():
    key = generate_key()
    active_keys[key] = datetime.now() + timedelta(days=1)
    return render_template('generate_key.html', key=key)

if __name__ == '__main__':
    app.run(debug=True)
