#write a program that reads in meters and shows in centimeters and millimeters.
#Meters converter
Meters = int(input('Write the number you would like to converter'))
Question = str(input('Write (Centi) for Centimeters or (Milli) for Millimeters.'))
Centimeters = (Meters*100)
Millimeters = (Meters*1000)
print(Millimeters, Centimeters)
