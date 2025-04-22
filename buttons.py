from telebot import types


def number_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Отправить номер📞', request_contact=True)
    kb.add(but1)

    return kb


def location_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Отправить локацию📍', request_location=True)
    kb.add(but1)

    return kb


def main_menu(products):
    kb = types.InlineKeyboardMarkup(row_width=2)
    cart = types.InlineKeyboardButton(text='Корзина🛒', callback_data='cart')
    all_products = [types.InlineKeyboardButton(text=f'{i[1]}', callback_data=i[0]) for i in products]
    kb.add(*all_products)
    kb.row(cart)

    return kb


def choice_pr_buttons(pr_amount, plus_or_minus='', amount=1):
    kb = types.InlineKeyboardMarkup(row_width=3)
    minus = types.InlineKeyboardButton(text='-', callback_data='decrement')
    count = types.InlineKeyboardButton(text=str(amount), callback_data=str(amount))
    plus = types.InlineKeyboardButton(text='+', callback_data='increment')
    to_cart = types.InlineKeyboardButton(text='В корзину🛒', callback_data='to_cart')
    back = types.InlineKeyboardButton(text='Назад⬅', callback_data='back')
    if plus_or_minus == 'increment':
        if amount <= pr_amount:
            count = types.InlineKeyboardButton(text=str(amount + 1), callback_data=str(amount))
    elif plus_or_minus == 'decrement':
        if amount > 1:
            count = types.InlineKeyboardButton(text=str(amount - 1), callback_data=str(amount))
    kb.add(minus, count, plus)
    kb.row(back, to_cart)

    return kb


def cart_buttons():
    kb = types.InlineKeyboardMarkup(row_width=2)
    order = types.InlineKeyboardButton(text='Оформить заказ🧾', callback_data='order')
    back = types.InlineKeyboardButton(text='Назад⬅', callback_data='back')
    clear = types.InlineKeyboardButton(text='Очистить корзину🗑', callback_data='clear')
    kb.add(order, back)
    kb.row(clear)

    return kb


## Кнопки админ-панели ##
def admin_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Добавить продукт')
    but2 = types.KeyboardButton('Удалить продукт')
    but3 = types.KeyboardButton('Изменить продукт')
    but4 = types.KeyboardButton('Перейти в главное меню')
    kb.add(but1, but2, but3)
    kb.row(but4)

    return kb


def admin_pr(products):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    all_products = [types.KeyboardButton(f'{i[1]}') for i in products]
    kb.add(*all_products)
    kb.row(back)

    return kb


def change_buttons():
    kb = types.InlineKeyboardMarkup(row_width=2)
    name = types.InlineKeyboardButton(text='Название', callback_data='name')
    des = types.InlineKeyboardButton(text='Описание', callback_data='description')
    price = types.InlineKeyboardButton(text='Цена', callback_data='price')
    count = types.InlineKeyboardButton(text='Кол-во', callback_data='count')
    photo = types.InlineKeyboardButton(text='Фото', callback_data='photo')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back_admin')
    kb.add(name, des, price, count)
    kb.row(photo)
    kb.row(back)

    return kb


def confirm_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    kb.add(yes, no)

    return kb
