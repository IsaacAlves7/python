# Python Password Generator
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "#&%[]{}()Ç~^\|*;/,._-@ç"
all = lower + upper + numbers + symbols
password = "".join(random.sample(all,length))
print(password)

# Output: 4-80GTktY9pU)HQz
