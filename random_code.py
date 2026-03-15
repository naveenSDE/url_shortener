import string
import random
def code():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))