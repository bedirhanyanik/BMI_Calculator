import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    weight = entry_weight.get()
    height = entry_height.get()

    # Boş bırakma kontrolü
    if not weight or not height:
        messagebox.showwarning("Uyarı", "Lütfen gerekli kısımları doldurunuz.")
        return

    # Sayısal değer kontrolü
    try:
        weight = float(weight)
        height = float(height)
    except ValueError:
        messagebox.showerror("Hata", "Geçerli değer giriniz (sayı olmalı).")
        return

    # BMI Hesaplama
    if height <= 0 or weight <= 0:
        messagebox.showerror("Hata", "Boy ve kilo sıfırdan büyük olmalı.")
        return

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        result = f"BMI: {bmi:.2f} - Zayıf"
    elif 18.5 <= bmi < 25:
        result = f"BMI: {bmi:.2f} - Normal"
    elif 25 <= bmi < 30:
        result = f"BMI: {bmi:.2f} - Kilolu"
    else:
        result = f"BMI: {bmi:.2f} - Obez"

    messagebox.showinfo("Sonuç", result)


# Ana pencere
root = tk.Tk()
root.title("BMI Hesaplayıcı")
root.geometry("300x200")

# Kilo label ve giriş
label_weight = tk.Label(root, text="Kilo (kg):")
label_weight.pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

# Boy label ve giriş
label_height = tk.Label(root, text="Boy (metre):")
label_height.pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

# Hesapla butonu
btn_calculate = tk.Button(root, text="BMI Hesapla", command=calculate_bmi)
btn_calculate.pack(pady=10)

root.mainloop()
