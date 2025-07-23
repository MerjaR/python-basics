# Filters out any letters in forbidden from string (list comprehension)
def filter_forbidden(string: str, forbidden: str):
    remove_forbidden = "".join([character for character in string if character not in forbidden])
    return remove_forbidden
