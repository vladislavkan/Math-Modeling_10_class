def gg (year=2000):
    """функция которая определяет является 
    ли год високосным или нет по заданной дате.
    """
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print("обычный")
    else:
        print("високосный")
gg(2004)


