import random

password = ""

def generatePassword(passwordLength, passwordType):
    global password
    if passwordType == 1:
        characters = "1234567890"
    elif passwordType == 2:
        characters = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM"
    elif passwordType == 3:
        characters = "1234567890qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM"
    elif passwordType == 4:
        characters = "1234567890qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM~`@#$%^&*()-_+={[}]|\\;:\"\',<.>/?"
    else:
        return None
    for _ in range(passwordLength):
        password += random.choice(characters)
    return password
if __name__ == "__main__":
   pass
