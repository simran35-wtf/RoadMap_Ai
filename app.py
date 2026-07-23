# app.py
from flask import Flask, render_template, request, jsonify
import os
from groq import Groq
from datetime import datetime
from dotenv import load_dotenv
import logging
import traceback

# load .env
load_dotenv()

# logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# read API key correctly from environment
API_KEY = os.environ.get("GROQ_API_KEY")
if not API_KEY:
    logger.error("GROQ_API_KEY not set. Make sure .env exists and load_dotenv() runs from the project root.")
    raise ValueError("GROQ_API_KEY environment variable not set")

# initialize Groq client
try:
    client = Groq(api_key=API_KEY)
    logger.info("✅ Groq client initialized successfully")
except Exception as e:
    logger.exception("Failed to initialize Groq client")
    client = None

SUPPORTED_MODELS = [
    "llama-3.1-8b-instant",
    "llama-3.3-70b-versatile",
    "meta-llama/llama-guard-4-12b",
    "openai/gpt-oss-120b"
]

@app.route('/')
def home():
    return render_template('index.html')

# quick test endpoint to check connectivity & model availability
@app.route('/test_groq', methods=['GET'])
def test_groq():
    if not client:
        return jsonify({'ok': False, 'error': 'client not initialized'}), 500
    try:
        model = SUPPORTED_MODELS[0]
        logger.info("Testing Groq with model: %s", model)
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say 'OK' in one word."}
            ],
            temperature=0.0,
            max_tokens=8
        )
        text = resp.choices[0].message.content
        return jsonify({'ok': True, 'model': model, 'response': text})
    except Exception as e:
        logger.exception("Test request failed")
        return jsonify({'ok': False, 'error': str(e), 'traceback': traceback.format_exc()}), 500

@app.route('/generate_roadmap', methods=['POST'])
def generate_roadmap():
    if not client:
        return jsonify({'error': 'API client not initialized'}), 500

    interest = request.form.get('interest')
    if not interest:
        return jsonify({'error': 'Interest field is required'}), 400

    last_error = None
    last_trace = None

    for model in SUPPORTED_MODELS:
        try:
            logger.info("Trying model %s for interest='%s'", model, interest)
            chat_completion = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful career and learning advisor. Create a detailed "
                            "step-by-step roadmap for learning the given interest. Format it with "
                            "clear headings, bullet points, and estimated timelines. Make it practical and actionable."
                        )
                    },
                    {"role": "user", "content": f"Create a comprehensive learning roadmap for: {interest}"}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            roadmap = chat_completion.choices[0].message.content

            # save roadmap
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            os.makedirs("roadmaps", exist_ok=True)
            filename = f"roadmaps/roadmap_{timestamp}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"Roadmap for: {interest}\n\n")
                f.write(roadmap)

            logger.info("Model %s succeeded, saved to %s", model, filename)
            return jsonify({'roadmap': roadmap, 'filename': filename, 'model_used': model})

        except Exception as e:
            logger.exception("Model %s failed", model)
            last_error = str(e)
            last_trace = traceback.format_exc()
            # try next model
            continue

    # all models failed
    return jsonify({
        'error': 'All models failed',
        'details': last_error,
        'traceback': last_trace,
        'suggestion': 'Check your API key, model names, rate limits, or the Groq status/console'
    }), 500

if __name__ == '__main__':
    app.run(debug=True)