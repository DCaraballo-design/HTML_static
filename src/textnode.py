from enum import Enum

class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"

class TextNode:(TEXT,TEXT_TYPE,URL):
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type  
        # URL is optional
        self.url = url if url else None

    def__eq__(self, other):
        if isinstance(other, TextNode):
            return True

    def __repr__(self):
        return f"TextNode(text={self.text}, text_type={self.text_type}, url={self.url})"