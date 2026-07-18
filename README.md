# Gemini AI Chatbot

A terminal-based AI chatbot built using Python and Google's Gemini API.

## Features

- Interactive chatbot
- Conversation history
- Secure API key management using .env
- Uses Gemini 2.5 Flash

## Tech Stack

- Python
- Google Gemini API
- google-genai
- python-dotenv

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/gemini-chatbot.git
```

### Navigate into the project

```bash
cd gemini-chatbot
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

Windows:

```bash
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a .env file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run

```bash
python app.py
```