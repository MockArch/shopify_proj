import http.client
import json


class FecthTheEczRate(object):

    def __init__(self, sender, reciever, is_cod, count, totalprice, invoice_num, weight, email, contian):
        self.sender = sender
        self.reciever= reciever
        self.is_cod = is_cod
        self.count = count
        self.totalprice = totalprice
        self.invoice_num = invoice_num
        self.weight = weight
        self.email = email
        self.contain = contian


    def fetch_the_rates(self):
        product_code = self._get_the_rates()
        self._generate_the_lable(product_code)

    def _get_the_rates(self):
        product_code = '1223'
        input_data = {
            "is_cod_booking": self.is_cod,
            "delivery_pincode": self.reciever['zip'],
            "packages": [
                {
                    "length": 10.0,
                    "height": 12.0,
                    "width": 11.0,
                    "weight": 1000.0,
                    "value": str(self.weight)
                }
            ],
            "quantity": self.count,
            "need_insurance": False,
            "is_commercial": True,
            "pickup_pincode": str(self.sender['zip']),
            "is_document": False
        }
        print(json.dumps(input_data, indent=4))
        ###
        # return the Product code
        return product_code

    def _generate_the_lable(self, pc):
       
        label_request = {
            "shipper": {
                "phone":"",# self.sender['phone'],
                "email": self.email,
                "address": {
                    "country": self.sender['country_code'],
                    "street2": self.sender['address2'],
                    "postal_code": self.sender['zip'],
                    "state": self.sender['province_code'],
                    "city": self.sender['city'],
                    "street1": self.sender['address1'],
                    "company_name": self.sender['name']
                },
                "name": self.sender['name']
            },
            "invoice_number": self.invoice_num,
            "send_confirmation_mail": True,
            "parcel_contents": self.contain ,
            "collect_on_delivery": self.totalprice,
            "receiver": {
                "phone": self.reciever['phone'],
                "email": "test@test.com",
                "address": {
                    "country": self.reciever['country'],
                    "street2": self.reciever['address2'],
                    "postal_code": self.reciever['zip'],
                    "state": self.reciever['province_code'],
                    "city": self.reciever['city'],
                    "street1": self.reciever['address1'],
                    "company_name": self.reciever['name']
                },
                "name": self.reciever['name']
            },
            "product_id": pc, # product_id
            "is_test_booking": False,
            "alert_receiver": True,
            "is_multi_packet_shipment": True,
            "customer_reference": "123128731982"
        }
        print(json.dumps(label_request, indent=4))
