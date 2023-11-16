
"""
Creator: Jaysen
"""

def jaysen_showers(jaysen, gpa):
    
    shower = "clean"

    if jaysen not in shower:
        gpa += 0.2

    return round(gpa, 2)

def main():

    name = input("Enter Your Name: ")
    gpa = float(input("Enter Your Current GPA (4.0 Scale): "))

    print("Hi, ", name, " ,based on your current trajectory in life, your current GPA is: ", jaysen_showers(name, gpa), sep="")
if __name__ == "__main__":
    main()
