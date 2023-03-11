#shopping cart
class Shopping:
    product={"mobiles" : ["iphone", "samsung"],
              "laptops" : ["Lenovo", "microsoft"]}
    l=[]
    for i in product.keys():
        l.append(product[i])
    def __init__(self):
        self.cart=[]



    def add_to_cart(self, item):
        self.item = item
        for j in self.l:
            if self.item in j:
                self.cart.append(self.item)
    def remove_cart(self, item):
        self.item = item
        for j in self.l:
            if item in j:
                self.cart.remove(self.item)
    def display_cart(self):
        print("products you have in cart are : ")
        for a in self.cart:
            print(a)



s = Shopping()
s.add_to_cart("iphone")
s.add_to_cart("lenovo")
s.add_to_cart("samsung")
s.add_to_cart("microsoft")
s.remove_cart("lenovo")
s.display_cart()



