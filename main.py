import os
import random
import requests
from dotenv import load_dotenv
from telegram import Bot

folder_name = "xkcd_images"


def download_random_comic():
    count_url = "https://xkcd.com/info.0.json"
    response = requests.get(count_url)
    response.raise_for_status()
    latest_comic_number = response.json()['num']

    random_comic_number = random.randint(1, latest_comic_number)

    url = f"https://xkcd.com/{random_comic_number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comic_data = response.json()

    img_url = comic_data['img']
    comic_title = comic_data['title']
    comic_alt = comic_data['alt']

    img_response = requests.get(img_url)
    img_response.raise_for_status()
    img_name = os.path.join(folder_name, f"xkcd_{random_comic_number}.png")

    with open(img_name, 'wb') as img_file:
        img_file.write(img_response.content)

    return img_name, comic_title, comic_alt


def publish_comic(bot, chat_id, img_name, comic_title, comic_alt):
    bot.send_message(chat_id=chat_id, text=f"Comic: {comic_title}\n{comic_alt}")
    with open(img_name, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)


def remove_local_file(img_name):
    if img_name and os.path.exists(img_name):
        os.remove(img_name)


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["TOKEN_TELEGRAM"]
    chat_id = os.environ["CHAT_ID_TELEGRAM"]

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    try:
        img_name, comic_title, comic_alt = download_random_comic()
        print(f"Сохранен комикс: {img_name}")
        print(f"Название комикса: {comic_title}")

        bot = Bot(token)
        publish_comic(bot, chat_id, img_name, comic_title, comic_alt)

    except requests.exceptions.RequestException as e:
        print(f"Error during HTTP request: {e}")

    finally:
        remove_local_file(img_name)
