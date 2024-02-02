import string
import random


class Codec:
    def __init__(self):
        self.link = {}
        self.N = 5

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        short = "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(self.N)
        )
        short_url = f"https://tinyurl.com/{short}"
        self.link[short_url] = longUrl
        return short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.link[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
