class Cart:
    product = {}

    def addProduct(self, name, num):
        if name not in self.product:
            self.product[name] = 0

        self.product[name] += num

    def removeProduct(self, name, num = 1):
        if name in self.product:
            self.product[name] -= num
        else:
            print "product is not exist"

    def showCart(self):
        return self.product


if __name__ == '__main__':
    cart_obj = Cart()
    cart_obj.addProduct('Baju Merah Mantap', 1)
    cart_obj.addProduct('Baju Merah Mantap', 1)
    cart_obj.addProduct('Bukuku', 3)
    cart_obj.addProduct('Singlet Hijau', 1)
    cart_obj.removeProduct('Bukuku')
    cart_obj.removeProduct('ProdukBohongan')
    print cart_obj.showCart()