import sys
if len(sys.argv)!=5:
    print("usage python internet.py <plan_name> <speed> <validity> <price>")
    sys.exit(1)
plan_name=sys.argv[1]
speed=sys.argv[2]
validity=sys.argv[3]
price=sys.argv[4]

print("___plan summary___")
print("Plan name",plan_name)
print("Speed",speed)
print("Validity",validity)
print("Price",price)