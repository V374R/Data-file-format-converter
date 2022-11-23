# Data-file-format-converter
Converts between json, yaml, and toml file formats
This script is used to convert between the popular data formats: json, yaml, and toml. It
takes a filename as an input, the input file format, and the output file format. It then
creates a new file with the required format or prints converted data to the console.
Please adhere to the following script usage. (note that inputs between square brackets
are optional)

Usage:
convert.py [-h] --out {yaml,json,toml} [--in {yaml,json,toml}]
[--output-file OUTPUT_FILE] [--print-only] file
Converts between json, yaml, and toml file formats

positional arguments:
file input file

optional arguments:
-h, --help show this help message and exit
--out {yaml,json,toml}
                      the output file format
--in {yaml,json,toml}
                     input file format. If not provided, the
script tries to auto detect format from filename
--output-file OUTPUT_FILE, -o OUTPUT_FILE
                      the output filename. If not provided, the
output file will have the same name as the input file
--print-only, -p print converted file contents to console
                      instead of writing to output file
