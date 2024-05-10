# def insert_newlines_in_file(file_path, keys_list):
#     # Read the contents of the file
#     with open(file_path, 'r', encoding='utf-8') as file:
#         lines = file.read()

#     modified_lines = []

#     # Iterate through each line split by newline
#     for line in lines.split('\n'):
#         line_modified = False
        
#         # Check for each key in the line
#         for key in keys_list:
#             if key in line:
#                 print("key:",key)
#                 print("line:",line)
#                 print("\n")
        
#                 # If the key is found in the line, add a newline after the key
#                 line = line.replace(key, key + '\n', 1)
#                 print("modifyed line:",line)
#                 print("\n\n")
#                 line_modified = True
#                 break
        
#         # If the line was not modified, append the original line
#         if not line_modified:
#             modified_lines.append(line)

#     # Write the modified lines back to the original file
#     with open("modified.txt", 'w', encoding='utf-8') as file:
#         file.write('\n'.join(modified_lines))

# # Example usage:
# file_path = 'textt.txt'

# keys_list = [
#     "Botanical name",
#     "Family",
#     "Synonyms",
#     "Common names",
#     "Vernacular names",
#     "Description of the plant",
#     "Herbarium specimen number",
#     "Habitat and geographical distribution",
#     "Plant material of interest",
#     "Other parts used",
#     "Definition of plant material of interest",
#     "Ethnomedical uses",
#     "Biological and pharmacological activities",
#     "Clinical data",
#     "Chemical constituents",
#     "Test for identity and purity",
#     "Chromatographic fingerprints",
#     "Macroscopy",
#     "Microscopy",
#     "Powdered plant material",
#     "Therapeutic actions",
#     "Therapeutic indications",
#     "Safety data",
#     "Precautions for use",
#     "Adverse effects",
#     "Contraindications",
#     "Dosage and dosage forms",
#     "Storage",
#     "References"
# ]

# insert_newlines_in_file(file_path, keys_list)


def insert_newlines_in_file(file_path, keys_list):
    # Read the contents of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read()

    modified_lines = []

    # Iterate through each line in the file
    for line in lines.split('\n'):
        modified_line = line
        
        # Iterate through each key in the keys_list
        for key in keys_list:
            # Find all occurrences of the key in the line
            start_idx = 0
            while True:
                # Find the next occurrence of the key starting from start_idx
                key_idx = modified_line.find(key, start_idx)
                
                if key_idx == -1:
                    break  # No more occurrences of key in this line
                
                # Insert '\n' before and after the key
                modified_line = (
                    modified_line[:key_idx] + '\n' + key + '\n' + modified_line[key_idx + len(key):]
                )
                
                # Move start_idx past the inserted key and '\n' to avoid infinite loop
                start_idx = key_idx + len(key) + 2

        # Append the modified line (split into multiple lines) to modified_lines
        modified_lines.extend(modified_line.split('\n'))

    # Write the modified lines back to the original file
    with open("modified.txt", 'w', encoding='utf-8') as file:
        file.write('\n'.join(modified_lines))

# Example usage:
file_path = 'textt.txt'

keys_list = [
    "Botanical name",
    "Family",
    "Synonyms",
    "Common names",
    "Vernacular names",
    "Description of the plant",
    "Herbarium specimen number",
    "Habitat and geographical distribution",
    "Plant material of interest",
    "Other parts used",
    "Definition of plant material of interest",
    "Ethnomedical uses",
    "Biological and pharmacological activities",
    "Clinical data",
    "Chemical constituents",
    "Test for identity and purity",
    "Chromatographic fingerprints",
    "Macroscopy",
    "Microscopy",
    "Powdered plant material",
    "Therapeutic actions",
    "Therapeutic indications",
    "Safety data",
    "Precautions for use",
    "Adverse effects",
    "Contraindications",
    "Dosage and dosage forms",
    "Storage",
    "References"
]

insert_newlines_in_file(file_path, keys_list)






