import mercadopago
import json

CLIENT_ID = '5074169278395239'
CLIENT_SECRET = 'Ge2VK7bhwoHJzXoCibKsLjhtAL4N5zdn'


def payment(req, **kwargs):

    name = kwargs['name']
    quantity = kwargs['quantity']
    price = kwargs['price']

    preference = {
        "items": [
            {
                "title": name,
                "quantity": quantity,
                "currency_id": "BRL",
                "unit_price": price
            }
        ],
        "payment_methods": {
            "excluded_payment_types": [
                {
                    "id": "credit_card"
                },
                {
                    "id": "debit_card"
                },
                {
                    "id": "paypal"
                },
                {
                    "id": "ticket"
                }
            ]
        }
    }

    mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)

    preferenceResult = mp.create_preference(preference)

    url = preferenceResult["response"]["init_point"]

    data = {
        "url": "/index",
        "topic": "payment"
    }

    mp.post("/webhooks", data)

    return url
