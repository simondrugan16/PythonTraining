age: int

# age = "dasda"
age = 20
def police_check(age: int) -> bool:
    if age > 16:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print(police_check(age))
