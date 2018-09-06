from lib.fetch_order import ShopifyOrderFetchClass





class FetchAndUpdate:


    def __init__(self,site_url=None, api_key=None, shared_secret=None, access_token=None):
        self.site_url = site_url
        self.api_key = api_key
        self.shared_secret =  None
        self.access_token =  access_token



    def fetch_shopify_orders(self):
        """
        """
        print("ehehhehe")
        obj = ShopifyOrderFetchClass(self.site_url, self.access_token)
        obj.get_the_orders()


    def update_shopify(self, order_id, trcking_numebr):
        pass



t = FetchAndUpdate(site_url='seelftest.myshopify.com',access_token='0c7b2d0e418cf53b2f961551b43ff3d2')
t.fetch_shopify_orders()
