# Remove non-alphanumeric characters from a Python string

import re

my_str = 'bobby !hadz@ com 123'

# ✅ Remove all non-alphanumeric characters from string

new_str = re.sub(r'[\W_]', '', my_str)
print(new_str)  # 👉️ 'bobbyhadzcom123'

# -----------------------------------------------

# ✅ Remove all non-alphanumeric characters from string,
#  preserving whitespace

new_str = re.sub(r'[^\w\s]', '', my_str)
print(new_str)  # 👉️ 'bobby hadz com 123'