"""Example of a Web Scraper using Regular Expressions"""

# Dependencies
import re

# Data
text_1 = "crypto-bot that is trading Bitcoin and other currencies"
text_2 = "cryptographic encryption methods that can be cracked easily with quantum computers"

# One-Liner
pattern = re.compile("crypto(.{1,30})coin")

# Result
print(pattern.match(text_1))
print(pattern.match(text_2))