import argparse
import numpy as np

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
    selected = [[0 for i in range(num_bry)] for j in range(W+1)] 
    arr = [[ 0 for i in range(W+1)] for j in range(num_bry+1)]
    for n in range(1, 11):
        print(selected[W])
        for tmpW in range(1, W+1):
            if ws[n] <= tmpW:
                if arr[n-1][tmpW-ws[n]] + hs[n] > arr[n-1][tmpW] :
                    arr[n][tmpW] = arr[n-1][tmpW-ws[n]] + hs[n]
                    selected[tmpW] = selected[tmpW-ws[n]]
                    selected[tmpW][n-1] = 1
                else:
                    selected[tmpW][n-1] = 0
                    arr[n][tmpW] = arr[n-1][tmpW]
            else:
                selected[tmpW][n-1] = 0
                arr[n][tmpW] = arr[n-1][tmpW]

    return arr[-1][-1], selected[W]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--print_items", action = "store_true")
    args = parser.parse_args()
    nsample = 1
    samples = read_sample(nsample)
    W = 250
    num_bry = 10
    savefile = open("dyout.txt", "w")
    if args.print_items:
        for ws, hs in samples:
            dynamicsol, S = knapsack_dynamic(ws, hs, W, num_bry)
            # print(dynamicsol, S)
            l1 = str(dynamicsol)
            savefile.write(l1+"\n")
            l2 = list(map(str, S))
            savefile.write(" ".join(l2)+"\n")
    else:
        for ws, hs in samples:
            dynamicsol, _ = knapsack_dynamic(ws, hs, W, num_bry)
            l1 = str(dynamicsol)
            savefile.write(l1+"\n")
    savefile.close()


        


if __name__ == "__main__":
    main()
