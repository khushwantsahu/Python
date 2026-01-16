#convert temprature , currency, distance

#convert temprature 
t = float(input("Enter temprature in celcius = "))

print("celcius to ferenhite :")
res1 = (t*9/5)+32
print("    =",res1,"F")

print("celcius to kelvin :")
res2 = t + 273.15
print(f"    = {res2:.2f} K")
print()


#convert currency
r = int(input("Enter indian currency ammount = "))
print("rupee to doller :")
res3 = r * 0.011
print(f"    = {res3:.2f} $")
print()


#calculate distance
s = float(input("Enter the average speed(kmph) = "))
t1 =float(input("total time to reach(in hour) = "))
d = s * t1
print("distance : ")
print(f"     = {d} km")