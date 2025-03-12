#pip install flask openai

from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI Client
client = OpenAI(api_key="sk-252bfaf9019141e18e453c7460160d8a", base_url="https://api.deepseek.com/v1")

def analyze_article(article_text, analysis_type):
    """Analyze article based on type"""
    prompts = {
        "5Ws": "Extract the 5Ws (Who, What, When, Where, Why) from the following article:",
        "how": "Explain how the events unfolded in the following article in a short single paragraph:",
    }
    
    prompt = f"{prompts[analysis_type]}\n\n{article_text}"
    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=messages
    )

    return response.choices[0].message.content

@app.route('/analyze_article', methods=['POST'])
def analyze():
    """API endpoint to analyze article"""
    data = request.json
    article_text = data.get("text")
    
    if not article_text:
        return jsonify({"error": "No text provided"}), 400

    # Get analysis results
    result = {
        "5Ws": analyze_article(article_text, "5Ws"),
        "how": analyze_article(article_text, "how")
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)















'''
from flask import Flask, request, jsonify
from openai import OpenAI



app = Flask(__name__)

# Initialize OpenAI Client
client = OpenAI(api_key="sk-252bfaf9019141e18e453c7460160d8a", base_url="https://api.deepseek.com/v1")

def analyze_article(article_text, analysis_type):
    """Analyze article based on type"""
    prompts = {
        "5Ws": "Extract the 5Ws (Who, What, When, Where, Why) from the following article:",
        "how": "Explain how the events unfolded in the following article in a short single paragraph:",
    }
    
    prompt = f"{prompts[analysis_type]}\n\n{article_text}"
    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=messages
    )

    return response.choices[0].message.content

@app.route('/analyze_article', methods=['POST'])
def analyze():
    """API endpoint to analyze article"""
    data = request.json
    article_text = data.get("text")
    
    if not article_text:
        return jsonify({"error": "No text provided"}), 400

    # Get analysis results
    result = {
        "5Ws": analyze_article(article_text, "5Ws"),
        "how": analyze_article(article_text, "how")
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
'''