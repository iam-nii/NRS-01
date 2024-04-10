import customtkinter as c
import winsound
def validate_float(input_string):
    """Validate the input string as a floating point number."""
    try:
        if input_string == ".":
            return True
        float(input_string)
        return True
    except ValueError:
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        return False
