import argparse

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

def knapsack_greedy(ws, hs, W):
    idx = list(range(1, len(ws)+1))
    items = list(zip(ws, hs, idx))
    items.sort(key=lambda item: item[0] / item[1])

    sol = 0
    S = []
    for w, h, i in items:
        if W - w >= 0:
            W -= w
            sol += h
            S.append(i)
        else:
            if sol < h:
                sol = h
                S = [i]
            break
    return sol, S

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--print_items", action="store_true")
    args = parser.parse_args()

    nsample = 10000
    samples = read_sample(nsample)
    W = 250
    savefile = open("grout.txt", "w")
    if args.print_items:
        for ws, hs in samples:
            sol, S = knapsack_greedy(ws, hs, W)
            print(sol, sorted(S))
    else:
        for ws, hs in samples:
            sol, _ = knapsack_greedy(ws, hs, W)
            print(sol)
            savefile.write(str(sol)+"\n")
    savefile.close()
