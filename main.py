import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from Auth_data import group_token
from photo_data import photo
from keyboard import *

if __name__ != '__main__':
    exit(0)

vk_session = vk_api.VkApi(token=group_token)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

        if event.from_user:
            usr = vk_session.method('users.get', {'user_ids': event.user_id})[0]
            print(r'https://www.vk.com/id{}'.format(usr['id']))
            print(usr['first_name'], usr['last_name'])
            print(event.text)
            print()

        if event.from_user and (event.text == 'Привет' or event.text == 'Прив' or event.text == 'start' or event.text == 'Начать'):
            vk.messages.send(
                user_id=event.user_id,
                message='Привет!',
                random_id=event.random_id,
                keyboard=KEYBOARD_MAIN
            )

        elif event.from_user and event.text == '1 картинка':
            vk.messages.send(
                user_id=event.user_id,
                attachment='photo{}_{}'.format(*photo()),
                random_id=event.random_id
            )
        elif event.from_user and event.text == '2 картинки':
            vk.messages.send(
                user_id=event.user_id,
                attachment=['photo{}_{}'.format(*photo()), 'photo{}_{}'.format(*photo())],
                random_id=event.random_id
            )
        elif event.from_user and event.text == 'Фоточки':
            vk.messages.send(
                user_id=event.user_id,
                message='Выбери количество',
                keyboard=KEYBOARD_PHOTOS,
                random_id=event.random_id
            )
        elif event.from_user and event.text == 'Назад':
            vk.messages.send(
                user_id=event.user_id,
                message='Главное меню',
                keyboard=KEYBOARD_MAIN,
                random_id=event.random_id
            )
        elif event.from_user and event.text == 'Помощь':
            vk.messages.send(
                user_id=event.user_id,
                message='Тебе могут помочь [id0|Алёна] или [id0|Денис]',
                random_id=event.random_id
            )