from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
HOST = "localhost"
PORT = 5020
def run_server():

    store = ModbusSlaveContext(
        hr=ModbusSequentialDataBlock(1, [0]*2))
    # 2 adet 0'dan başlatılan holding register tanımlandı.
    # Sıcaklık---[0]
    # Nem--------[1]

    context = ModbusServerContext(slaves=store, single=True)

    # Sunucuyu başlat (localhost: 5020)
    try:
        StartTcpServer(context, address=(HOST, 5020))  # Lokal veya ortak ağ revizyonu
    except KeyboardInterrupt:
        print("\nSunucu kapatılıyor!\n")


if __name__ == "__main__":
    print(f"✅ Modbus TCP Server başlatıldı: {HOST}:{PORT}")
    run_server()
