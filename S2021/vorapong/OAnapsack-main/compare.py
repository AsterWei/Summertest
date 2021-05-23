def main():
    Max = 0
    Ave = 0
    grsolution = []
    dysolution=[]
    greedyfile = open("grout.txt", "r").readlines()
    for line in greedyfile:
        grsolution.append(int(line))
    dynamicfile = open("dyout.txt", "r").readlines()
    for line in dynamicfile:
        dysolution.append(int(line))
    for i in range(10000):
        frac = grsolution[i]/dysolution[i]
        if(frac > Max):
            Max = frac
        Ave += frac/10000
    print("M = %f" % Max)
    print("A = %f" % Ave)
        


if __name__ == "__main__":
    main()
