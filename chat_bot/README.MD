# AI Chatbot with MySQL

An interactive command-line AI Chatbot built in Python using Scikit-Learn. It provides automated responses to general knowledge and programming queries.

---

## Demo Screenshot

![AI Chatbot Output](images/Screenshot%20%28162%29.png)

---

## Features

* **Built-in Knowledge Base**: Answers questions about greetings, identity, programming concepts (Python, AI, Machine Learning, C, Java, HTML, CSS, JavaScript), jokes, and more.
* **Interactive Console Loop**: Real-time conversational interface in the terminal. Type `quit` to end the session.
* **MySQL Database History**: Automatically records every `user_message` and `bot_reply` into the `chat_history` table in MySQL.

---

## Prerequisites & Dependencies

Make sure Python 3.x is installed along with the required Python libraries:

```bash
pip install scikit-learn mysql-connector-python
```

---

## How to Run

1. Ensure MySQL is running on `localhost` with user `root` (or update database configuration in `chat_bot_py.py`).
2. Run the chatbot script:
   ```bash
   python chat_bot_py.py
   ```
3. Enter your queries when prompted `You: `. Enter `quit` to exit the application.
