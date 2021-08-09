import config
from telebot import types

class Product:
    def __init__(self, type_, name, delete, img=[config.kitten]):
        self.type = type_
        self.name = name
        self.img = img
        self.caption = ' '.join((type_, name))
        self.delete = delete + [0]


first = [
    Product("Электрокардиостимулятор", 'ApolloDR', [1, 2, 3],
            img=['https://docs.google.com/uc?id=1lhcSg5JCXsl533r2S3gk4kJcI0DnLkyV', 'https://docs.google.com/uc?id=14Nv-Vp_CrOE56c5auTcfiCHs1memhXJ4']),
    Product("Электрокардиостимулятор", 'ApolloSR', [1, 2, 3],
            img=['https://docs.google.com/uc?id=1Z96Yg7dy6SXLN_0XpsBLJ6ufQJmaAUN9', 'https://docs.google.com/uc?id=1nGbFKcZIskuX29R4unjdLM4vWTevlf6k']),
    Product("Электрокардиостимулятор", 'ApolloDC', [1, 2, 3],
            img=['https://docs.google.com/uc?id=1ko5vbd67hMzmLGgF7QViAodYe7gh53EH', 'https://docs.google.com/uc?id=1CIbkdGN_UNuamfUVdj-VPa0kKAutHjiK']),
    Product("Электрокардиостимулятор", 'ApolloSC', [1, 2, 3],
            img=['https://docs.google.com/uc?id=1BIRA3W7U8T7rqlTd_2tr-gIGkOfHRwLd', 'https://docs.google.com/uc?id=1q_nVSL_lAfCNCJ6nprv80uR3cK3JoSc1']),
    Product("Электрокардиостимулятор", 'ApolloCRT', [1, 2, 3],
            img=['https://docs.google.com/uc?id=1CFQ15z600lvgZKpz7W9qGB_XdGkGd4Gk', 'https://docs.google.com/uc?id=1g1hQy5lzYnoCyr30pDttRiP4URUqaVHz']),
]

second = [
    Product("Электрод", 'ApolloA', [-1, 1, 2],
            img=['https://docs.google.com/uc?id=1fQmhEnxF3wNLKTu5_6PR2IjsEzYmrw_v', 'https://docs.google.com/uc?id=1wuE1j7GApK1D9opjuvRZyYEM1nNKwbhX']),
    Product("Электрод", 'ApolloV', [-1, 1, 2],
            img=['https://docs.google.com/uc?id=11C59pJUL0ag5THnwVgP69K1I6QhaSy1u', 'https://docs.google.com/uc?id=1HH7veWJijOx2NxBI9117l2VrlZk2b6Ry']),
    Product("Электрод", 'ApolloAF', [-1, 1, 2],
            img=['https://docs.google.com/uc?id=1iig7MYIfKnFjG9GhKxtnSLCw7o9lBjbS', 'https://docs.google.com/uc?id=1fK61oOPpDMbvCjzOM9cnK-w9Zc7Yovxi']),
    Product("Электрод", 'Apollo', [-1, 1, 2],
            img=['https://docs.google.com/uc?id=1-Ox1WZPLWnQll3gMGjPTDh1p26S73weU', 'https://docs.google.com/uc?id=15aZGaH1S4mpG3eadZs09NA43nWZ-9-H1']),
]

third = [
    Product('Источник питания', 'BF4234K/BF4238K', [-1, -2, 1],
            img=['https://docs.google.com/uc?id=1PtYpTDYWyvmqqzUK2eq_rjYgSXEcgrEs', 'https://docs.google.com/uc?id=1xCzapIaWJKHc58sJeN2gJDjqIefGXbmM'])
]

content = dict()
for i in first:
    content[i.name] = i
for i in second:
    content[i.name] = i
for i in third:
    content[i.name] = i

markup_main = types.InlineKeyboardMarkup()
markup_main.add(
    types.InlineKeyboardButton(text='Электрокардиостимуляторы', callback_data='content_0'),
)
markup_main.add(
    types.InlineKeyboardButton(text='Электроды', callback_data='content_1'),
)
markup_main.add(
    types.InlineKeyboardButton(text='Источники питания', callback_data='content_2'),
)
markup_main.add(
    types.InlineKeyboardButton(text='Контакты', callback_data='contacts')
)
markup_main.add(
    types.InlineKeyboardButton(text='TEST', callback_data='TEST')
)

markup1 = types.InlineKeyboardMarkup()
markup1.add(
    types.InlineKeyboardButton(text='ApolloDR', callback_data='product_ApolloDR'),
    types.InlineKeyboardButton(text='ApolloSR', callback_data='product_ApolloSR'),
    types.InlineKeyboardButton(text='ApolloDC', callback_data='product_ApolloDC'),
)
markup1.add(
    types.InlineKeyboardButton(text='ApolloSC', callback_data='product_ApolloSC'),
    types.InlineKeyboardButton(text='ApolloCRT', callback_data='product_ApolloCRT'),
)
markup1.add(types.InlineKeyboardButton(text='Назад', callback_data='continue'))

markup2 = types.InlineKeyboardMarkup(row_width=4)
markup2.add(
    types.InlineKeyboardButton(text='ApolloA', callback_data='product_ApolloA'),
    types.InlineKeyboardButton(text='ApolloV', callback_data='product_ApolloV'),
    types.InlineKeyboardButton(text='ApolloAF', callback_data='product_ApolloAF'),
    types.InlineKeyboardButton(text='Apollo', callback_data='product_Apollo'),
)
markup2.add(types.InlineKeyboardButton(text='Назад', callback_data='continue'))

markup3 = types.InlineKeyboardMarkup()
markup3.add(
    types.InlineKeyboardButton(text='BF4234K/BF4238K', callback_data='product_BF4234K/BF4238K'),
)
markup3.add(types.InlineKeyboardButton(text='Назад', callback_data='continue'))

markup_product = [markup1, markup2, markup3]

#  mne stydno za etu glinu. Eto vremenno tak xd

markup_product = [markup1, markup2, markup3]
markup_map = {
    0: 'Электрокардиостимуляторы',
    1: 'Электроды',
    2: 'Источники питания',
}

markup_continue = types.InlineKeyboardMarkup()
markup_continue.add(types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='continue'))

markup_continue2 = types.InlineKeyboardMarkup()
markup_continue2.add(types.InlineKeyboardButton(text='Продолжить', callback_data='continue2'))


if __name__ == '__main__':
    for i in first:
        print('i:', i)

    for i in content:
        print('content:', i)
