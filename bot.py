import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from functions.learn import get_tech
from functions.project import get_project

load_dotenv()  

# docs: https://docs.python-telegram-bot.org/en/stable/

BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}.\nI am What To Do Today Bot.\nMy Creator create me to help him randomize some thing he want to do, such as daily learn material, project to do, etc.\n\nHere Some command you can use:\n/learn - Give random Tech Stack to learn\n/project - Generate some idea for your project\n')

async def learn_today(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None: 
    await update.message.reply_text(f'Try to learn this : {get_tech()}')

async def project(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None: 
    await update.message.reply_text(f'Try to build this: {get_project()}')

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("learn", learn_today))
    app.add_handler(CommandHandler("project", project))

    app.run_polling()

if __name__ == '__main__':
    main()
