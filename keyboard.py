import json


# KEYBOARD_STEP_1 = {
#     'one_time': False,
#     'buttons': [[{
#         'action': {
#             'type': 'text',
#             'payload': json.dumps({'buttons': '1'}),
#             'label': 'Предыдущая',
#         },
#         'color': 'negative'
#     },
#     {
#         'action': {
#             'type': 'text',
#             'payload': json.dumps({'buttons': '2'}),
#             'label': 'Pred',
#         },
#         'color': 'primary'
#     }
#     ]]
# }

KEYBOARD_PHOTOS = str(json.dumps({
    "one_time": False,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "label": "1 картинка"
                },
                "color": "positive"
            },

            {
                "action": {
                    "type": "text",
                    "label": "2 картинки"
                },
                "color": "positive"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "negative"
            }
        ]
    ]
}, ensure_ascii=False))

KEYBOARD_MAIN = str(json.dumps({
    "one_time": False,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "label": "Фоточки"
                },
                "color": "positive"
            },
            {
                "action": {
                    "type": "text",
                    "label": "Помощь"
                },
                "color": "negative"
            }
        ]
    ]
}, ensure_ascii=False))
