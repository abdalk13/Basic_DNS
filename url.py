#-----------------------------------------
# URL formatting function (YOUR CODE)
#-----------------------------------------
def formatURL_first(url_in:str)->bytes:
    url_bin=''
    urlsplited=url_in.split('.')
    for numbers in urlsplited:
        url_bin += chr(len(numbers)) + numbers
    url_bin+= chr(0)
    return url_bin.encode(encoding='utf_8')

    # your code goes here
Answer1=formatURL_first('bbc.co.uk')
Answer2=formatURL_first('facebook.com')
Answer3=formatURL_first('mixteco.utm.mx')
Answer4=formatURL_first('eluniversal.com.mx')
print("       The questions at the beginning", "\n",Answer1 )
print(Answer2)
print(Answer3)
print(Answer4, "\n")
#-----------------------------------------------------------
# Lab 5.1.2: formatNameField
#-----------------------------------------------------------

#it will be the same as 5.1 so we can just call the function
def formatURL_second(url_in:str)->bytes:
    url_bin=formatURL_first(url_in) #here we called the old function
    unicodezero=chr(0) #The chr() function returns the character that represents the specified unicode, so use ite for 1 adn 0
    unicodeone=chr(1)
    url_bin=url_bin.decode('utf-8')+unicodezero+unicodeone+unicodezero+unicodeone # we re take the urlformat and re and add with chr(0) and chr(1) 
    return url_bin.encode(encoding='utf_8')

#-------------------------------------------------------------
#-------------------------------------------------------------

#The answer of questions in the pdf
Answer1=formatURL_second('bbc.co.uk')
Answer2=formatURL_second('facebook.com')
Answer3=formatURL_second('mixteco.utm.mx')
Answer4=formatURL_second('eluniversal.com.mx')
print("       The questions at the beginning", "\n",Answer1 )
print(Answer2)
print(Answer3)
print(Answer4, "\n")
#---------------------------------------------------------------
#---------------------------------------------------------------


#----------------------------------------------------------------
#----------------------------------------------------------------
#---------------   Message Assembly 5.2   -----------------------
#----------------------------------------------------------------
def the12_bytes(url: bytes) -> bytes:
    
    unicodezero = chr(0).encode(encoding='utf_8')
    unicodeone= chr(1).encode(encoding='utf_8')
    unicode14= chr(14).encode(encoding='utf_8')
    unicode16= chr(16).encode(encoding='utf_8')

    url_in= bytes()
    url_in= url_in + unicode14 + unicode16 +unicodeone + unicodezero + unicodezero  + unicodeone + unicodezero+ unicodezero + unicodezero+ unicodezero + unicodezero + unicodezero
    
    return   url_in + url
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------


# Answer question 5.2
#----------------------------------------------
answer1=(the12_bytes(formatURL_second("oru.se")))
answer2=(the12_bytes(formatURL_second("bbc.co.uk")))
answer3=(the12_bytes(formatURL_second("facebook.com")))
answer4=(the12_bytes(formatURL_second("mixteco.utm.mx")))
answer5=(the12_bytes(formatURL_second("eluniversal.com.mx")))

print("    The questions 5.2" )
print("\n",answer1)
print(answer2)
print(answer3)
print(answer4, "\n")

