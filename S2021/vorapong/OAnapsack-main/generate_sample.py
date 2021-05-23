import numpy as np

if __name__ == "__main__":
    np.random.seed(1)

    nsample = 10000
    nsize = 10
    max_weight = 100

    samples = np.random.randint(1, max_weight+1, nsample * 2 * nsize)
    samples = samples.reshape([nsample * 2, -1])
    savefile = open("in.txt", "w")
    for sample in samples:
        l = list(map(str, sample))
        # print(" ".join(l))
        savefile.write(" ".join(l)+"\n")
    savefile.close()
