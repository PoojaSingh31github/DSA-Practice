import re

# Regex patterns
roman = r"^(M){0,3}(CM)?(CD|D)?(C){0,3}(XC)?(XL|L)?(X){0,3}(IX)?(IV|V)?(I){0,3}$"
phone = r"^\+?[1-9]\d{1,14}$"
email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
ipv4 = r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})$"
url = r"^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

# Sample inputs
roman_input = "MMMCMXCIX"  # Valid Roman numeral
phone_input = "+12345678901"  # Valid phone number
email_input = "example@example.com"  # Valid email address
ipv4_input = "192.168.1.1"  # Valid IPv4 address
url_input = "https://www.example.com"  # Valid URL

# Check and print results
print(bool(re.match(roman, roman_input)))  # True
print(bool(re.match(phone, phone_input)))  # True
print(bool(email.match(email_input)))  # True
print(bool(re.match(ipv4, ipv4_input)))  # True
print(bool(re.match(url, url_input)))  # True
