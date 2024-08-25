def count_lines(file_path):
    try:
        with open(file_path) as file:
            lines = file.readlines()
            line_count = len(lines)
    except FileNotFoundError:
        print("NO FILE FOUND!")
    return line_count

def replace_tabs(file_path):
    try:
        with open(file_path) as file:
            contents = file.read()
            contents = contents.replace("\t"," ")

        with open(file_path,'w') as file:
            file.write(contents)
    except FileNotFoundError:
        print("File Not Found")

def save_columns(file_path, columns):
    try:
        selected_columns = []
        with open(file_path) as file:
            for line in file:
                words = line.split()

                selected_columns.append(words[columns])

    except FileNotFoundError:
        print("File Not Found")
    return selected_columns

def write_column(column, file_name):
    try:
        with open(f"{file_name}.txt",'w') as file:

            for line in column:
                file.write(line + '\n')
    except FileNotFoundError:
        print("File Not Found")

def merge_file(file1, file2,new_file):
    try:
        with open(file1) as f1, open(file2) as f2, open(new_file, 'w') as new_file:
            for line1, line2 in zip(f1, f2):
                new_file.write(f"{line1.strip()}\t{line2.strip()}\n")
    except FileNotFoundError:
        print("No File Found")


def first_N_lines(file_path, number):
    try:
        with open(file_path) as file:
            lines = []
            n=0
            for line in file:
                lines.append(line)
                n+=1
                if n  == number:
                    break
    except FileNotFoundError:
        print("No File Found")
    return lines

def last_N_lines(file_path, number):
    try:
        with open(file_path) as file:
            lines = file.readlines()  # Read all lines into memory
            return lines[-number:]    # Return the last `number` lines
    except FileNotFoundError:
        print("No File Found")
    return lines

def split_file(file_path, num_parts):
    try:
        with open(file_path) as file:
            lines = file.readlines()

            total_lines = len(lines)
            lines_per_part = total_lines // num_parts
            extra_lines = total_lines % num_parts

            start = 0
            for i in range(num_parts):
                end = start + lines_per_part + (1 if i < extra_lines else 0)
                part_lines = lines[start:end]
                part_filename = f"{file_path}_part_{i+1}.txt"
                with open(part_filename, 'w') as part_file:
                    part_file.writelines(part_lines)
                start = end

            print(f"File split into {num_parts} parts successfully.")
    except FileNotFoundError:
        print("File not found.")

def sort_by_third_column(file_path, output_file):
    try:
        with open(file_path) as file:
            lines = file.readlines()

            # Split each line into components, sort by the third column (index 2) in descending order
            sorted_lines = sorted(lines, key=lambda x: int(x.split()[2]), reverse=True)

            # Write the sorted lines to a new file
            with open(output_file, 'w') as out_file:
                out_file.writelines(sorted_lines)

            print(f"File sorted by the third column in descending order and saved as {output_file}.")

    except FileNotFoundError:
        print("File not found.")
    except IndexError:
        print("One or more lines in the file do not have a third column.")
    except ValueError:
        print("The third column contains non-integer values that cannot be sorted.")

from collections import Counter

def count_and_sort_by_frequency(file_path):
    try:
        with open(file_path) as file:
            first_column = [line.split()[0] for line in file]

            # Use Counter to count the frequency of each unique string in the first column
            frequency_counter = Counter(first_column)

            # Sort by frequency in descending order
            sorted_frequencies = sorted(frequency_counter.items(), key=lambda x: x[1], reverse=True)

            # Print the results
            for word, count in sorted_frequencies:
                print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found.")
    except IndexError:
        print("One or more lines in the file do not have a first column.")

file_path = "C:\\Users\\Hakim Hisham\\Downloads\\popular-names.txt"

print("Number of lines:",count_lines(file_path))
replace_tabs(file_path)
print("Successfully replace tabs with a space!")
col1 = save_columns(file_path, 0)
col2 = save_columns(file_path , 1)
write_column(col1, "col1")
write_column(col2, "col2")
print("Successfully saved first and second columns in text file!")
merge_file("col1.txt","col2.txt","merged_file.txt")
print("Successfully merged col1.txt and col2.txt in text file!")
print("".join(first_N_lines("merged_file.txt", 10)))
print("".join(last_N_lines("merged_file.txt", 10)))
split_file("merged_file.txt", 5)
sort_by_third_column(file_path, "sorted_file")
count_and_sort_by_frequency(file_path)

