# CodeBuddy 🤖

> A local AI coding practice assistant powered by open-source AI.

CodeBuddy is a beginner-friendly coding assistant built for learners who want help with programming questions, debugging, hints, and practice — while keeping their interactions local on their own computer.

It uses **Ollama** to run the open-source **Qwen2.5-Coder** model locally.

---

## ✨ Features

* 💡 **Ask a Coding Question** — Get simple explanations of programming concepts.
* 🐛 **Debug My Code** — Understand errors and find possible fixes.
* 🧩 **Give Me a Hint** — Get guidance without immediately seeing the full solution.
* 📝 **Practice Question** — Generate programming questions for practice.
* 🔒 **Local AI** — Questions and code are processed locally through Ollama.
* 🌐 **Simple Web Interface** — Clean and beginner-friendly UI.

---

## 🏗️ How It Works

```text
User
  ↓
CodeBuddy Web Interface
  ↓
Python Local Server
  ↓
Ollama
  ↓
Qwen2.5-Coder
  ↓
AI Response
  ↓
CodeBuddy Interface
```

The application uses:

* **HTML** for the interface
* **CSS** for styling
* **JavaScript** for interaction
* **Python** built-in HTTP server for the backend
* **Ollama** for local AI inference
* **Qwen2.5-Coder:3b** as the coding model

---

## 🛠️ Requirements

Before running CodeBuddy, install:

1. Python 3.13 or later
2. Ollama
3. Qwen2.5-Coder model

Pull the model using:

```bash
ollama pull qwen2.5-coder:3b
```

---

## 🚀 Running CodeBuddy

### 1. Start Ollama

Make sure Ollama is running on your computer.

You can test the model with:

```bash
ollama run qwen2.5-coder:3b
```

### 2. Start CodeBuddy

Open the CodeBuddy project folder and run:

```bash
python server.py
```

Or run `server.py` directly using Python IDLE.

### 3. Open the application

Open your browser and visit:

```text
http://localhost:8000
```

You can now use CodeBuddy locally.

---

## 📁 Project Structure

```text
CodeBuddy/
│
├── index.html      # Main web interface
├── style.css       # Application styling
├── server.py       # Python backend and Ollama connection
└── README.md       # Project documentation
```

---

## 🔐 Privacy

CodeBuddy is designed around local AI processing.

The application sends coding questions from the browser to the local Python server, which communicates with Ollama running on the same computer.

After the required software and model are downloaded, the AI interaction can work without sending the coding conversation to a remote AI API.

---

## 🌱 Why Open-Source AI?

CodeBuddy uses a locally running open-source/open-weight coding model instead of depending on a hosted AI API.

This makes it possible to:

* Run AI on a personal computer
* Keep coding questions and code local
* Experiment with different models
* Customize the application
* Learn how AI systems work
* Avoid per-request API costs

The model does need to be downloaded initially, so internet access is required during setup.

---

## 🎯 Built For

CodeBuddy was created for a friend who is learning programming and needs a simple way to:

* Understand difficult concepts
* Debug mistakes
* Get hints while solving problems
* Practice programming regularly

The goal is not to replace learning, but to make learning programming easier and more interactive.

---

## 🔮 Future Improvements

Possible future features include:

* Multiple programming language modes
* Code editor with syntax highlighting
* Conversation history
* Learning progress tracking
* Personalized practice difficulty
* More local AI models
* Voice-based coding assistance

---

## 📜 License

This project is open source and intended for learning, experimentation, and community contribution.
