import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QDialog, \
    QMessageBox, QFileDialog, QComboBox, QSizePolicy, QGridLayout
from PyQt5.QtGui import QPixmap
class SistemInformasiObat(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Apoid")
        self.setGeometry(300, 100, 600, 600)

        self.label_penyakit = QLabel("Cari Penyakit:")
        self.penyakit_input = QLineEdit()

        self.label_umur = QLabel("Pilih Umur:")
        self.combo_umur = QComboBox()
        self.combo_umur.addItem("Dewasa")
        self.combo_umur.addItem("Anak-anak")

        self.btn_cari_obat = QPushButton("Cari Obat")
        self.btn_cari_obat.clicked.connect(self.cari_obat)

        self.search_results_layout = QVBoxLayout()

        self.label_hasil = QLabel("Hasil Pencarian:")

        self.btn_credit = QPushButton("Credit")
        self.btn_credit.clicked.connect(self.show_credit_dialog)



        layout = QVBoxLayout()

        layout.addWidget(self.label_penyakit)
        layout.addWidget(self.penyakit_input)
        layout.addWidget(self.label_umur)
        layout.addWidget(self.combo_umur)
        layout.addWidget(self.btn_cari_obat)
        layout.addWidget(self.label_hasil)
        layout.addLayout(self.search_results_layout)
        layout.addWidget(self.btn_credit)
        self.setLayout(layout)

    def cari_obat(self):
        penyakit = self.penyakit_input.text()
        umur = self.combo_umur.currentText()
            {
                "penyakit": "Flu",
                "obat": "Procold",
                "harga": "Rp. 4.000 - Rp. 4.470",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Flu",
                "obat": "Ultraflu",
                "harga": "Rp. 2.900 - Rp. 6.000",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Flu",
                "obat": "Intunal-F",
                "harga": "Rp. 3.294 - Rp. 5.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Alergi ringan",
                "obat": "Caladine Salep 15 mg",
                "harga": "Rp. 8.500 - Rp. 8.800",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Alergi ringan",
                "obat": "Caladine Salep 15 mg",
                "harga": "Rp. 6.500 - Rp. 10.000",
                "kategori": "Anak-anak",

            },
            {
                "penyakit": "Alergi ringan",
                "obat": "Cetirizine Kaplet",
                "harga": "Rp. 2.500 - Rp. 7.000",
                "kategori": "Dewasa",

            },
            {
                "penyakit": "Alergi ringan",
                "obat": "Cetirizine Kaplet",
                "harga": "Rp. 1.000 - Rp. 6.900",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Alergi ringan",
                "obat": "Loratadine Kaplet",
                "harga": "Rp. 9.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Amandel",
                "obat": "Amoxan",
                "harga": "Rp. 42.500 - Rp. 65.500",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Amandel",
                "obat": "Amoxan",
                "harga": "Rp. 33.500 - Rp. 40.900",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Amandel",
                "obat": "Amoxilin Kaplet",
                "harga": "Rp. 6.100 - Rp. 9.700",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Amandel",
                "obat": "Amoxilin Kaplet",
                "harga": "Rp. 7.000 - Rp. 10.000",
                "kategori": "Dewasa",

            },
            {
                "penyakit": "Amandel",
                "obat": "Cefadroxil",
                "harga": "Rp. 59.000 - Rp. 64.000",
                "kategori": "Anak-anak",

            },
            {
                "penyakit": "Amandel",
                "obat": "Cefadroxil",
                "harga": "Rp. 58.300 - Rp. 63.700",
                "kategori": "Dewasa",

            },
            {
                "penyakit": "Batuk pilek",
                "obat": "Alerhis",
                "harga": "Rp. 13.000 - Rp. 13.800",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Batuk pilek",
                "obat": "Alerhis",
                "harga": "Rp. 13.000 - Rp. 13.800",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Batuk pilek",
                "obat": "Benadryl Sirup",
                "harga": "Rp. 23.400 - Rp. 26.600",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Batuk pilek",
                "obat": "Benadryl Sirup",
                "harga": "Rp. 23.400 - Rp. 26.600",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Batuk pilek",
                "obat": "Bisolvon 8 mg",
                "harga": "Rp. 25.000 - Rp. 34.000",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Batuk pilek",
                "obat": "Bisolvon 8 mg",
                "harga": "Rp. 25.000 - Rp. 34.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Demam",
                "obat": "Bufect suspensi",
                "harga": "Rp. 21.900",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Demam",
                "obat": "Bufect suspensi",
                "harga": "Rp. 21.900",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Demam",
                "obat": "Prioris Triple Action",
                "harga": "Rp. 9.600 - Rp. 10.900",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Demam",
                "obat": "Prioris Triple Action",
                "harga": "Rp. 9.600 - Rp. 10.900",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Demam",
                "obat": "Sanmol",
                "harga": "Rp. 1.500 - Rp. 2.500",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Demam",
                "obat": "Sanmol",
                "harga": "Rp. 1.500 - Rp. 2.500",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Diare",
                "obat": "Diatabs",
                "harga": "Rp. 2.300 - Rp. 3.200",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Diare",
                "obat": "Diatabs",
                "harga": "Rp. 2.300 - Rp. 3.200",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Diare",
                "obat": "Leoperamide",
                "harga": "Rp. 20.000",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Diare",
                "obat": "Leoperamide",
                "harga": "Rp. 20.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Diare",
                "obat": "Oralit",
                "harga": "Rp. 1.100",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Diare",
                "obat": "Oralit",
                "harga": "Rp. 1.100",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Gangguan pencernaan ringan",
                "obat": "anatasida tablet 200mg",
                "harga": "Rp. 1.800 - Rp. 8.000",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Gangguan pencernaan ringan",
                "obat": "anatasida tablet 200mg",
                "harga": "Rp. 1.800 - Rp. 8.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Gangguan pencernaan ringan",
                "obat": "antasida-doen antasida-doen-sirup",
                "harga": "Rp. 4.500 - Rp. 7.000",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Gangguan pencernaan ringan",
                "obat": "antasida-doen antasida-doen-sirup",
                "harga": "Rp. 4.500 - Rp. 7.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Gangguan pencernaan ringan",
                "obat": "Lasoprazole",
                "harga": "Rp. 4.500 - Rp. 7.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Gangguan tidur ringan",
                "obat": "Antangin Good Night",
                "harga": "Rp. 6.100 - Rp. 6.400",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Gangguan tidur ringan",
                "obat": "Lelap",
                "harga": "Rp. 31.000 - Rp. 38.800",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Gangguan tidur ringan",
                "obat": "Nutrimax Dream",
                "harga": "Rp. 98.000 - Rp. 287.700",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Gatal gatal kulit",
                "obat": "Alleron 4 mg",
                "harga": "Rp. 1.000 - Rp. 2.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Gatal gatal kulit",
                "obat": "Alleron 4 mg",
                "harga": "Rp. 1.000 - Rp. 2.000",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Gatal gatal kulit",
                "obat": "Caladine lotion",
                "harga": "Rp. 16.000 - Rp. 21.000",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Gatal gatal kulit",
                "obat": "Caladine lotion",
                "harga": "Rp. 16.000 - Rp. 21.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Gatal gatal kulit",
                "obat": "Heroxyn Bedak 85mg",
                "harga": "Rp. 14.000 - Rp. 16.000",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Gatal gatal kulit",
                "obat": "Heroxyn Bedak 85mg",
                "harga": "Rp. 14.000 - Rp. 16.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Gigi sensitif",
                "obat": "Ibuprofen",
                "harga": "Rp. 2.600 - Rp. 7.100",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Gigi sensitif",
                "obat": "Mefinal kaplet",
                "harga": "Rp. 15.000 - Rp. 25.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Gigi sensitif",
                "obat": "Ponstan Kaplet",
                "harga": "Rp. 32.600 - Rp. 38.100",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "kram perut ringan",
                "obat": "Feminax kaplet",
                "harga": "Rp. 2.200 - Rp. 3.800",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "kram perut ringan",
                "obat": "Feminax kaplet",
                "harga": "Rp. 2.200 - Rp. 3.800",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "kram perut ringan",
                "obat": "Mefinal Kaplet",
                "harga": "Rp. 15.000 - Rp. 25.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "kram perut ringan",
                "obat": "Polysilane sirup",
                "harga": "Rp. 21.700 - Rp. 31.000",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "kram perut ringan",
                "obat": "Polysilane sirup",
                "harga": "Rp. 21.700 - Rp. 31.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Luka goresan",
                "obat": "Betadine",
                "harga": "Rp. 15.700 - Rp. 16.500",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Luka goresan",
                "obat": "Betadine",
                "harga": "Rp. 15.700 - Rp. 16.500",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Luka goresan",
                "obat": "Hansaplast",
                "harga": "Rp. 6.700 - Rp. 7.000",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Luka goresan",
                "obat": "Hansaplast",
                "harga": "Rp. 6.700 - Rp. 7.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Luka goresan",
                "obat": "Rivanol one Med 100mL",
                "harga": "Rp. 5.500 - Rp. 7.700",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Luka goresan",
                "obat": "Rivanol one Med 100mL",
                "harga": "Rp. 5.500 - Rp. 7.700",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Masuk angin",
                "obat": "Antangin",
                "harga": "Rp. 13.800 - Rp. 17.600",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Masuk angin",
                "obat": "Antangin",
                "harga": "Rp. 13.800 - Rp. 17.600",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Masuk angin",
                "obat": "Freshcare",
                "harga": "Rp. 13.500 - Rp. 16.600",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Masuk angin",
                "obat": "Freshcare",
                "harga": "Rp. 13.500 - Rp. 16.600",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Masuk angin",
                "obat": "Tolak angin",
                "harga": "Rp. 54.500 - Rp. 60.600",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Masuk angin",
                "obat": "Tolak angin",
                "harga": "Rp. 54.500 - Rp. 60.600",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Mata merah",
                "obat": "Cendo citrol tetes",
                "harga": "Rp. 29.600 - Rp. 38.800",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Mata merah",
                "obat": "Insto",
                "harga": "Rp. 15.500 - Rp. 24.900",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Mata merah",
                "obat": "Rohto tetes",
                "harga": "Rp. 14.000 - Rp. 19.700",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Mata merah",
                "obat": "Rohto tetes",
                "harga": "Rp. 14.000 - Rp. 19.700",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Nyeri otot",
                "obat": "CounterPain cream",
                "harga": "Rp. 125.500",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Nyeri otot",
                "obat": "NeoRemacyl",
                "harga": "Rp. 8.400 - Rp. 10.700",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Nyeri otot",
                "obat": "Paramex Nyeri otot",
                "harga": "Rp. 2.400",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Pilek biasa",
                "obat": "Actifed Plus Expectorant sirup hijau",
                "harga": "Rp. 66.700 - Rp. 69.800",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Pilek biasa",
                "obat": "Afrin Nasal Spray",
                "harga": "Rp. 61.603",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Pilek biasa",
                "obat": "Afrin Nasal Spray",
                "harga": "Rp. 61.603",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Pilek biasa",
                "obat": "Sanmol Forte Syrup",
                "harga": "Rp. 32.500 - Rp. 39.500",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Radang Tenggorokan",
                "obat": "Cooling 5 Mouth Spray",
                "harga": "Rp. 31.500 - Rp. 45.500",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Radang Tenggorokan",
                "obat": "Cooling 5 Mouth Spray",
                "harga": "Rp. 31.500 - Rp. 45.500",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Radang Tenggorokan",
                "obat": "Degirol hisap",
                "harga": "Rp. 19.300 - Rp. 31.100",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Radang Tenggorokan",
                "obat": "Methylprednisolone",
                "harga": "Rp. 6.900 - Rp. 12.900",
                "kategori": "Anak-anak",
            },
            {
                "penyakit": "Radang Tenggorokan",
                "obat": "Methylprednisolone",
                "harga": "Rp. 6.900 - Rp. 12.900",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Sakit kepala ringan",
                "obat": "Bodrex",
                "harga": "Rp. 3.200 - Rp. 11.900",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Sakit kepala ringan",
                "obat": "Panadol",
                "harga": "Rp. 11.500 - Rp. 15.700",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Sakit kepala ringan",
                "obat": "Paramex",
                "harga": "Rp. 3.100 - Rp. 12.900",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Sariawan",
                "obat": "Degirol",
                "harga": "Rp. 19.300 - Rp. 31.100",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Sariawan",
                "obat": "Mixsaga",
                "harga": "Rp. 25.000 - Rp. 37.000",
                "kategori": "Dewasa",
            }, {
                "penyakit": "Sariawan",
                "obat": "Enkasari",
                "harga": "Rp. 23.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Vertigo",
                "obat": "Benzodiazepine",
                "harga": "Rp. 30.000",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Vertigo",
                "obat": "Betahistine",
                "harga": "Rp. 2.500 - Rp. 13.200",
                "kategori": "Dewasa",
            },
            {
                "penyakit": "Vertigo",
                "obat": "Dimenhydrinate",
                "harga": "Rp. 35.000",
                "kategori": "Dewasa",
            },
        ]
        while self.search_results_layout.count():
            item = self.search_results_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        matching_obat = [item for item in data_obat_list if
                         item["penyakit"].lower() == penyakit.lower() and item["kategori"] == umur]

        if matching_obat:
            for obat_info in matching_obat:
                obat = obat_info["obat"]
                harga = obat_info["harga"]

                result_widget = QWidget()
                result_layout = QHBoxLayout()

                label_result = QLabel(f"Obat: {obat}, Harga: {harga}")
                result_layout.addWidget(label_result)


                result_widget.setLayout(result_layout)
                self.search_results_layout.addWidget(result_widget)
        else:
            self.search_results_layout.addWidget(QLabel("Data obat tidak ditemukan."))

    def show_credit_dialog(self):
        # Tampilkan dialog kredit
        credit_dialog = QDialog(self)
        credit_dialog.setWindowTitle("Credit")
        credit_dialog.setGeometry(100, 100, 400, 200)

        # Data contoh (ganti ini dengan data sebenarnya Anda)
        pembuat_info = [
            {"nama": "Ahmad Hidayat Nurwahid Hayim", "nim": "18231005"},
            {"nama": "Elvira Rahmadani Setyaningrum", "nim": "18231024"},
            {"nama": "Mochammad Meziedane Febri Muzaranu", "nim": "18231034"},
            {"nama": "Muhammad Rifqy", "nim": "18231036"},
        ]

        grid_layout = QGridLayout(credit_dialog)

        for row, pembuat in enumerate(pembuat_info):
            # Tambahkan QLabel untuk informasi lainnya
            label_nama = QLabel(pembuat["nama"], credit_dialog)
            grid_layout.addWidget(label_nama, row, 1)

            label_peran = QLabel(pembuat["nim"], credit_dialog)
            grid_layout.addWidget(label_peran, row, 2)
        close_button = QPushButton("Tutup", credit_dialog)
        close_button.clicked.connect(credit_dialog.accept)
        grid_layout.addWidget(close_button, len(pembuat_info), 0, 1, 3)

        # Menampilkan dialog kredit
        credit_dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SistemInformasiObat()
    window.show()
    sys.exit(app.exec_())

