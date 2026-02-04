"""Game Tebak Kosakata (bahasa Indonesia)

Cara main:
- Program menampilkan sebuah kata (dalam satu bahasa).
- Disediakan opsi 1-5 berisi daftar negara.
- Pemain memilih angka 1-5 yang menurutnya merupakan negara yang tepat untuk kata tersebut.
- Program memberi tahu benar/salah dan menampilkan skor di akhir.
"""

import random
from typing import List, Dict

ENTRIES: List[Dict[str, str]] = [
    {"word": "bonjour", "language": "Prancis", "country": "Prancis"},
    {"word": "hello", "language": "Inggris", "country": "Inggris"},
    {"word": "hola", "language": "Spanyol", "country": "Spanyol"},
    {"word": "selamat pagi", "language": "Indonesia", "country": "Indonesia"},
    {"word": "hallo", "language": "Jerman", "country": "Jerman"},
    {"word": "ciao", "language": "Italia", "country": "Italia"},
    {"word": "bom dia", "language": "Portugis", "country": "Brasil"},
    {"word": "konnichiwa", "language": "Jepang", "country": "Jepang"},
    {"word": "nǐ hǎo", "language": "Mandarin", "country": "Tiongkok"},
    {"word": "privet", "language": "Rusia", "country": "Rusia"},
    {"word": "marhaba", "language": "Arab", "country": "Arab Saudi"},
    {"word": "annyeong", "language": "Korea", "country": "Korea Selatan"},
    {"word": "namaste", "language": "Hindi", "country": "India"},
    {"word": "sawubona", "language": "Zulu", "country": "Afrika Selatan"},
    {"word": "dzień", "language": "Polandia", "country": "Polandia"},
    {"word": "hej", "language": "Swedia", "country": "Swedia"},
    {"word": "salut", "language": "Rumania/Prancis", "country": "Rumania"},
    {"word": "olá", "language": "Portugis/Espanyol", "country": "Portugal"},
    {"word": "hei", "language": "Norwegia", "country": "Norwegia"},
    {"word": "goedendag", "language": "Belanda", "country": "Belanda"},
]

ALL_COUNTRIES = sorted({entry["country"] for entry in ENTRIES})


def build_options(correct_country: str, all_countries: List[str], k: int = 5) -> List[str]:
    """Buat daftar opsi berisi `k` negara termasuk negara yang benar."""
    choices = [c for c in all_countries if c != correct_country]
    distractors = random.sample(choices, k - 1)
    opts = distractors + [correct_country]
    random.shuffle(opts)
    return opts


def ask_round(entry: Dict[str, str], all_countries: List[str]) -> bool:
    word = entry["word"]
    language = entry.get("language", "-")
    correct = entry["country"]
    options = build_options(correct, all_countries)

    print(f"\nKata: '{word}'")
    # Jangan tampilkan bahasa agar pemain menebak dari kata saja (lebih menantang)
    for i, opt in enumerate(options, start=1):
        print(f"  {i}. {opt}")

    while True:
        choice = input("Pilih jawaban (1-5) atau 'q' untuk keluar: ").strip().lower()
        if choice == "q":
            raise KeyboardInterrupt
        if choice in {"1", "2", "3", "4", "5"}:
            idx = int(choice) - 1
            selected = options[idx]
            is_correct = selected == correct
            if is_correct:
                print("✅ Benar!")
            else:
                print(f"❌ Salah. Jawaban benar: {correct} ({language})")
            return is_correct
        print("Masukkan tidak valid — masukkan angka 1-5 atau q untuk keluar.")


def main():
    print("=== Game Tebak Kosakata ===")
    print("Tebak negara asal kata. Ketik 'q' kapan saja untuk keluar.")

    try:
        rounds_input = input("Berapa ronde yang ingin dimainkan? (default 5): ").strip()
        rounds = int(rounds_input) if rounds_input else 5
    except ValueError:
        rounds = 5

    score = 0
    used = set()
    available = list(range(len(ENTRIES)))
    random.shuffle(available)

    for r in range(1, rounds + 1):
        if not available:
            print("Selesai: tidak ada lagi kata yang tersisa.")
            break
        idx = available.pop()
        entry = ENTRIES[idx]
        print(f"\n--- Ronde {r} dari {rounds} ---")
        try:
            if ask_round(entry, ALL_COUNTRIES):
                score += 1
        except KeyboardInterrupt:
            print("\nKeluar dari permainan...")
            break

    print("\n=== Hasil ===")
    print(f"Skor kamu: {score} dari {r if 'r' in locals() else 0}")
    pct = (score / (r if 'r' in locals() else 1)) * 100
    print(f"Persentase: {pct:.1f}%")

    again = input("Mau main lagi? (y/N): ").strip().lower()
    if again == "y":
        main()


if __name__ == "__main__":
    main()
