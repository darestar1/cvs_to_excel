import pandas as pd
import tkinter as tk
from tkinter import filedialog
def transfer_data(csv_path, excel_path):
    try:
        # CSV dosyasını oku
        veri_df = pd.read_csv(csv_path)

        # Excel dosyasını oku
        hedef_df = pd.read_excel(excel_path)

        # CSV'den gelen verileri Excel dosyasındaki observationid sütununa eşleştir
        hedef_df['Observation ID'] = veri_df['Name']
        hedef_df['UTM Zone'] = veri_df['Zone']
        hedef_df['Description'] = veri_df['Description']
        hedef_df['Easting m'] = veri_df['Easting']
        hedef_df['Northing m'] = veri_df['Northing']
        hedef_df['Date'] = veri_df['Time']

        # Değişiklikleri kaydet
        hedef_df.to_excel(excel_path, index=False)

        # Değişikliklerin uygulandığını onaylamak için Excel dosyasını tekrar oku ve yazdır
        hedef_df = pd.read_excel(excel_path)
        print(hedef_df)

        print("Veri aktarımı başarıyla tamamlandı.")
    except Exception as e:
        print("Veri aktarımı sırasında bir hata oluştu:", str(e))

def browse_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    csv_entry.delete(0, tk.END)
    csv_entry.insert(0, file_path)

def browse_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
    excel_entry.delete(0, tk.END)
    excel_entry.insert(0, file_path)

# Tkinter penceresini oluştur
root = tk.Tk()
root.title("Veri Aktarım Uygulaması")

# CSV dosyası seçme butonu ve etiketi
tk.Label(root, text="CSV Dosyası:").grid(row=0, column=0)
csv_path = tk.StringVar()
csv_entry = tk.Entry(root, textvariable=csv_path, width=50)
csv_entry.grid(row=0, column=1)
tk.Button(root, text="CSV Dosyası Seç", command=browse_csv, width=15).grid(row=0, column=2)

# Excel dosyası seçme butonu ve etiketi
tk.Label(root, text="Excel Dosyası:").grid(row=1, column=0)
excel_path = tk.StringVar()
excel_entry = tk.Entry(root, textvariable=excel_path, width=50)
excel_entry.grid(row=1, column=1)
tk.Button(root, text="Excel Dosyası Seç", command=browse_excel, width=15).grid(row=1, column=2)

# Veri aktarım butonu
tk.Button(root, text="Veri Aktarımını Başlat", command=lambda: transfer_data(csv_path.get(), excel_path.get()), width=30).grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
