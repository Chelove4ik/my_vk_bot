import vk_api
from Auth_data import servise_key, owner_id, album_id
from random import choice

vk_session = vk_api.VkApi(token=servise_key)


def photo():
    ses_own_id = choice(owner_id)
    ses_alb_id = album_id[ses_own_id]
    pho = vk_session.method('photos.get', {'owner_id': ses_own_id, 'album_id': ses_alb_id, 'count': 1000})
    lst = []

    try:
        for i in range(pho['count']):
            lst.append(pho['items'][i]['id'])
    except Exception:
        pass

    return [ses_own_id, choice(lst)]
