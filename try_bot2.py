from typing import Final
from telegram import  ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes,ConversationHandler



TOKEN: Final = '7432685124:AAGa6s5AylUmbIrgXxP-KPSQZwk1En5O-30'
BOT_USERNAME : Final = '@BabuSpare_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.username
    first_name = user.first_name
    keyboard = [
        [KeyboardButton("Option 1"), KeyboardButton("Option 2")],
        [KeyboardButton("Option 3"), KeyboardButton("Help")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text('Please choose an option:', reply_markup=reply_markup)
    await update.message.reply_text(f'Hello {first_name} (@{username})! I am a bot to help you with your spare parts needs. Please choose an option:', reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.username
    await update.message.reply_text(f' I am a bot, how can I help you today?')

async def post_item(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.first_name
    await update.message.reply_text(' what item do you want to post?')

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):#for inline query
    query = update.callback_query
    await query.answer()

    choice = query.data
    if choice == '1':
        await query.edit_message_text(text="You chose option 1")
    elif choice == '2':
        await query.edit_message_text(text="You chose option 2")
    elif choice == '3':
        await query.edit_message_text(text="You chose option 3")

async def start_Buttons(update :Update ,context : ContextTypes.DEFAULT_TYPE):
    user=update.effective_user
    username=user.username
    first_name=user.first_name
    keyboard=[ [KeyboardButton("update_profile"),KeyboardButton("my_posted_items"),KeyboardButton("upload new item")]]
    replay_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
    await update.message.reply_text('what do u want to do ', reply_markup=replay_markup)
    await update.message.reply_text(f'Hello {first_name} (@{username})! I am a bot to help you with your spare parts needs. Please choose an option:', reply_markup=replay_markup)


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello'
    elif 'how are you' in processed:
        return 'I am fine, thank you'
    else:
        return 'I do not understand you'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.username
    first_name = user.first_name
    last_name = user.last_name if user.last_name else ""

    messageType: str = update.message.chat.type  # to know whether it is a private chat or group chat
    text: str = update.message.text
    print(f'user({update.message.chat.id}) in {messageType}: "{text}" (username: {username}, name: {first_name} {last_name})')

    if messageType == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        if text[0]!="/":
            response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(f'{response}')

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')


# Define states
MENU, OPTION1, OPTION2 = 0,1,2


# Define the /start command handler
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("አዲስ እቃ ለመለጠፍ"),
          KeyboardButton("እስካሁን የልጠፍኩት እቃ ዝርዝር")],
        [KeyboardButton("Help")]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text('welcome to babu spare custmor requsit boot click your desire form the', reply_markup=reply_markup)
    return MENU

# Define the menu state handler
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "አዲስ እቃ ለመለጠፍ":
        await update.message.reply_text('You chose Option 1')
        return OPTION1
    elif text == "እስካሁን የልጠፍኩት እቃ ዝርዝር":
        await update.message.reply_text('You chose Option 2')
        return OPTION2
    elif text.lower() == "help":
        await help_command(update, context)
        return MENU
    else:
        await update.message.reply_text(f'Invalid option: {text}')
        return MENU

# Define handlers for Option 1 state
async def option1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You are now in Option 1 state. Send /back to return to menu.')
    return OPTION1

# Define handlers for Option 2 state
async def option2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You are now in Option 2 state. Send /back to return to menu.')
    return OPTION2

# Define a /help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is the help section. How can I assist you?')

# Define a handler to go back to the menu
async def go_back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await start_command(update, context)

#  a function to handle errors
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
app = Application.builder().token(TOKEN).build()

# Set up the ConversationHandler with the states MENU, OPTION1, and OPTION2
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start_command)],
    states={#hash map 
        MENU: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, menu)
        ],
        OPTION1: [
            CommandHandler('back', go_back),
            MessageHandler(filters.TEXT & ~filters.COMMAND, option1)
        ],
        OPTION2: [
            #we can add other options 
            CommandHandler('back', go_back),
            MessageHandler(filters.TEXT & ~filters.COMMAND, option2)
        ],
    },
    fallbacks=[CommandHandler('start', start_command)]
)

# Add the conversation handler to the application
app.add_handler(conv_handler)

# Add error handler
app.add_error_handler(error_handler)






if __name__ == '__main__':
    print("starting the bot")
    
    # Commands
    #app.add_handler(CommandHandler('start', start_command))
    #app.add_handler(CommandHandler('help', help_command))
    #app.add_handler(CommandHandler('post', post_item))

    # Button presses
    #app.add_handler(CallbackQueryHandler(button))


    # Messages
    #app.add_handler(MessageHandler( filters.TEXT and ~ filters.COMMAND, handle_message))

    # Errors
    #app.add_error_handler(error)

    # Polling
    print('polling...')
    app.run_polling(poll_interval=4)
