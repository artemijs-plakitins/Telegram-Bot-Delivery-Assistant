from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)



workerMenuKeys = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = 'Deliver today')],
    [KeyboardButton(text = 'Already delivered')],
    [KeyboardButton(text = 'Work-Account')]],resize_keyboard=True,
      input_field_placeholder = 'Choose a button...')


cityKeys = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Rīga',callback_data='Riga')],
    [InlineKeyboardButton(text = 'Liepāja',callback_data='Liepaja')],
    [InlineKeyboardButton(text = 'Daugavpils',callback_data='Daugavpils')]])