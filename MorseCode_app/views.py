from django.shortcuts import render
from django.http import HttpResponse

MORSE_CODE_DICT = { ' ':'/', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}


def index(request):
    return render(request,'MorseCode_app/index.html')
    
def Txt_to_Morse(request):
    txt = request.GET['msg']
    code = [MORSE_CODE_DICT[i.upper()] + ' ' for i in txt if i.upper() in MORSE_CODE_DICT.keys()]
    morse=''.join(code)
    return render(request,'MorseCode_app/index.html',{'morse':morse})

def Morse_to_Txt():
    txt = input('Enter Morse to Convert to Text: ')
    code = [k for i in txt.split() for k,v in MORSE_CODE_DICT.items() if i==v]
    newtxt = ''.join(code)
    print(newtxt)