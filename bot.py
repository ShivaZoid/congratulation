import os
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())


async def send_greeting(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Нажми на меня")
    button2 = types.KeyboardButton("Немного о боте")
    markup.add(button1, button2)
    await message.answer(
        "Серега, привет (͡° ͜ʖ ͡°), этот телеграм бот o(≧o≦)o был создан, "
        "только что-бы поздравить тебя с Днем рождения ヽ(・∀・)ﾉ"
        "\n"
        "\n"
        "Вот перепетая песни Сереги пирата - как же он силён"
        "\n"
        "\n"
        "[Куплет]\n"
        "На тройке опять я, но Рубик на мид\n"
        "Титанчик хочет отомстить, но я забыл, кто ты\n"
        "Я будто палач, и мне никто не даст сдачи\n"
        "Я будто палач, и мне никто не даст сдачи\n"
        "Захожу в игру, на ФП беру\n"
        "Разора, потому что я на нём ебу\n"
        "Тиммейты снова плачут, «Разор не даст сдачи»\n"
        "Смотри, как я хуячу, ты ебаный неудачник\n\n"
        "[Припев]\n"
        "Как же ты силён, как же ты умён\n"
        "Им никогда не стать такими же\n"
        "Как же ты силён, как же ты умён\n"
        "Ты скоро станет лучшим в мире\n"
        "На-на, на-на, на-на, на-на, на (Лучшим)\n"
        "На-на, на-на, на-на, на-на, на\n"
        "На-на, на-на, на-на, на-на, на (Лучшим)\n"
        "На-на, на-на, на-на, на-на, на",
        reply_markup=markup,
    )


async def send_about_message(message: types.Message):
    await message.answer(
        "В виртуальном мире, в сети той дали,\n"
        "Телеграм бот жил, свою миссию знал.\n"
        "Он задачу одну исполнить должен был,\n"
        "Поздравить и исчезнуть, словно сон в ночи.\n\n"
        "Человека одного, радость принести,\n"
        "С днем рождения пожелать в этот миг.\n"
        "Словно звезда яркая, он загорелся вдруг,\n"
        "Счастье в сердце человека зажгло.\n"
        "Но время подошло, его роль сыграна,\n"
        "И бот молча исчез, как утренний туман.\n"
        "Словно ветер унес в небытие его,\n"
        "Остался лишь след в памяти, словно сказка с краю.\n"
        "Человек стоял, глядя в пустоту экрана,\n"
        "Грусть окутала душу, словно пелена.\n"
        "Но в сердце его жила память о миге,\n"
        "Когда бот принес счастье, словно ангел во сне.\n"
        "Так и жизнь текла, история прошла,\n"
        "Бот ушел, но оставил свой след навек.\n"
        "И человек иногда вспоминал о нем,\n"
        "О том, как бот принес радость в мир темный и тихий.",
    )


async def send_start_message(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Нажми на меня")
    button2 = types.KeyboardButton("Немного о боте")
    markup.add(button1, button2)
    await message.answer(
        "Выбери одну из кнопок:",
        reply_markup=markup,
    )


async def button_click_handler(message: types.Message):
    user_id = message.from_user.id

    if message.text == "Нажми на меня":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Нажми на меня")
        button2 = types.KeyboardButton("Немного о боте")
        markup.add(button1, button2)
        await message.answer(
            "Серега, когда ты запустил этого бота, я взломал твою телегу "
            "(｡◕‿‿◕｡) Гагагага. "
            f"Вот id твоей телеги - {user_id}",
            reply_markup=markup,
        )
    elif message.text == "Немного о боте":
        await send_about_message(message)


@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await send_greeting(message)


@dp.message_handler(text=["Нажми на меня", "Немного о боте"])
async def on_button_click(message: types.Message):
    await button_click_handler(message)


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
