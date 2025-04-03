from flask import Flask, request, render_template
import os

app = Flask(__name__, template_folder=os.path.join('form', 'templates'))

@app.route("/")
def home():
    return render_template('question_form.html', message="Welcome to your Customer AI virtual assistant CAIVA")

@app.route('/resolve', methods=['POST'])
def question_form_post():
    text = request.form["input_question"]
    processed_text = text.upper()
    return render_template('feedback_form.html', solution=processed_text)

@app.route("/", methods=["POST"])
def ask():
    return render_template('question_form.html', message="Thank you for your feedback! Anything else to ask about?")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)