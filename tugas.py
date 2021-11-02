Pegawai = 'Ahmad'
Agama = 'Muslim'
Gapok = 4000000
Anak = 2
Tunja = 0.2 * Gapok

if (Anak <= 2):
    Tunke = 0.10 * Gapok
elif (Anak >= 2):
    Tunke = 0.20 * Gapok
else:
    Tunke = 0

Gator = Gapok + Tunja + Tunke
Zapro = (0, 0.025)[Agama == 'Muslim' and Gator >= 6000000]
Gaber = Gator - Zapro

print(
    'Nama Pegawai\t\t :', Pegawai,
    '\nAgama\t\t\t :', Agama,
    '\nJumlah Anak\t\t :', Anak,
    '\nGaji Pokok\t\t : Rp.', Gapok,
    '\nTunjangan Jabatan\t : Rp.', Tunja,
    '\nTunjangan Keluarga\t : Rp.', Tunke,
    '\nGaji Kotor\t\t : Rp.', Gator,
    '\nZakat Profesi\t\t : Rp.', Zapro,
    '\nTake Home Pay\t\t : Rp.', Gaber
)
