import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages...")
    if not os.path.exists(dir_path_content):
        print(f"Content directory '{dir_path_content}' does not exist.")
        return

    # Walk through the content directory recursively
    for root, _, files in os.walk(dir_path_content):
        for filename in files:
            if filename.endswith(".md"):  # Process only markdown files
                markdown_path = os.path.join(root, filename)
                # Generate the relative path for the output HTML file
                relative_path = os.path.relpath(markdown_path, dir_path_content)
                html_path = os.path.join(dir_path_public, relative_path).replace(".md", ".html")

                print(f"Generating page from {markdown_path} to {html_path}...")
                generate_page(markdown_path, template_path, html_path)

    print("All pages generated successfully!")


if __name__ == "__main__":
    main()
