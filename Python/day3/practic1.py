#creating reusable function of previous practices

def main():
    x = get_int("Enter Number = ")
    y = get_int("Enter Number = ")
    CLI_Calculator(x,y)

    c = get_int("Enter temprature('C) = ")
    cel_to_fer(c)

    cel_to_kel(c)

    s = get_int("Enter the average speed(kmph(default = 60)) = ")
    t = get_int("total time to reach(in hour (default = 1h)) = ")
    calculate_des(s,t)
    


def get_int(prompt):
    return float(input(prompt))

def CLI_Calculator(x,y):
    print("x + y = ",(x+y))
    print("x - y = ",(x-y))
    print("x * y = ",(x*y))
    print("x / y = ",(x/y))
    print("x % y = ",(x%y))


def cel_to_fer(c = 30):
    print("celcius to ferenhite(default = 30'C) :")
    res = (c*9/5)+32
    print("    =",res,"F")

def cel_to_kel(c = 30):
    print("celcius to kelvin (default = 30'C) :")
    res = c + 273.15
    print(f"    = {res:.2f} K")

def rup_to_dol(r = 1):
    print("rupee to doller :")
    res = r * 0.011
    print(f"    = {res:.2f} $")

def calculate_des(s=60,t=1):
    d = s * t
    print("distance : ")
    print(f"     = {d} km")
main()