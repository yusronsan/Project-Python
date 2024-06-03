# Memebuat nama cafe
print('=================THICKLY CAFE=================')

# Memasukkan nama pembeli dan tanggal pembelian
nama = input('Nama pembeli: ')
tanggal = input('Tanggal: ')

# Header for food menu
print('===============     FOOD     ===============')

# Memasukkan daftar makanan yang disediakan
food_menu = {'Tteoboki': 21.000, 'Corndog': 15.000, 'Mandu': 17.000, 'Croffel': 13.000, 'Ramyeon': 18.000, 'Gimbap': 14.000, 'Egg Toast': 21.000, 'Croissant': 20.000, 'Hotteok': 17.000, 'Crombolini': 23.000}
# Mencetak semua daftar makanan agar pelanggan mengetahui apa saja yang terseda di cafe tersebut
for item, price in food_menu.items():
    price(f'{item}: {price:.3f}')

# Header for drink menu
print('===============     DRINK     ===============')

# Memasukkan daftar minuman yang disediakan 
drink_menu = {'americano': 18.000, 'Matcha ice': 11.000, 'strawberry latte': 21.000, 'latte': 19.000, 'Hot Chocolatte': 15.000, 'Ice Cream Mix3': 15.000, 'Tahi Tea': 18.000} 
# Mencetak semua daftar minuman agar pelabggan