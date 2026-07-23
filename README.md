# AI Roadmap Generator 🗺️

An AI-powered web application that generates personalized learning roadmaps using the **Groq API** and **Flask**. Simply describe your learning goal, and get a structured, step-by-step roadmap to guide your journey.

## ✨ Features

- 🤖 AI-generated learning roadmaps powered by Groq's fast LLM inference
- 🎯 Personalized paths based on user goals, skill level, and time availability
- 🌐 Clean, responsive web interface (Flask + HTML templates)
- ⚡ Fast response times thanks to Groq's LPU inference engine
- 📋 Structured output (topics, milestones, resources, estimated timelines)

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **AI/LLM:** Groq API
- **Frontend:** HTML, CSS, JavaScript
- **Environment Management:** python-dotenv

## 📁 Project Structure

```
roadmap_AI/
├── templates/
│   └── index.html        # Main frontend page
├── .env                   # Environment variables (API keys) - not committed
├── .gitignore
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A [Groq API key](https://console.groq.com/keys)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/roadmap_AI.git
   cd roadmap_AI
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## 💡 Usage

1. Enter the topic or skill you want to learn (e.g., "Machine Learning", "Web Development", "DevOps")
2. Optionally specify your current level and available time
3. Click **Generate Roadmap**
4. Receive a structured, AI-generated learning path with milestones and resources

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your API key from Groq Console, used to authenticate requests to the Groq LLM API |

## 📦 Requirements

Example `requirements.txt`:
```
flask
groq
python-dotenv
```

## 🗺️ Roadmap (Future Improvements)

- [ ] Export roadmap as PDF
- [ ] Save/load user roadmaps
- [ ] Add progress tracking
- [ ] Support multiple LLM providers
- [ ] User authentication

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/roadmap_AI/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for the blazing-fast LLM inference API
- [Flask](https://flask.palletsprojects.com/) for the lightweight web framework