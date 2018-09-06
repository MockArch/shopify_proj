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

    def _status_check(self, obj):
        pass
                