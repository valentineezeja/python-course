## Method Resolution Order
This the order which Python chooses the order of methods in a multi-inheritance scenario

## Syntax:
Class A ...

Class B ...

Class C ...

Class D(B, C)  #MULTIPLE INHERITANCE

You can find the MRO using the methods below:

print(D.__mro__)
print(D.mro())
help(D)