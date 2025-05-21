import os

# Import the SYMBOLS_UNICODE dictionary from icons_dict.py
from manim_nerdfont_icons.icons_dict import SYMBOLS_UNICODE

# Output file name
output_file = "icon_table.md"

# Function to generate the Markdown table
def generate_markdown_table(symbols_unicode, output_file):
    # Table header
    table = [
        "| Icon          | Name        | Unicode | Unicode (Integer) | Example Code Snippet            |",
        "|---------------|-------------|---------|--------------------|----------------------------------|",
    ]

    # Populate the table rows
    for name, unicode_int in symbols_unicode.items():
        # Convert integer to character
        unicode_char = chr(unicode_int)
        unicode_hex = f"U+{unicode_int:04X}"
        example_code = f"`icon = nerdfont_icon(\"{name}\")`"
        table.append(
            f"| {unicode_char}            | {name}     | {unicode_hex}  | {unicode_int}              | {example_code}               |"
        )

    # Write the table to the output file
    with open(output_file, "w") as f:
        f.write("\n".join(table))

    print(f"Markdown table written to {output_file}")


if "__main__" == __name__:
    # Generate the Markdown table
    generate_markdown_table(SYMBOLS_UNICODE, output_file)


