import phonenumbers
from phonenumbers import timezone,geocoder,carrier
from sys import argv,exit

def phone(x):
    phoneNumber = phonenumbers.parse(x)
    timeZone = timezone.time_zones_for_number(phoneNumber)
    Carrier = carrier.name_for_number(phoneNumber, 'en')
    Region = geocoder.description_for_number(phoneNumber, 'en')
    possible = phonenumbers.is_possible_number(phoneNumber)
    valid = phonenumbers.is_valid_number(phoneNumber)



    print(f''' \n
    Information    
                                      
         Time-Zone        :   {timeZone}
         Region           :     {Region}
         Carrier          :     {Carrier}
         Possiblity       :     {possible}
         Validaity        :     {valid}
    
    ''')




def main():
    x=argv[1]
    phone(x)


if __name__ == "__main__":
    try:
        main()
    except:
        print("\n Error happened . Exiting")
        exit()

