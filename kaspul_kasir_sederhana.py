import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="admin_kasir_db"
        )
        self.cursor = self.conn.cursor()

class Member:
    def __init__(self, member_id, nama, vip):
        self.member_id = member_id
        self.nama = nama
        self.vip = vip

    @staticmethod
    def cari_member(db, member_id):
        sql = "SELECT member_id, nama, vip FROM member WHERE member_id = %s"
        db.cursor.execute(sql, (member_id,))
        data = db.cursor.fetchone()

        if data:
            return Member(data[0], data[1], data[2])
        else:
            print("⚠️ Member tidak ditemukan, dianggap NON MEMBER")
            return Member("-", "Pelanggan Umum", 0)


class Barang:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def subtotal(self):
        return self.harga * self.jumlah

class Kasir:
    def __init__(self):
        self.keranjang = []




    def tambah_barang(self, barang):
        self.keranjang.append(barang)

    def total_belanja(self):
        return sum(b.subtotal() for b in self.keranjang)

    def hitung_diskon(self, total, vip):
        diskon = 0

        # Promo minimarket
        if total >= 200000:
            diskon += total * 0.10

        # Diskon VIP
        if vip == 1:
            diskon += total * 0.05

        return diskon

    def cetak_struk(self, member):
        print("\n========= STRUK BELANJA =========")
        print("ID Member :", member.member_id)
        print("Nama      :", member.nama)
        print("Status    :", "VIP" if member.vip else "Non VIP")
        print("\n========= BARANG BELANJA =========")

        for b in self.keranjang:
            print(f"{b.nama} x{b.jumlah} = Rp{b.subtotal():,}")

        total = self.total_belanja()
        diskon = self.hitung_diskon(total, member.vip)
        bayar = total - diskon

        print("\n========= RINCIAN PEMBAYARAN =========")
        print("Total   : Rp", f"{total:,}")
        print("Diskon  : Rp", f"{int(diskon):,}")
        print("Bayar   : Rp", f"{int(bayar):,}")
        print("================================")

        return bayar

db = Database()
print("=== SISTEM KASIR MINIMARKET ===")
member_id = input("Masukkan ID Member: ")

member = Member.cari_member(db, member_id)
if not member:
    exit()

kasir = Kasir()

while True:
    print("\nInput Barang")
    nama = input("Nama barang: ")
    harga = int(input("Harga: "))
    jumlah = int(input("Jumlah: "))

    kasir.tambah_barang(Barang(nama, harga, jumlah))

    lanjut = input("Tambah barang lagi? (y/n): ")
    if lanjut.lower() != "y":
        break

total_bayar = kasir.cetak_struk(member)