#!/usr/bin/env python3
# Jacob Sturges, ID: 112918980
import math
def main():
    print("Welcome to my position/velocity calculator!")
    const = float(input("Enter the constant term: "))  # User enter constant term
    const = newRound(const)                             # newRound method invoked by constant variable
    lin = float(input("Enter the linear term: "))
    lin = newRound(lin)
    quad = float(input("Enter the quadratic term: "))
    quad = newRound(quad)
    print("The position equation is " + str(quad) + "t^2" + " + " + str(lin) + "t " + "+ " + str(const))  # Str casting
    derivQuad = float((2*quad))                                                     # Derivative concerning t^2 (quad)
    print("The velocity equation is " + str(derivQuad) + "t " + "+ " + str(lin))
    time = float(input("Enter a time to calculate: "))                              # User enters time
    rawPosition = (quad*(time ** 2) + (lin * time) + const)                         # Position formula
    position2 = newRound(rawPosition)                                               # newRound method on position
    print("The position at the time " + str(time) + " is " + str(position2))
    velocity = ((derivQuad*time) + lin)                                             # Velocity formula
    velocity = newRound(velocity)                                                   # newRound method on velocity
    print("The velocity at the time " + str(time) + " is " + str(velocity))
    print("Thank you!")


def newRound(decimalValue):  # This is a method I created to round any number to the nearest 3 decimal places.
    rawPosition = decimalValue
    temp = 1000 * rawPosition
    temp = int(temp)            # Truncate
    temp = temp / 1000.0
    return temp                 # Return


if __name__ == '__main__':
    main()
