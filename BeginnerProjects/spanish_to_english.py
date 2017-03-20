## This program translates spanish numbers to english numbers.

Numbers = {'uno': 'one',\
           'dos': 'two',\
           'tres': 'three',\
           'cuatro': 'four',\
           'cinco': 'five',\
           'seis': 'six',\
           'siete': 'seven',\
           'ocho': 'eight',\
           'nueve': 'nine',\
           'diez': 'ten',\
           'once': 'eleven',\
           'doce': 'twelve',\
           'trece': 'thirteen',\
           'catorce': 'fourteen',\
           'quince': 'fifteen',\
           'dieciseis': 'sixteen',\
           'diecisiete': 'seventeen',\
           'dieciocho': 'eighteen',\
           'diecinueve': 'nineteen',\
           'veinte': 'twenty',\
           'treinta': 'thirty',\
           'cuarenta': 'fourty',\
           'cincuenta': 'fifty',\
           'sesenta': 'sixty',\
           'setenta': 'seventy',\
           'ochenta': 'eighty',\
           'noventa': 'ninety',\
           'cien': 'hundred',\
           'y': ''\
          }


def translateNumber(n):
    """This function converts the value of n into corresponding
    spanish words. It accepts only 'string' values of n."""
    if type(n) != str:
        return None
    else:
        translation = ""
        word = ""
        for c in n:
            if c != ' ':
                word += c
            elif word in Numbers:
                translation += Numbers[word] + " "
            else:
                translation += word + " "
        return translation
    
def convert():
    n = input("Enter the number in spanish : ")
    if translateNumber(n) == None:
        print("Invalid input.\nEnter string value only.")
        convert()
    else:
        print("In english it is" + translateNumber(n))
