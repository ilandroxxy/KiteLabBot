import telebot
from telebot import types
import datetime as dt

bot = telebot.TeleBot('1898710807:AAHzsje09qxhkB6jlfI3cjlT7QzSJHBFXhE')
# real 1898710807:AAHzsje09qxhkB6jlfI3cjlT7QzSJHBFXhE
# test 5543492408:AAFKGXowK8CV5Q4IFOGzDTCTR4OAaL_tU2I

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ` ⛔  ️✅ 📊📈🧮 💫  🏄‍♂️🏄🏄‍♀️

@bot.callback_query_handler(func=lambda call: True)
def step(call):

    # Каталог товаров -------------------------------------
    if call.data == 'f1':
        file1 = open('files/MainProductions.pdf', 'rb')
        bot.send_message(call.message.chat.id, '💫')
        bot.send_document(call.message.chat.id, file1)

    elif call.data == 'f2':
        file2 = open('files/Accessories.pdf', 'rb')
        bot.send_message(call.message.chat.id, '⚡️')
        bot.send_document(call.message.chat.id, file2)

    elif call.data == 'f3':
        file3 = open('files/Delivery.pdf', 'rb')
        bot.send_message(call.message.chat.id, '💥️')
        bot.send_document(call.message.chat.id, file3)

    elif call.data == 'f4':
        file4 = open('files/Guarantee.pdf', 'rb')
        bot.send_message(call.message.chat.id, '💫')
        bot.send_document(call.message.chat.id, file4)
    # Каталог товаров -------------------------------------




#START
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("Католог \nтоваров")
    btn2 = types.KeyboardButton('Получить контакты')
    btn3 = types.KeyboardButton('Социальные сети')
    btn4 = types.KeyboardButton('Посетите наш сайт')
    btn5 = types.KeyboardButton('Сделать заказ')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    sti_0 = open('photo/logo.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_0)
    send_mess = f"*Доброго времени, {message.from_user.first_name}*!\nРады видеть вас и хотим представить Telegram-бота 🤖 производства KiteLab 🏄‍️🏄🏄‍\nПриступим к общению!"
    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)

# CATALOG
@bot.message_handler(commands=['catalog'])
def catalog(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("1. Основная продукция.", callback_data="f1"),
               types.InlineKeyboardButton("2. Цены на оборудование.", callback_data="f2"),
               types.InlineKeyboardButton("3. Доставка.", callback_data="f3"),
               types.InlineKeyboardButton("4. Гарантии.", callback_data="f4"))

    message_text = "После нажатия кнопки дождитесь загрузки файлов!"
    bot.send_message(message.chat.id, message_text, parse_mode='Markdown', reply_markup=markup)

# HELP
@bot.message_handler(commands=['help'])
def help(message):
    message_text = "*You can control me by sending these commands:*\n\n*Commands public*\n/help - справка по всем командам в боте\n/start - перезапуск бота, на стартовую позицию\n" \
                    '/getmyid - бот покажет ваш id пользователя Telegram\n'
    bot.send_message(message.chat.id, message_text, parse_mode="Markdown")


# GETMYID
@bot.message_handler(commands=['getmyid'])
def getmyid(message):
    user = str(message.chat.id)
    message_text = "*Ваш user ID: *" + user
    bot.send_message(message.chat.id, message_text, parse_mode="Markdown")



@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == "Католог \nтоваров":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("1. Основная продукция.", callback_data="f1"),
                   types.InlineKeyboardButton("2. Цены на оборудование.", callback_data="f2"),
                   types.InlineKeyboardButton("3. Доставка.", callback_data="f3"),
                   types.InlineKeyboardButton("4. Гарантии.", callback_data="f4"))

        message_text = "После нажатия кнопки дождитесь загрузки файлов!"
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown', reply_markup=markup)



    elif get_message_bot == "Получить контакты":
        message_text = "*Наши контакты:*\n\n[FaceBook Messenger](m.me/kitelaboratory)\n\n[Telegram](t.me/PavelKolabin)\n\n[WhatsApp](wa.me/message/V6JOJV6KV6ZSO1)\n\n" \
                       "Написать на корпоративную почту: info@kitelab.pro\n\nПозвонить по номеру телефона:"
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_contact(message.chat.id, phone_number=79513821281, first_name='KiteLab', last_name='Оборудование для кайтбординга')


    elif get_message_bot == "Посетите наш сайт":
        pic_2 = open('photo/aloha.png', 'rb')
        bot.send_photo(message.chat.id, pic_2)
        message_text = "Посетите наш сайт [www.kitelab.pro](https://kitelab.pro/ru)"
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown', disable_web_page_preview=True)


    elif get_message_bot == "Социальные сети":
        markup = types.InlineKeyboardMarkup(row_width=3)
        markup.add(types.InlineKeyboardButton("Instagram", url="https://instagram.com/kitelaboratory?utm_medium=copy_link"),
                   types.InlineKeyboardButton("Facebook", url="https://www.facebook.com/kitelaboratory"))
        message_text = "Нажимайте на ссылки, чтобы перейти на страницу нашего производства в социальных сетях."
        bot.send_message(message.chat.id, message_text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif get_message_bot == "Сделать заказ":
        bot.send_message(message.chat.id, 'На этом моменте можно было реализовать отправку заказа тебе в чат (получается чат твоего бота, но на твой аккаунт) или в отдельную группу.'
                                          'Все заказы можно было бы промаркировать #хэштегами, чтобы было удобнее сортить по группе заказов.\n\n'
                                          'Можно добавить нормальный каталог товаров, просто уйдет время.\n\n'
                                          'Можно сделать минимальную статистику, чтобы через бота устраивать рассылки всем людям которые когда-то на него заходили и не заблокировали бота.')
    else:
        bot.send_message(message.chat.id, "🤖 Я пока не разговариваю, но быстро учась!")
bot.polling(none_stop=True)


