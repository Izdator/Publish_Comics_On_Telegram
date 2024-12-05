import os
import random
import requests
from dotenv import load_dotenv
from telegram import Bot

folder_name = "xkcd_images"


def send_random_comic(token, chat_id):
    img_name = None

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

        print(f"Сохранен комикс: {img_name}")
        print(f"Название комикса: {comic_title}")

        bot = Bot(token)
        bot.send_message(chat_id=chat_id, text=f"Comic: {comic_title}\n{comic_alt}")

        with open(img_name, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)

    except requests.exceptions.RequestException as e:
        print(f"Error during HTTP request: {e}")

    finally:
        if img_name and os.path.exists(img_name):
            os.remove(img_name)


def main():
    load_dotenv()
    token = os.environ["TOKEN_TELEGRAM"]
    chat_id = os.environ["CHAT_ID_TELEGRAM"]
    send_random_comic(token, chat_id)


if __name__ == "__main__":
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    main()