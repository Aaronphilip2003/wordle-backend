import csv

# Input and output file paths
input_file = 'words.txt'
output_file = 'words.csv'

# Read words from text file and write to CSV
with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    # Create CSV writer
    writer = csv.writer(outfile)
    
    # Write header row
    writer.writerow(["line_number", "word"])

    # Read each line, strip whitespace, and write with line number
    for line_num, word in enumerate(infile, start=1):
        word = word.strip()  # Remove newline and extra spaces
        if word:  # Only write non-empty lines
            writer.writerow([line_num, word])
        else:
            print(f"Skipped empty or invalid line at line number {line_num}")

print(f"Converted {input_file} to {output_file}")
