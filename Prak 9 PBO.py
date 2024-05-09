import math
class BangunRuang:
    def volume(self, *bangunruang):
        if len(bangunruang) == 1:
            #Volume Kubus
            sisi = bangunruang[0]
            return sisi ** 3
        elif len(bangunruang) == 3:
            #Volume Balok
            panjang, lebar, tinggi = bangunruang
            return panjang * lebar * tinggi
        elif len(bangunruang) == 2:
            #Volume Tabung
            jari_jari, tinggi = bangunruang
            return math.pi * jari_jari ** 2 * tinggi
        else:
            return "Jumlah argumen salah, tidak bisa untuk menghitung volume"

bangun_ruang = BangunRuang()
print("===============================\nNama : Rangga Aditya Pradana\nNIM : 064002300026\n===============================")
print("Volume Kubus dengan sisi 5 adalah :", bangun_ruang.volume(5))
print("Volume Balok dengan panjang 3, lebar 4, dan tinggi 5 adalah :", bangun_ruang.volume(3, 4, 5))
print("Volume Tabung dengan jari-jari 2 dan tinggi 6 adalah :", bangun_ruang.volume(2, 6))




