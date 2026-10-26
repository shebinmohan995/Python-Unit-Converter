

#UNIT CONVERSION OF LENGTH
category=input("ENTER CATEGORY(length,weight,speed):")
if category=="length":

    num=float(input("ENTER THE VALUE:"))
    from_unit=input("ENTER THE UNIT:").lower().strip()
    to_unit=input("ENTER THE UNIT:").lower().strip()

    def length_converter(num,from_unit,to_unit):
        conversion={"m":1,
                    "km":1000,
                    "cm":0.01,
                    "mm":0.001}
        #CONVERSION
        value=num*conversion[from_unit]
        result=value/conversion[to_unit]
        return result
    print(length_converter(num,from_unit,to_unit))

#UNIT CONVERSION OF WEIGHT

elif category=="weight":
    num=float(input("ENTER THE WEIGHT:"))
    from_weight=input("ENTER THE UNIT:").lower().strip()
    to_weight=input("ENTER THE UNIT:").lower().strip()

    def weight_converter(num,from_weight,to_weight):
        conversion={"kg":1000,
                     "g":1,
                     "mg":0.001,
                     "lbs":453.59,
                     "oz":28.35}
        #CONVERSION
        value=num*conversion[from_weight]
        result=value/conversion[to_weight]
        return result
    print(weight_converter(num,from_weight,to_weight))

#SPEED CONVERSION
elif category=='speed':
    speed=float(input("ENTER THE SPEED:"))
    unit_from=input("ENTER THE UNIT:").lower().strip()
    unit_to=input("ENTER THE UNIT:").lower().strip()
    def speed_conversion(speed,unit_from,unit_to):
        conversion={"m/s":1,
                    "km/h":0.277778,
                    "mph":0.44704,
                    "ft/s":0.3048}
        #CONVERSION
        value=speed*conversion[unit_from]
        result=value/conversion[unit_to]
        return result
    print(speed_conversion(speed,unit_from,unit_to))
else:
    print("INVALID CATEGORY")




