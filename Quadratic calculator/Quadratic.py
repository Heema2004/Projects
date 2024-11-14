from cmath import sqrt
def main():
    a = int(input("please enter the value of a for a quadratic equation of the form ax^2 + bx +c: "))
    b = int(input("please enter the value of b for a quadratic equation of the form ax^2 + bx +c: "))
    c = int(input("please enter the value of c for a quadratic equation of the form ax^2 + bx +c: "))
    quadratic(a,b,c)
def quadratic(a,b,c):
    x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2-4*a*c))/(2*a)
    print("The values for X are, X1 = ",x1,", X2 = ", x2)
main()
