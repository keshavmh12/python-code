import json
import re
filename ="data.txt"
def load_password():
    with open(filename,"r") as f:
        return json.load(f)

