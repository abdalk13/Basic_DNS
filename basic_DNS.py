
from socket import AF_INET, SOCK_DGRAM, socket

from lab5 import formatURL_second, the12_bytes


#DNS_server = '192.168.1.90'
DNS_server = '8.8.8.8'
DNS_port=53
timeout=10
#-----------------------------------------
# Socket initialization
#-----------------------------------------
 
clientsocket = socket(AF_INET, SOCK_DGRAM)      #\x01\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x03bbc\x02co\x02uk\x00\x00\x01\x00\x01'
                                                #\xff\x9b\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x03bbc\x02co\x02uk\x00\x00\x01\x00\x01
clientsocket.settimeout(timeout)
  
DNS_port = int(DNS_port)
urlToQuery='www.bbc.co.uk'
formatted_url=formatURL_second(urlToQuery)
query_to_DNS = the12_bytes(formatted_url)
#-----------------------------------------
# Question assembly (YOUR CODE)
#-----------------------------------------

try:
    clientsocket.sendto(query_to_DNS,(DNS_server, DNS_port))
    message, address = clientsocket.recvfrom(1024)
    #-----------------------------------------
    #-----------------------------------------
    
    #-----5.4---------------------------------
    #-----------------------------------------
    
    messagelength= len(message)    
    # the message will be 230 long there we can find 12 bytes from the header
    #  and the formatted url which in our case its the function formatURL_second and it will also be  12 bytes
    # then we have the type and ip and there we can find the ip we are communicating with.
    # we can give "number" the value 12+ len (formatted_url) to skip go through the head message, 

    number=12+ len(formatted_url)
    #while the number is smaller than what the message length is
    while number < messagelength:             
        if number ==  (messagelength-1):
            break
        number +=1    
        if message[number] == 0 and message[number + 1] == 4:
            ip = "" #ip is an empty str
            # We want to find the ip by going through a loop there is start from i is equal to number +2
            # while the message (number +1) is equal to 4 and message(number)=0
            i=number + 2
            # we goes in loop between i to +4 because the ip is the 4 next digits
            for i in range((i) , (number + 6)):
                # we add the values to to our ip
                ip += str(message[i])
                ip += "."
            # remove the last dot we have
            ip = ip[:-1]
            print("IP -->",ip)
       
except:
#-----------------------------------------
#-----------------------------------------
    print('A timeout has occured, no reply from the DNS server')

  
     
 
