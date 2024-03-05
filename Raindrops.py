def convert(number):
    string=""
    if number%3==0:
        string="Pling"
    if number%5==0:
        string=string+'Plang'
    if number%7==0:
        string=string+"Plong"
    if number%7!=0 and number%5!=0 and number%3!=0:
        string=str(number)
    return string
