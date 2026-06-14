# Jared Morris
# Assignment 1
# 100 Bottles of Beer Countdown Program

def countdown_bottles(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
        bottles -= 1

    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, 0 bottles of beer on the wall.\n")


def main():
    bottles = int(input("How many bottles of beer are on the wall? "))
    countdown_bottles(bottles)
    print("Time to buy more beer!")


main()