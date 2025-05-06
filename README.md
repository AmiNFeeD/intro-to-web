# Chatroom (Flask + Socket.IO)

A minimal real‑time chat app built for the course project.

## Features
- Join / leave notifications
- Real‑time messaging via WebSockets
- Message history (last 50 messages) loaded on join
- Clear‑history button (dev‑only)
- SQLite persistence (`chat.db`)

## Tech stack
| Layer | Library |
|-------|---------|
| Backend | Flask 3.x, Flask‑SocketIO 5.x, Eventlet |
| Database | SQLite (`sqlite3` stdlib) |
| Front‑end | Vanilla JS, HTML, CSS |

## Setup

```bash
git clone --single-branch -b Chatroom https://github.com/AmiNFeeD/intro-to-web.git
cd chatroomych
python -m venv env && source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5001 in two browser windows
