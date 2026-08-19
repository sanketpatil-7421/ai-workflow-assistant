# 🤖 Local Command AI Agent

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)](#features)

A lightweight, zero-dependency Python AI agent that runs 100% locally in your terminal. It executes commands like greetings, system time retrieval, and graceful exits without needing API keys, cloud services, or an internet connection.

---

## 📐 Architecture & Logic Flow

                  +----------------------+
                  |      User Input      |
                  +----------+-----------+
                             |
                             v
                  +----------------------+
                  | Normalize Text Input |
                  |  (.strip().lower())  |
                  +----------+-----------+
                             |
                             v
                  +----------------------+
                  |   Intent Evaluator   |
                  +---+------+--------+--+
                      |      |        |
      +---------------+      |        +---------------+
      | ("hello")            | ("date")               | ("bye")
      v                      v                        v
+-------------------+  +--------------------+  +--------------------+
|  Greeting Module  |  |  Datetime Module   |  |   Exit Pipeline    |
| Return String Msg |  | Query System Clock |  | Close Terminal Loop|
+---------+---------+  +---------+----------+  +---------+----------+
|                      |                        |
+-------------------+--+------------------------+
|
v
+----------------------+
|   Terminal Output    |
+----------------------+


---

## ⚡ Features

* **Zero External Dependencies:** Uses only built-in Python standard libraries (`datetime`).
* **100% Offline & Private:** No API keys, cloud calls, or internet connection required.
* **Instant Processing:** Deterministic rule-matching guarantees sub-millisecond execution.
* **Interactive CLI Loop:** Continuous REPL loop for seamless terminal interaction.

---

## 📋 Supported Commands

| Command Category | Input Triggers | Internal Action | Output Response |
| :--- | :--- | :--- | :--- |
| **Greeting** | `hello`, `hi` | Matches greeting keyword | `"Hello! How can I help you today?"` |
| **Date & Time** | `date`, `time` | Reads system time via `datetime` | `"Today's date is Wednesday, August 19, 2026..."` |
| **Exit** | `bye`, `exit` | Sets loop condition to terminate | `"Goodbye! Have a great day."` |

---

## 🚀 Quick Start

### Prerequisites
* Python 3.8 or higher installed on your system.

### Running the Agent

1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git)
   cd YOUR-REPOSITORY-NAME
Execute the Python script directly:

Bash
python main.py
🛠️ Code Overview
project-root/
│
├── main.py          # Core engine and command router
├── README.md        # Documentation and diagrams
└── LICENSE          # MIT License
Python
import datetime

def simple_agent(command: str) -> str:
    cmd = command.strip().lower()

    if "hello" in cmd or "hi" in cmd:
        return "Hello! How can I help you today?"
    elif "date" in cmd or "time" in cmd:
        now = datetime.datetime.now()
        return f"Today's date is {now.strftime('%A, %B %d, %Y')} and the current time is {now.strftime('%I:%M %p')}."
    elif "bye" in cmd or "exit" in cmd:
        return "Goodbye! Have a great day."
    else:
        return f"Unknown command: '{command}'. Try saying 'hello', 'date', or 'bye'."

if __name__ == "__main__":
    print("Agent started. Type 'hello', 'date', or 'bye' (or 'exit' to quit).")
    while True:
        user_input = input("\nYou: ")
        response = simple_agent(user_input)
        print(f"Agent: {response}")
        
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break
