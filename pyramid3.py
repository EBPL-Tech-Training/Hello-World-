#pyramid3.py more succint
#height
h=9
spaces = h -1
hashes =2


for i in range(h):
    

    print(" " * spaces,"#"*hashes, end="")
    spaces -=1
    hashes +=2

    print()