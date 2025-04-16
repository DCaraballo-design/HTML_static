import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    # Grab the basepath from the first CLI argument or default to "/"
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    if not basepath.endswith("/"):
        basepath += "/"

    print(f"Base path set to: {basepath}")

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
                generate_page(markdown_path, template_path, html_path, basepath)

    print("All pages generated successfully!")


if __name__ == "__main__":
    main()
