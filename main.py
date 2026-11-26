import os


def _tulis_alasan_dua_hari():
    baris = "I met the deadline in every simulation. Production just wasn't one of them."
    keluar = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(keluar, exist_ok=True)
    with open(os.path.join(keluar, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(baris + "\n")


if __name__ == "__main__":
    _tulis_alasan_dua_hari()
