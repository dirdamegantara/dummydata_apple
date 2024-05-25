import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Menentukan rentang harga untuk setiap produk
price_ranges = {
    "iPhone": (7000000, 20000000, 100000),
    "iPad": (7000000, 15000000, 100000),
    "MacBook": (10000000, 50000000, 100000)
}

# Rentang kuantitas untuk setiap produk
quantity_ranges = {
    "iPhone": (50, 1000),
    "iPad": (10, 1000),
    "MacBook": (10, 1000)
}

# Fungsi untuk menghasilkan harga acak dalam rentang tertentu dengan perbedaan harga tertentu
def random_price(min_price, max_price, step):
    return np.random.choice(np.arange(min_price, max_price + step, step))

# Membuat tanggal transaksi berurutan
start_date = datetime.now() - timedelta(days=1000)
dates = [start_date + timedelta(days=i) for i in range(1000)]

# Membuat data penjualan dummy
data = []
for date in dates:
    entry = {"Tanggal Transaksi": date.strftime("%d/%m/%Y")}
    total_quantity = 0
    total_revenue = np.int64(0)  # Pastikan total pendapatan menggunakan tipe int64
    for product, (min_price, max_price, step) in price_ranges.items():
        price = random_price(min_price, max_price, step)
        min_quantity, max_quantity = quantity_ranges[product]
        quantity = np.random.randint(min_quantity, max_quantity + 1)
        total_quantity += quantity
        total_revenue += np.int64(price) * np.int64(quantity)  # Menggunakan np.int64 untuk kedua operand
        entry[f"{product} Terjual"] = quantity
    entry["Jumlah Transaksi"] = total_quantity
    entry["Total Pendapatan"] = total_revenue
    data.append(entry)

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan 10 data pertama
print(df.head(10))

# Menyimpan data ke file CSV tanpa kolom harga individual produk
df.to_csv("dummy_penjualan_apple_indonesia.csv", index=False, columns=["Tanggal Transaksi", "iPhone Terjual", "iPad Terjual", "MacBook Terjual", "Jumlah Transaksi", "Total Pendapatan"])
