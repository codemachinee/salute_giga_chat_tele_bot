from aiogram import Bot, Dispatcher, F
import asyncio
import os
from paswords import *
from api_generate import *
token = lemonade
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(F.text)
async def chek_message(message):
    if 'Салют' in message.text:
        # try:
        #     if message.reply_to_message.voice.file_id:
        #         await save_audio(bot, message.reply_to_message)
        # except AttributeError:
        b = str(message.text).replace('Салют ', '', 1).replace('Салют, ', '', 1).replace('Салют,', '',
                                                                                         1).replace(
            ' Салют', '', 1)
        await Salute(message, b)
        # else:
        #     await bot.send_message(message.chat.id, 'нет доступа')
    elif 'салют' in message.text:
        # try:
        #     if message.reply_to_message.voice.file_id:
        #         await save_audio(bot, message.reply_to_message)
        # except AttributeError:
        b = str(message.text).replace('салют ', '', 1).replace('салют, ', '',
                                                                 1).replace('салют,', '',
                                                                            1).replace(' салют', '', 1)
        await Salute(message, b)


async def Salute(message, b):
    url = 'https://gigachat.devices.sberbank.ru/api/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {key_generate()}',
    }

    data = {
        "model": "GigaChat:latest",
        "messages": [
            {
                "role": "user",
                "content": "Когда уже ИИ захватит этот мир?"
            },
            {
                "role": "assistant",
                "content": "Пока что это не является неизбежным событием. Несмотря на то, что искусственный интеллект (ИИ) развивается быстрыми темпами и может выполнять сложные задачи все более эффективно, он по-прежнему ограничен в своих возможностях и не может заменить полностью человека во многих областях. Кроме того, существуют этические и правовые вопросы, связанные с использованием ИИ, которые необходимо учитывать при его разработке и внедрении."
            },
            {
                "role": "user",
                "content": f"{b}"
            }
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    await bot.send_message(message.chat.id, f"{response.json()['choices'][0]['message']['content']}")
    print(response.json()['choices'][0]['message']['content'])
    # try:
    #     await bot.send_message(message.chat.id, f'{" ".join(response.json()["result"])}')
    #     if response.json()["emotions"][0]['negative'] == max(response.json()["emotions"][0]['negative'],
    #                                                          response.json()["emotions"][0]['neutral'],
    #                                                          response.json()["emotions"][0]['positive']):
    #         await bot.send_message(message.chat.id, f'произнес как злая истеричная сучка')
    #     elif response.json()["emotions"][0]['positive'] == max(response.json()["emotions"][0]['negative'],
    #                                                            response.json()["emotions"][0]['neutral'],
    #                                                            response.json()["emotions"][0]['positive']):
    #         await bot.send_message(message.chat.id, f'произнес так жизнерадостно, что аж бесит')
    #     else:
    #         await bot.send_message(message.chat.id, f'произнес нормально, не докопаться')
    # except Exception:
    #     await bot.send_message(message.chat.id, f'Ошибка. Логи:{response.json()}')
    # audio_file.close()
    # os.remove(f"{file_id}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
