from pymodbus.client.sync import ModbusTcpClient
import time
import random

HOST = 'localhost'  # Server scriptinin çalıştığı Hostun IP adresi
PORT = 5020         # Modbus standart port 502. Geliştirme için 5020 kullanılıyor.
reg_address = 0

print("🔌 Modbus Client başlatıldı.")
try:
    while True:
        try:
            client = ModbusTcpClient(HOST, port=PORT)  # ModbusTcpClient ile bağlanmayı dener.
            if not client.connect():                   # Bağlantı sağlanmazsa.
                print("❌ Sunucuya bağlanılamıyor... Tekrar deneniyor.")
                time.sleep(3)  # 3 saniye bekle. Tekrar dene.
                continue

            print("✅ Sunucuya bağlandı!")

            while True:
                sicaklik = round(random.uniform(20, 30))  # Rastgele sıcaklık ve nem değerleri üretiliyor.
                nem = random.randint(40, 60)

                r1 = client.write_register(reg_address, sicaklik)  # Sıcaklık değerinin holding register'a yazılması
                r2 = client.write_register(reg_address + 1, nem)

                print(f"Sıcaklık: {sicaklik} °C | Nem: %{nem}")
                time.sleep(5)

        except Exception as e:
            print(e)

except KeyboardInterrupt:
    print("\nProgram kapatılıyor!\n")
