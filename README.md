## About Telegram-Bot-Delivery-Assistant
- This project is made for the purpose of learning how to develop telegram bots. For communication with Telegram API, I use **aiogram3** module.


## How to Obtain a Telegram Bot Token

1. Open Telegram and search for **"BotFather"**.
2. Start a chat with BotFather and send the command **/newbot** to create a new bot.
3. Follow the prompts to name your bot and choose a **unique username**.
4. Once created, BotFather will provide you with a **token** — this token is required for authentication and interaction with the **Telegram API.**

## Requirements and .env

- I recommend creating a **.venv** virtual environment before running the bot to avoid problems with **module versions**. <br>
- Open terminal and create virtual environment : <br>
Linux / macOS : ```python3 -m venv .venv```<br>
Windows : ```python -m venv .venv```<br>
- Virtual environment activation : <br>
Linux / macOS : ```source .venv/bin/activate```<br>
Windows : ```.venv\Scripts\activate``` <br>
- Virtual environment deactivation : <br>
Linux / macOS / Windows : ```deactivate```<br>

Requirements :
1. python 3.x
2. dotenv
3. aiogram
4. sqlalchemy
5. aiosqlite

## Database

- This project uses a **SQLite** database. When you start the bot, the database will be **automatically** created and filled with the necessary data. When data is inserted into the database, a notification saying **"The data has been successfully added!"** will appear in your terminal. If you restart the bot, the database will not be created again since it already exists within the project.<br>

## How to run

1. Create file **.env**<br>
2. Add const variables __TOKEN__ and **DB_URL**<br>
```TOKEN=...your token...```<br>
```DB_URL=...your DB URL...```<br>
3. Open terminal and run :<br>
Linux / macOS : ```python3 main.py```<br>
Windows : ```python main.py```