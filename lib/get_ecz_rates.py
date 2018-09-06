import http.client
import json

class FecthTheEczRate(object):

    def __init__(self, sender_pincode, reciever_pincode, is_cod, count):
        self.sender_pincode = sender_pincode
        self.reciever_pincode = reciever_pincode
        self.is_cod = is_cod
        self.count = count

    def fetch_the_rates(self):
        product_code = '1223'
        input_data = {
            "is_cod_booking": self.is_cod,
            "delivery_pincode": self.reciever_pincode,
            "packages": [
                {
                    "length": 10.0,
                    "height": 12.0,
                    "width": 11.0,
                    "weight": 1000.0,
                    "value": "240"
                }
            ],
            "quantity": self.count,
            "need_insurance": False,
            "is_commercial": True,
            "pickup_pincode": str(self.sender_pincode),
            "is_document": False
        }
        print(json.dumps(input_data, indent=4))
        ###
        # return the Product code
        return product_code