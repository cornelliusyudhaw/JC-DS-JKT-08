import pandas as pd
from sqlalchemy import create_engine
import datetime

engine = create_engine("mysql+mysqlconnector://root:abc123@localhost/hokihokibento?host=localhost?port=3306")
conn = engine.connect()




results_product = conn.execute('SELECT * from produk').fetchall()
menu = pd.DataFrame(results_product, columns = results_product[0].keys())

def lihat_cart():
    cart_check = pd.DataFrame(conn.execute('select produkId from cart').fetchall())
    empty = pd.DataFrame([])
    if cart_check.equals(empty):
        print('Belum ada pesanan')
    else:    
        results_cart = conn.execute ('SELECT * from cart c join produk p on c.produkId = p.id').fetchall()
        cart = pd.DataFrame(results_cart, columns = results_cart[0].keys())
        for i,j,k,l in list(zip(range(1, len(cart)+1), cart['nama'], cart['quantity'], cart['harga'])):
            print(f"{i}. {j} banyak: {k}, total: {k*l}")

def lihat_menu():
    for i,j,k in list(zip(menu['nama'], menu['harga'], range(1,len(menu['nama'])+1))):
        print(f"{k}. {i} harga: {j}")
    while(True):
        pilih = int(input('Beli yang mana: '))
        if pilih <= 0 or pilih > len(menu['nama']):
            print('Coba lagi')
        else:
            while(True):
                banyak = int(input('Berapa banyak: '))
                if banyak <= 0:
                    print('Coba lagi')
                else:
                    break

            cart_check = pd.DataFrame(conn.execute('select produkId from cart').fetchall())
            empty = pd.DataFrame([])
            if cart_check.equals(empty) == False: 
                for i in cart_check[0]:
                        if i == pilih:
                            conn.execute("update cart set quantity = {} where produkId = {}".format(banyak,i))
                        elif (i != pilih) and (pilih not in cart_check[0].values):
                            conn.execute("insert into cart values(null,{},{})".format(pilih,banyak))
                            break
                        else:
                            conn.execute("update cart set quantity = {} where produkId = {}".format(banyak,i))   
            elif cart_check.equals(empty):      
                conn.execute("insert into cart values(null,{},{})".format(pilih,banyak))   

            while(True):      
                lagi = input('Beli lagi (ya/tidak): ') 
                if lagi == 'ya' or lagi == 'tidak':
                    break
                else:
                    print('Coba lagi')    
            if lagi == 'tidak':        
                break            

def checkout():
    cart_check = pd.DataFrame(conn.execute('select produkId from cart').fetchall())
    empty = pd.DataFrame([])
    if cart_check.equals(empty):
        print('Belum ada pesanan')
    else:
        nama = input('Silakan masukkan nama: ')
        
        results_cart = conn.execute('SELECT * from cart c join produk p on c.produkId = p.id').fetchall()
        cart = pd.DataFrame(results_cart, columns = results_cart[0].keys())

        for i,j,k,l in list(zip(range(1, len(cart)+1), cart['nama'], cart['quantity'], cart['harga'])):
            print(f"{i}. {j} banyak: {k}, total: {k*l}")
            
        total_bayar = cart['quantity'].mul(cart['harga']).sum()
        print(f"Total seluruh biaya {total_bayar}")

        while(True):
            uang = int(input('Masukkan pembayaran: '))
            if uang < total_bayar:
                print('Uang kurang')
            elif uang == total_bayar:
                print('Uang pas')
                break
            else:
               print(f"Uang kembali {uang-total_bayar}")
               break     

        date = datetime.datetime.now().date().isoformat()
        result_tr = conn.execute("insert into transaction values(null,'{}','{}',{},{})".format(date,nama,total_bayar,uang))
       
        for i,j,k in list(zip(cart['produkId'], cart['quantity'], cart['harga'])):
            conn.execute("insert into transaction_detail values(null,{},{},{},{})".format(result_tr.lastrowid, i, j, (j*k)))
        
        conn.execute("TRUNCATE cart")

def lihat_history():
    res_history = conn.execute("""select namaPembeli, nama as namaPaket, quantity,
                                     t_d.harga as totalHarga from 
                                     (select namaPembeli, t_d.produkId, quantity,
                                      harga from transaction_detail t_d join transaction t
                                       on t.id = t_d.transactionId)
                                      t_d join produk p on t_d.produkId = p.id """).fetchall()
    history = pd.DataFrame(res_history, columns = res_history[0].keys())
    empty = []
    if history.equals(empty):
        print('Belum ada pesanan')
    else:
        print(history)         
            
def hoki():
    
    while(True):
        print('Selamat Datang di Hoki Hoki Bento\n1. Lihat menu\n2. Lihat cart\n3. Checkout\n4. Lihat history\n5. Keluar')
        milih = int(input('Silakan pilih: '))
        if milih == 1:
            lihat_menu()
        elif milih == 2:
            lihat_cart()
        elif milih == 3:
            checkout()
        elif milih == 4:
            lihat_history()            
        elif milih == 5:
            print('Terima kasih')
            break
        else:
            print('Coba lagi')    

hoki()
