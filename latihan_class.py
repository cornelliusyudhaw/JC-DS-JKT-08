
class BikinMenu:
    def __init__(self, nama, menu, harga):
        self.name = nama
        self.menus = menu
        self.price = harga
        self.history = []

    def menu_price(self):
       buy = int(input('Mau beli yang mana: '))
       try:
           print('{} telah membeli {} dengan harga {}'.format(self.name, self.menus[buy-1], self.price[buy-1]))
           self.history.append(self.menus[buy-1])
       except:
           print('Invalid input')    
       
    def get_menu(self):      
        print('Menu Makanan\n')
        for idx, val, price in zip(range(len(self.menus)),self.menus, self.price):
            print('{}. {} harganya adalah {}'.format(idx+1, val, price))
        print('\n')
        
    def get_history(self):
        if len(self.history):
            z = '{} telah membeli'.format(self.name)
            if len(self.history) == 1:
                z += ' {}'.format(self.history[0])
                print(z)
            else:
                if len(self.history) == 2:
                        z += ' {} dan {}'.format(self.history[0], self.history[1])

                for idx, val in enumerate(self.history):
                    if len(self.history) == 2:
                        break
                    elif idx == len(self.history) - 1:
                        z += ' dan {}'.format(val)
                    elif idx == len(self.history) - 2:
                        z += ' {}'.format(val)    
                    else:
                        z += ' {},'.format(val)
                print(z)        
        else:
            print('Belum ada pembelian')                        

Paul=BikinMenu('Paul', ['Ayam Goreng', 'Nasi Bakar', 'Sate Kambing'], [1000, 2000, 3000])

Paul.get_menu()

Paul.menu_price()
Paul.menu_price()
Paul.menu_price()
Paul.menu_price()
Paul.get_history()

# Paul.menu_price()
# Paul.get_history()
# Paul.menu_price()
# Paul.get_history()
# Paul.menu_price()
# Paul.get_history()