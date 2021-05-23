
def read_sample(nsample):
    readfile = open("in.txt", "r")
    samples = []
    for i in range(nsample):
        ws = readfile.readline().split()
        hs = readfile.readline().split()
        ws = list(map(int, ws))
        hs = list(map(int, hs))
        samples.append([ws, hs])
    # print(samples)
    return samples

def knapsack_dynamic(ws, hs , W, num_bry):
    ws.insert(0,0)
    hs.insert(0,0)
    arr = [[ 0 for i in range(W+1)] for j in range(num_bry+1)]
    for n in range(1, 11):
        for tmpW in range(1, W+1):
            if ws[n] <= tmpW:
                if arr[n-1][tmpW-ws[n]] + hs[n] > arr[n-1][tmpW] :
                    arr[n][tmpW] = arr[n-1][tmpW-ws[n]] + hs[n]
                else:
                    arr[n][tmpW] = arr[n-1][tmpW]
            else:
                arr[n][tmpW] = arr[n-1][tmpW]
    return arr[-1][-1]

def main():
    nsample = 10000 #number of samples
    samples = read_sample(nsample)
    W = 250 #max weight W
    num_bry = 10 #number of strawberry
    savefile = open("dyout.txt", "w")
    for ws, hs in samples:
        dynamicsol= knapsack_dynamic(ws, hs, W, num_bry)
        l1 = str(dynamicsol)
        savefile.write(l1+"\n")
    savefile.close()


        


if __name__ == "__main__":
    main()
