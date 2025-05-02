class CartSession():
    def __init__(self, session):
        self.session=session
        self._cart=self.session.get('cart',{
            'items':[],
            'total_price':0,
            'total_items':0
        })
        self.session['cart']=self._cart
        


    def save(self):
        self.session.modified=True

    def clear(self):  
        self._cart['items']=[]
        self._cart['total_price']=0
        self._cart['total_items']=0
        self.save()  

    def add_product(self,product_id):
        for item in self._cart['items']:
            if item['product_id']==product_id:
                item['quantity']+=1
                break
        else:
            self._cart['items'].append({
                'product_id':product_id,
                'quantity':1
            })
        self._cart['total_items']+=1
        self._cart['total_price']+=1

        