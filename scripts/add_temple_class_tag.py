import os
import re
import yaml

# Function to read markdown file and extract metadata
def read_markdown(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    metadata_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
    if metadata_match:
        metadata = yaml.safe_load(metadata_match.group(1))
        return metadata, content
    return None, content

# Function to write metadata back to the markdown file
def write_markdown(file_path, metadata, content):
    new_metadata = yaml.dump(metadata, sort_keys=False)
    new_content = re.sub(r'---\n(.*?)\n---', f'---\n{new_metadata}---', content, flags=re.DOTALL)
    with open(file_path, 'w') as file:
        file.write(new_content)

# Function to process markdown files in a directory
def process_markdown_files(directory):
    pattern = re.compile(r'^(ENGR|ECE)\s\d{4}')
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            metadata, content = read_markdown(file_path)
            if metadata and 'description' in metadata:
                match = pattern.match(metadata['description'])
                if match:
                    tag = match.group(0).lower().replace(' ', '-')
                    if 'tags' in metadata:
                        if tag not in metadata['tags']:
                            metadata['tags'].append(tag)
                    else:
                        metadata['tags'] = [tag]
                    write_markdown(file_path, metadata, content)

# Directory containing markdown files
directory = './src/content/blog'

# Process the markdown files
process_markdown_files(directory)
