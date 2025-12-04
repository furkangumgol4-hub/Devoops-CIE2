import sys
default_plan = "6month"
default_speed = "150Mbps"
default_validity = "12/2/26"
default_price = "1600"

if len(sys.argv) > 1:
    plan_name = sys.argv[1]
else:
    plan_name = default_plan

if len(sys.argv) > 2:
    speed = sys.argv[2]
else:
    speed = default_speed

if len(sys.argv) > 3:
    validity = sys.argv[3]
else:
    validity = default_validity

if len(sys.argv) > 4:
    price = sys.argv[4]
else:
    price = default_price

print("___ Plan Summary ___")
print("Plan name:", plan_name)
print("Speed:", speed)
print("Validity:", validity)
print("Price:", price)
