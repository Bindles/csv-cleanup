import csv

# Define the input and output file names
input_csv_file = 'input.csv'
output_csv_file = 'output.csv'

# Open the input and output CSV files
with open(input_csv_file, 'r', newline='') as input_file, open(output_csv_file, 'w', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file, quoting=csv.QUOTE_MINIMAL)

    # Loop through each row in the input CSV
    for row in csv_reader:
        if len(row) >= 3:  # Assuming the third column contains the Body (HTML)
            # Wrap the content in double quotes
            row[2] = f'"{row[2]}"'

        # Write the modified row to the output CSV
        csv_writer.writerow(row)

print("CSV processing complete. Modified data saved to output.csv.")
