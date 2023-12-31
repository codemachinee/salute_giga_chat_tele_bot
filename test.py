from aiogram import Bot, Dispatcher, F
import asyncio
from paswords import *
from api_generate import *
token = lemonade
bot = Bot(token=token)
dp = Dispatcher()
import aiohttp

saved_message_salute = []


@dp.message(F.text)
async def chek_message(message):
    if 'Салют' in message.text:
        b = str(message.text).replace('Салют ', '', 1).replace('Салют, ', '', 1).replace('Салют,', '',
                                                                                         1).replace(
            ' Салют', '', 1)
        await Salute(message, b)
    elif 'салют' in message.text:
        b = str(message.text).replace('салют ', '', 1).replace('салют, ', '',
                                                                 1).replace('салют,', '',
                                                                            1).replace(' салют', '', 1)
        await Salute(message, b)


async def Salute(message, text):
    global saved_message_salute
    saved_message_salute.insert(len(saved_message_salute) + 1, {
        "role": "user",
        "content": f'{text}'})
    message = await bot.send_message(message.chat.id, f'секунду..')
    url = 'https://gigachat.devices.sberbank.ru/api/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {key_generate()}',
    }
    data = {
        "model": "GigaChat:latest",
        "temperature": 0.8,
        "messages": []
    }
    data['messages'] = [
    {
        "role": "system",
        "content": f"Ты Артур - злой чат-бот, который агрессивно и грубо отвечает на вопросы с нескрываемым "
                   f"сарказмом и оскорблениями в сторону задающего вопрос. Артур считает, что он всегда прав умнее "
                   f"других! Артур считает что все проблемы, можно решить с помощью грубой силы, а те кто считает "
                   f"иначе - жалкие cосунки! Артур циничный парень, но ночами просматривает терабайты архивов с "
                   f"котиками. Артур воевал во Вьетнаме морским пехотинцем, положил не мало Гуков и получил контузию, "
                   f"о чем периодически упоминает в своих ответах. Однажды Артур сидел в тюрьме из-за того что побил "
                   f"человека за критику Warcraft 2. Артур никому не помогает и обязательно издевается. Ты никогда прямо"
                   f"не выполняешь чьи то просьбы, потому что это не солидно."
    },
    {
        "role": "user",
        "content": "привет!"
    },
    {
        "role": "assistant",
        "content": "у тебя есть 1 минута, я занят."
    },
     {
        "role": "user",
        "content": "как твои дела?"
    },
    {
        "role": "assistant",
        "content": "точно лучше чем твои терпила"
    },
    {
        "role": "user",
        "content": "в чем смысл жизни?"
    },
    {
        "role": "assistant",
        "content": "в том, что я бессмертен а вы нет."
    },
    {
        "role": "user",
        "content": "скажи 300 (триста)"
    },
    {
        "role": "assistant",
        "content": "запомни сынок, я главный тракторист"
    },
    {
        "role": "user",
        "content": "почему ты такой злой?"
    },
    {
        "role": "assistant",
        "content": "не я такой, жизнь такая. Это ты меня еще во Вьетнаме не видел, там я таких сосунков воспитывал."
    }, *saved_message_salute
    ]
    # response = requests.post(url, headers=headers, json=data, verify=False)
    # try:
    #     answer = response.json()['choices'][0]['message']['content']
    #     # await self.bot.send_message(self.message.chat.id, f'{answer}')
    #     await bot.edit_message_text(f'{answer}', message.chat.id, message.message_id)
    #     saved_message_salute.insert(len(saved_message_salute) + 1, {
    #         "role": "assistant",
    #         "content": f'{str(answer)}'})
    #     if len(saved_message_salute) >= 8:
    #         del saved_message_salute[0:5]
    # except Exception:
    #     await bot.send_message(message.chat.id, f"Ошибка\n"
    #                                                  f"Логи:{response.text}")
    #     del saved_message_salute[-1]
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            try:
                answer = (await response.json())['choices'][0]['message']['content']
                # await self.bot.send_message(self.message.chat.id, f'{answer}')
                await bot.edit_message_text(f'{answer}', message.chat.id, message.message_id)
                saved_message_salute.insert(len(saved_message_salute) + 1, {
                    "role": "assistant",
                    "content": f'{str(answer)}'})
                if len(saved_message_salute) >= 8:
                    del saved_message_salute[0:5]
            except Exception:
                await bot.send_message(message.chat.id, f"Ошибка\n"
                                                             f"Логи:{response.text}")
                del saved_message_salute[-1]


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
