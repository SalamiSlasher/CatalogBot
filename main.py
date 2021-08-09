import telebot
import config
import templates
import os

#os.chdir('catalog')

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def Welcome(message):
    bot.send_message(message.chat.id, config.start, reply_markup=templates.markup_main)

@bot.callback_query_handler(func=lambda call: call.data == 'contacts')
def Contacts(call):
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text=config.contacts, reply_markup=templates.markup_continue)

@bot.callback_query_handler(func=lambda call: call.data == 'continue')
def Continue(call):
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text=config.start, reply_markup=templates.markup_main)

@bot.callback_query_handler(func=lambda call: 'content' in call.data)
def ContentType(call):
    num = int(call.data.split('_')[1])
    text = templates.markup_map[num]
    markup = templates.markup_product[num]
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text=text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: 'product' in call.data)
def Product(call):
    product = templates.content[call.data.split('_')[1]]
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text=product.type + ' ' + product.name)
    try:
        bot.send_photo(call.message.chat.id, photo=product.img[0])
        bot.send_photo(call.message.chat.id, photo=product.img[1], reply_markup=templates.markup_continue2)
    except:
        print('wtf')

@bot.callback_query_handler(func=lambda call: call.data == 'continue2')
def Continue2(call):
    try:
        bot.delete_message(chat_id=call.message.chat.id,
                           message_id=call.message.message_id)
        bot.delete_message(chat_id=call.message.chat.id,
                           message_id=call.message.message_id - 1)
        bot.delete_message(chat_id=call.message.chat.id,
                           message_id=call.message.message_id - 2)
    except:
        pass
    Welcome(call.message)

@bot.callback_query_handler(func=lambda call: call.data == 'TEST')
def Test(call):



if __name__ == '__main__':
    bot.polling(none_stop=True)
