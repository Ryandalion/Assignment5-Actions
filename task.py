def firstrun():
    return "success"


def compute_area(radius):
    area = 3.14 * radius * radius
    return area


def compute_first_last(sentence):
    first_element = sentence[0]
    last_element = sentence[-1]
    return first_element, last_element


def compute_days(date_1, date_2):
    difference = date_2 - date_1
    return difference.days


