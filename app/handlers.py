from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)


import app.keyboards as kb
import app.database.requests as rq


router = Router()


@router.message(CommandStart())
async def commandStart(message: Message) -> None:
    await message.answer(
        'Hi! Great to have you back at work! Before getting started,'
        ' please register your workday by sending /startworkday.')



@router.message(F.text == '/startworkday')
async def registerWorkDay(message: Message) -> None:
    await message.answer('Your workday has begun!', reply_markup=kb.workerMenuKeys)

@router.message(F.text == 'Deliver today')
async def openCityKeys(message: Message) -> None:
    await message.answer('Select a city', reply_markup=kb.cityKeys)



@router.callback_query(F.data.in_(rq.cityList))
async def showCityOrders(callback: CallbackQuery) -> None:

    city = callback.data
    await callback.answer(f'{city} selected')

    orders_info = await rq.get_order_by_city(city)

    if orders_info:
        orderSelectionKeyboard = InlineKeyboardMarkup(inline_keyboard=[])

        for order_id, address, paid_status in orders_info:
            orderSelectionKeyboard_button = InlineKeyboardButton (
                text = f"Order information --> ID: {order_id} | {address} | Paid: {paid_status}",
                callback_data = f"order_{order_id}"
            )
            orderSelectionKeyboard.inline_keyboard.append([orderSelectionKeyboard_button])
            await callback.message.edit_text(
                f"Select an order in {city}:", reply_markup = orderSelectionKeyboard)
    else:
        await callback.message.edit_text(f"No orders found for {city}.")