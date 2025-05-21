from manim_nerdfont_icons.icons_dict import SYMBOLS_UNICODE
import csv

# Name der Ausgabedatei
output_file = "icon_table.csv"

# Funktion zum Erzeugen der CSV-Datei ohne Example Code Snippet
def generate_csv(symbols_unicode, output_file):
    # Tabellenkopf ohne Example Code Snippet
    header = ["Icon", "Name", "Unicode", "Unicode (Integer)"]

    with open(output_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for name, unicode_int in symbols_unicode.items():
            unicode_char = chr(unicode_int)
            unicode_hex = f"U+{unicode_int:04X}"
            writer.writerow([unicode_char, name, unicode_hex, unicode_int])

    print(f"CSV-file written to {output_file}")

if __name__ == "__main__":
    generate_csv(SYMBOLS_UNICODE, output_file)
