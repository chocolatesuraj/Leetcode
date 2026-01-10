class Codec:
    def __init__(self):
        self.base="http:/tinyurl.com/"
        self.encode_map={}
        self.decode_map={}

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encode_map:
            self.encode_map[longUrl]=str(len(self.encode_map)+1)
            self.decode_map[str(len(self.encode_map))]=longUrl
            return self.base + self.encode_map[longUrl]
        else:
            return self.base + self.encode_map[longUrl]

        """Encodes a URL to a shortened URL.
        """
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_map[shortUrl.strip(self.base)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
