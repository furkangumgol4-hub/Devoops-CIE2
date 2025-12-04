import sys

if len(sys.argv) == 5:
    script_name = sys.argv[0]
    plan_name = sys.argv[1]
    speed = sys.argv[2]
    validity = sys.argv[3]
    price = sys.argv[4]
else:
    plan_name = "base"
    speed = "10mbps"
    validity = "3month"
    price = "500"

print("___plan summary___")
print("Plan name:", plan_name)
print("Speed:", speed)
print("Validity:", validity)
print("Price:", price)
