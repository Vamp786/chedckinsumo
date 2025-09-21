from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        flash('Please fill all the fields.', 'error')
        return redirect(url_for('home'))

    # Here you can add logic to save the message or send email
    print(f"New message from {name} ({email}): {message}")

    flash(f'Thank you, {name}! Your message has been received.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)