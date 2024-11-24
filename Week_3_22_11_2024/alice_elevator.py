elevator_A = int(input("Enter the location of elevator A:"))
elevator_B = int(input("Enter the location of elevator B:"))
alice = int(input("Enter the location of alice:"))
alice_A = alice - elevator_A
alice_B = alice - elevator_B

if alice_A < 0:
    alice_A = -alice_A
if alice_B < 0:
    alice_B = -alice_B
if alice_A<alice_B:
    print("A")
else:
    print("B")

