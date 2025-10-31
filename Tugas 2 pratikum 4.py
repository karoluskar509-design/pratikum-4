import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# Fungsi Substitusi Cipher
# -----------------------------
def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext

# -----------------------------
# Fungsi Transposisi Cipher
# -----------------------------
def transposisi_cipher(plaintext):
    # Hapus spasi sebelum transposisi
    plaintext = plaintext.replace(" ", "")
    part_length = len(plaintext) // 4
    parts = [plaintext[i:i + part_length] for i in range(0, len(plaintext), part_length)]
    ciphertext = ''
    for col in range(4):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]
    return ciphertext

# -----------------------------
# Fungsi untuk Menjalankan Proses
# -----------------------------
def proses_cipher():
    plaintext = entry_plaintext.get().upper()
    aturan_input = entry_aturan.get().upper()

    # Validasi input
    if not plaintext.strip():
        messagebox.showerror("Error", "Plaintext tidak boleh kosong!")
        return
    if not aturan_input.strip():
        messagebox.showerror("Error", "Aturan substitusi tidak boleh kosong!")
        return

    # Parsing aturan substitusi
    try:
        aturan_pairs = [pair.strip() for pair in aturan_input.split(',')]
        aturan = {}
        for pair in aturan_pairs:
            k, v = pair.split(':')
            aturan[k.strip()] = v.strip()
    except:
        messagebox.showerror("Error", "Format aturan salah!\nGunakan format seperti: A:B, B:C, C:D")
        return

    # Proses substitusi
    cipher_substitusi = substitusi_cipher(plaintext, aturan)
    # Proses transposisi
    cipher_transposisi = transposisi_cipher(cipher_substitusi)

    # Tampilkan hasil
    entry_substitusi.delete(0, tk.END)
    entry_substitusi.insert(0, cipher_substitusi)
    entry_transposisi.delete(0, tk.END)
    entry_transposisi.insert(0, cipher_transposisi)

# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("Program Gabungan Substitusi & Transposisi Cipher")
root.geometry("700x420")
root.resizable(False, False)

# Judul
title_label = ttk.Label(root, text="🔐 Substitusi & Transposisi Cipher", font=("Arial", 18, "bold"))
title_label.pack(pady=15)

# Frame utama
frame = ttk.Frame(root, padding=10)
frame.pack(fill="x", padx=30)

# Input plaintext
ttk.Label(frame, text="Masukkan Plaintext:").grid(row=0, column=0, sticky="w", pady=5)
entry_plaintext = ttk.Entry(frame, width=60)
entry_plaintext.grid(row=0, column=1, pady=5)

# Input aturan substitusi
ttk.Label(frame, text="Masukkan Aturan Substitusi (contoh: U:K, N:N, I:I, K:K, A:B):").grid(row=1, column=0, sticky="w", pady=5)
entry_aturan = ttk.Entry(frame, width=60)
entry_aturan.grid(row=1, column=1, pady=5)

# Tombol Proses
ttk.Button(root, text="🔄 Proses Enkripsi", command=proses_cipher).pack(pady=15)

# Hasil
hasil_frame = ttk.Frame(root, padding=10)
hasil_frame.pack(fill="x", padx=30)

ttk.Label(hasil_frame, text="Hasil Substitusi Cipher:").grid(row=0, column=0, sticky="w", pady=5)
entry_substitusi = ttk.Entry(hasil_frame, width=60)
entry_substitusi.grid(row=0, column=1, pady=5)

ttk.Label(hasil_frame, text="Hasil Substitusi + Transposisi Cipher:").grid(row=1, column=0, sticky="w", pady=5)
entry_transposisi = ttk.Entry(hasil_frame, width=60)
entry_transposisi.grid(row=1, column=1, pady=5)

# Footer
ttk.Label(root, text="Dibuat oleh: Latihan Substitusi & Transposisi Cipher", font=("Arial", 10, "italic")).pack(pady=10)

root.mainloop()
