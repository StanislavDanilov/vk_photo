import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
vk_session = vk_api.VkApi(token='c05dfc0e6bc4911809c7d06f5d497a4bfb587e64839f3aaf36c532c121e682b86cf41332e6f5aedc4aa7f')
attachments = []
upload = VkUpload(vk_session)
image_url = 'https://sun9-56.userapi.com/c845521/v845521422/18b9e3/8gKawjyKY_s.jpg'
image = session.get(image_url, stream=True)
photo = upload.photo_messages(photos=image.raw)[0]
attachments.append(
    'photo{}_{}'.format(photo['owner_id'], photo['id'])
)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    attachment=','.join(attachments),
                    message='Ваш текст'
                )
            elif event.from_chat:
                vk.messages.send(
                    chat_id=event.chat_id,
                    message='Ваш текст')

