# Отправка случайного комикса XKCD в Telegram

Этот скрипт отправляет случайный комикс XKCD в указанный Telegram-канал или чат. 
Программа получает случайный номер комикса из общего количества комиксов и загружает его, после чего отправляет изображение и заголовок комикса в Telegram.

## Установка зависимостей

Для успешного выполнения кода, необходимо установить следующие библиотеки:

1. `requests` - библиотека для выполнения HTTP-запросов к API XKCD и другим ресурсам.
2. `python-telegram-bot` - библиотека для работы с API Telegram, позволяющая взаимодействовать с ботами и отправлять сообщения.
3. `python-dotenv` - модуль для загрузки переменных окружения из файла `.env`.


### Настройка переменных окружения
Переменные окружения помогают скрыть конфиденциальную информацию, такую как токены доступа. В данном коде используется следующая переменная:
- `TOKEN_TELEGRAM` — токен доступа для работы с API Telegram.
Для получения переменной окружения из кода используется встроенный модуль `os`. Вот пример, как это выглядит:
```
TOKEN = os.getenv("TOKEN_TELEGRAM")
```
Зарегистрировать бота Telegram в мессенджере [Telegram](https://telegram.me/BotFather).
Сервисный токен выглядит примерно так:
```
958423683:AAEAtJ5Lde5YYfkjergber.
```
Также Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Пример запуска скрипта из командной строки. Этот код создает Telegram-бота, отправляет текстовое сообщение в указанный чат и прикрепляет к нему изображение.
```
python3 main.py 
```
## Описание работы

1. Скрипт устанавливает соединение с API XKCD и получает количество последних комиксов.
2. Генерируется случайный номер комикса, и его данные загружаются через API.
3. Изображение комикса сохраняется в локальную директорию, после чего это изображение отправляется в указанный Telegram-канал или чат.
4. После отправки изображение удаляется из локальной папки.

## Цель проекта

Код написан в образовательных целях и может быть использован как основной шаблон для создания других Telegram-ботов или перезаписи для работы с другими API.