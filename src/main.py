import shutil
import os
from textnode import TextNode, TextType


def copy_static_to_public(src_dir, dest_dir):
    """
    Recursively copies all contents from the source directory to the destination directory.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)  # Create the destination directory if it doesn't exist

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        print(f"Copying {src_path} to {dest_path}")

        if os.path.isdir(src_path):
            # If the item is a directory, recursively copy its contents
            copy_static_to_public(src_path, dest_path)
        else:
            # If the item is a file, copy it to the destination
            shutil.copy2(src_path, dest_path)


def copy_images_to_public(src_images_dir, dest_images_dir):
    """
    Copies all images from the source images directory to the destination images directory.
    """
    if not os.path.exists(dest_images_dir):
        os.makedirs(dest_images_dir)  # Create the destination images directory if it doesn't exist

    for item in os.listdir(src_images_dir):
        src_path = os.path.join(src_images_dir, item)
        dest_path = os.path.join(dest_images_dir, item)

        if os.path.isfile(src_path) and item.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')):
            # Copy only image files
            shutil.copy2(src_path, dest_path)


# Example usage in the main function
def main():
    # Define source and destination directories relative to the script's location
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Get the directory of the current script
    src_dir = os.path.join(base_dir, "static")
    dest_dir = os.path.join(base_dir, "public")
    src_images_dir = os.path.join(src_dir, "images")
    dest_images_dir = os.path.join(dest_dir, "images")
    

    # Clear the public directory
    clear_public(dest_dir)

    # Copy contents from static to public
    copy_static_to_public(src_dir, dest_dir)

    # Copy images to the public/images folder
    copy_images_to_public(src_images_dir, dest_images_dir)

    print(f"Copied contents from {src_dir} to {dest_dir}")
    print(f"Copied images from {src_images_dir} to {dest_images_dir}")


def clear_public(public_dir):
    """
    Ensures the public directory and its images subdirectory exist,
    and clears the contents of the public directory.
    """
    # Ensure the public directory exists
    if not os.path.exists(public_dir):
        os.makedirs(public_dir)

    # Ensure the images subdirectory exists
    image_folder = os.path.join(public_dir, "images")
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    # Clear the contents of the public directory
    for filename in os.listdir(public_dir):
        file_path = os.path.join(public_dir, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path) and filename != "images":
            shutil.rmtree(file_path)


main()