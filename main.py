import requests
import os
import random
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN_TELEGRAM")
CHAT_ID = os.getenv("CHAT_ID_TELEGRAM")

folder_name = "xkcd_images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


def send_random_comic():
    try:
        count_url = "https://xkcd.com/info.0.json"
        response = requests.get(count_url)
        response.raise_for_status()
        latest_comic_number = response.json()['num']

        random_comic_number = random.randint(1, latest_comic_number)

        url = f"https://xkcd.com/{random_comic_number}/info.0.json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        img_url = data['img']
        comic_title = data['title']
        comic_alt = data['alt']

        img_response = requests.get(img_url)
        img_response.raise_for_status()
        img_name = os.path.join(folder_name, f"xkcd_{random_comic_number}.png")

        with open(img_name, 'wb') as img_file:
            img_file.write(img_response.content)

        print(f"Картинка сохранена в {img_name}")
        print(f"Название комикса: {comic_title}")

        bot = Bot(TOKEN)

        bot.send_message(chat_id=CHAT_ID, text=f"Комикс: {comic_title}\n{comic_alt}")

        with open(img_name, 'rb') as file:
            bot.send_document(chat_id=CHAT_ID, document=file)

        os.remove(img_name)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении HTTP-запроса: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    send_random_comic()
