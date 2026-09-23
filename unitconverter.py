def km_to_miles(km):
    return km * 0.621

def kg_to_pounds(kg):
    return kg * 2.2 

def celsius_to_farenheit(celsius):
    return (celsius * 9/5 + 32)
while True:
    print("1.Length converter")
    print("2.Weight converter")
    print("3.Temperature converter")
    print("4.Exit")
    option = input("choose an option ").strip()
    if option == "4":
        print("goodbye")
        break
    elif option == "1":
        while True:
            conversion = input("kilometer to miles or 0 to go back: ").strip()
            if conversion == "0":
                break
            try:
                conversion = int(conversion)
            except:
                print("wrong entry")   
                continue  
            print(f"{conversion} km = {round(km_to_miles(conversion), 2)} miles")
    elif option == "2":
        while True:            
            conversionii = input("kilogram to pounds or 0 to go back: ").strip()
            if conversionii == "0":
                break
            try:
                conversionii = int(conversionii)
            except:
                print("Wrong entry")
                continue    
            print(f"{conversionii} kg = {round(kg_to_pounds(conversionii), 2)} pounds")
    elif option == "3":
        while True:
            conversioniii = input("celsius_to_farenheit or 0 to go back: ").strip()
            if conversioniii == "0":
                break
            try:
                conversioniii = int(conversioniii)
            except:
                print("wrong entry")
                continue    
            print(f"{conversioniii} degree celsius = {round(celsius_to_farenheit(conversioniii), 2)} farenheit")
    else:
        print("invalid input")