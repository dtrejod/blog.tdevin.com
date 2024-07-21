import os
import yaml
from yaml.dumper import SafeDumper

class CustomDumper(SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(CustomDumper, self).increase_indent(flow, False)

def update_tags_in_markdown_files(directory, action, tags):
    """
    Update tags in markdown files within a specified directory.

    :param directory: Path to the directory containing markdown files.
    :param action: 'add' or 'remove' to specify the action on tags.
    :param tags: List of tags to add or remove.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            # Find the start and end of the front matter
            if lines[0].strip() == '---':
                end_index = 1
                while end_index < len(lines) and lines[end_index].strip() != '---':
                    end_index += 1
                
                # Load the front matter as a dictionary
                front_matter = yaml.safe_load(''.join(lines[1:end_index]))
                
                # normalize to all lowercase
                front_matter['tags'] = [tag.lower() for tag in front_matter.get('tags', [])]

                # Update the tags
                if action == 'add':
                    front_matter['tags'] = list(set(front_matter.get('tags', []) + tags))
                elif action == 'remove':
                    front_matter['tags'] = [tag for tag in front_matter.get('tags', []) if tag not in tags]
                
                # Update the file content with the new front matter
                new_front_matter = yaml.dump(front_matter, Dumper=CustomDumper, default_flow_style=False, sort_keys=False)
                new_content = '---\n' + new_front_matter + '---\n' + ''.join(lines[end_index+1:])
                
                # Write the updated content back to the file
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)

# Example usage
directory_path = "./src/content/blog"

# Tags to add or remove
tags_to_add = []
tags_to_remove = ['programming']

update_tags_in_markdown_files(directory_path, 'add', tags_to_add)
update_tags_in_markdown_files(directory_path, 'remove', tags_to_remove)

