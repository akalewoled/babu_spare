from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler , filters, ContextTypes
TOKEN: Final = '7432685124:AAGa6s5AylUmbIrgXxP-KPSQZwk1En5O-30'
BOT_USERNAME : Final = '@BabuSpare_bot'


async def start_command(update :Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am a bot to help you with your spare parts needs. How can I help you today?')

async def help(update :Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I  am abot how can i help you today?')


async def post_item(update :Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('what item do you want to post?')
  

#Hnadle responses
def handle_response(text :str) -> str:
        
        processed : str = text.lower()

        if text in  processed:
            return 'Hello'
        elif text in  processed:
            return 'I am fine, thank you'
        else:
            return 'I do not understand you'
        
async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    messageType: str = update.message.chat.type #to know weather it is on private chat or group chat

    text : str = update.message.text
    print(f'user({update.message.chat.id}) in {messageType}: "{text}"')

    if messageType =='group':
        if BOT_USERNAME in text:
            new_text : str = text.replace(BOT_USERNAME, '').strip()
            response : str = handle_response(new_text)
        else:
            return
    else:
        response :str = handle_response(text)
    print('Bot' , response)
    await update.message.reply_text(response)

async def error(update :Update,context :ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')

if __name__== '__main__':
    print("startig the bot")
    app =Application.builder().token(TOKEN).build()
    

    #commands

    app.add_error_handler(CommandHandler('start' ,start_command))
    app.add_handler(CommandHandler('help',help))
    app.add_handler(CommandHandler('post',post_item))


    #messages 
    app.add_handler(MessageHandler(filters.TEXT ,handle_message))
         
    #errors
    app.add_error_handler(error)

    #polls ("the frequency of the time we need to refresh the data")
    print('polling...')
    app.run_polling(poll_interval=4)

