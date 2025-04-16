import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    """
    Generates an HTML page from a markdown file using a template.

    Args:
        from_path (str): Path to the markdown file.
        template_path (str): Path to the HTML template file.
        dest_path (str): Path to save the generated HTML file.
        basepath (str): The base path for the site.
    """
    print(f" * {from_path} {template_path} -> {dest_path}")

    # Read the markdown file
    with open(from_path, "r", encoding="utf-8") as from_file:
        markdown_content = from_file.read()

    # Read the template file
    with open(template_path, "r", encoding="utf-8") as template_file:
        template = template_file.read()

    # Convert markdown to HTML
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    # Extract the title from the markdown
    title = extract_title(markdown_content)

    # Replace placeholders in the template
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # Replace href and src paths with the basepath
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    # Ensure the destination directory exists
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    # Write the final HTML to the destination file
    with open(dest_path, "w", encoding="utf-8") as to_file:
        to_file.write(template)


def extract_title(md):
    """
    Extract the H1 header (title) from a markdown string.

    Args:
        md (str): The markdown string.

    Returns:
        str: The extracted title.

    Raises:
        ValueError: If no H1 header is found.
    """
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()  # Remove the # and any leading/trailing whitespace
    raise ValueError("no title found")
