import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure Google Generative AI
genai.configure(api_key=os.environ["API_KEY"])

# Define the route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate AI content
@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form.get('user_input')  # Get the user input from the frontend
    
    if user_input:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        return jsonify({"generated_text": response.text})  # Return the generated content
    
    return jsonify({"error": "No input provided"}), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
