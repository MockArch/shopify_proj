import http.client
import json
from . get_ecz_rates import FecthTheEczRate

class ShopifyOrderFetchClass(object):
    """
    """

    def __init__(self, site_url, access_token):
        if "https://" in site_url:
            site_url = site_url.replace('https://','')
            
        self.apiKey = None
        self.siteUrl = None
        self.accessToken = None
        self.headers = {
            'x-shopify-access-token': access_token,
            'Content-type': 'application/json'
        }
        self.conn = http.client.HTTPSConnection(site_url)

    def get_the_orders(self):
        """
        """
        self.conn.request("GET","/admin/orders.json?fulfillment_status=unshipped&status=open", headers=self.headers)
        data = self.conn.getresponse()
        if data.status == 200:
            data1 = data.read().decode("utf-8")
            rep = json.loads(data1)
            print(json.dumps(rep['orders'][0]['total_price'], indent=4))
            for i in rep['orders']:
                sender = i['line_items'][0]['origin_location']
                reciever = i['shipping_address']
                totalprice = i['total_price']
                is_code = True if i['gateway'] == 'Cash on Delivery (COD)' else False
                count = 2
                weight = 0
                contain = ""
                invoice_num = None
                for it in i['line_items']:
                    couit = it['quantity'] + count
                    invoice_num = it['id']
                    weight = it['grams'] + weight
                    email = i['contact_email']
                    contain = it['name'] + ',' + contain
                   
                obj = FecthTheEczRate(
                    sender, 
                    reciever,
                    is_code, 
                    count,
                    totalprice,
                    invoice_num,
                    weight,
                    email,
                    contain
                     )
                obj.fetch_the_rates()
                
        else:
            print("something went wrong response status code is %s" % str(data.status))
            print(data.read().decode("utf-8"))

    def update_order(self, order_id, tracking_no):
        """
        """
        location_id = 0
        url = '/admin/orders/' + str(order_id) +'/fulfillments.json'
        self.conn.request("GET", "/admin/locations.json",  headers=self.headers)
        loc_data = self.conn.getresponse()
        if loc_data.status == 200:
            rep = json.loads(loc_data.read().decode("utf-8"))
            location_id = rep['locations'][0]['id']
        else:
            print("something went wrong response status code is %s" % str(loc_data.status))
            print(loc_data.read().decode("utf-8"))
        self.conn.close()
        print(location_id)    
        payload = {
            "fulfillment": {
                "location_id": location_id,
                "tracking_number": str(tracking_no),
                "tracking_urls": [
                    'www.test.com/tracking'
                ],
                "notify_customer": True
            }
            }    
        self.conn.request("POST",url, body= json.dumps(payload), headers=self.headers)
        resp_data =  self.conn.getresponse()
        if resp_data.status == 200:
            rep = json.loads(resp_data.read().decode("utf-8"))
            print(rep)
        else:
            print("something went wrong response status code is %s" % str(resp_data.status))
            print(resp_data.read().decode("utf-8"))  
        