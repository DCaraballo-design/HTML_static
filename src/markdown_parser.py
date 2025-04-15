def extract_title(markdown):
    """
    Extract the H1 header (title) from a markdown string.

    Args:
        markdown (str): The markdown string to extract the title from.

    Returns:
        str: The extracted title.

    Raises:
        ValueError: If no H1 header is found in the markdown.
    """
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):  # Check for a single # followed by a space
            return line[2:].strip()  # Remove the # and leading/trailing whitespace
    raise ValueError("No H1 header found in the markdown")
