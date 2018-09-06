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
            'x-shopify-access-token': access_token
        }
        print(site_url)
        self.conn = http.client.HTTPSConnection(site_url)

    def get_the_orders(self):
        """
        """
        self.conn.request("GET","/admin/orders.json?fulfillment_status=unshipped&status=open", headers=self.headers)
        data = self.conn.getresponse()
        if data.status == 200:
            data1 = data.read().decode("utf-8")
            rep = json.loads(data1)
            for i in rep['orders']:
                sender_pincode = i['line_items'][0]['origin_location']['zip']
                reciever_pincode = i['shipping_address']['zip']
                is_code = True if i['gateway'] == 'Cash on Delivery (COD)' else False
                count =  i['line_items'][0]['quantity']

                obj = FecthTheEczRate(sender_pincode, reciever_pincode, is_code, count)
                obj.fetch_the_rates()
            
                
        else:
            print("something went wrong response status code is %s" % str(data.status))
            print(data.read().decode("utf-8"))

    def _status_check(self, obj):
        pass
                