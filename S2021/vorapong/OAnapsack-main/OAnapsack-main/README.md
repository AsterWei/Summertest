# Tasks for Student 2

This directory contains (1) a sample generator and (2) a program for greedy algorithm.

## Dependency
- numpy

## Generate samples

```sh
$ python3 generate_sample.py > in.txt
```

The format is as follows:
```
w_11 w_12 ... w_1n
v_11 v_12 ... v_1n
:
w_m1 w_m2 ... w_mn
v_m1 v_m2 ... v_mn
```
where `m` is the number of cases (=100,000), `n` is the number of items (=10), `w_ij` and `v_ij` is j-th item's weight and happiness in i-th case, respectively.

## Solve knapsack problems

```sh
$ cat in.txt | python3 knapsack_greedy.py > out.txt
```

If you want to see what items are chosen, please add the option `--print_items`.

```sh
$ cat in.txt | python3 knapsack_greedy.py --print_items > out.txt
```

# Task for student 3

Solving knaosack problem by Dynamic programming

reference 
https://ja.wikipedia.org/wiki/%E3%83%8A%E3%83%83%E3%83%97%E3%82%B5%E3%83%83%E3%82%AF%E5%95%8F%E9%A1%8C#:~:text=%E3%83%8A%E3%83%83%E3%83%97%E3%82%B5%E3%83%83%E3%82%AF%E5%95%8F%E9%A1%8C%EF%BC%88%E3%83%8A%E3%83%83%E3%83%97%E3%82%B5%E3%83%83%E3%82%AF%E3%82%82%E3%82%93%E3%81%A0%E3%81%84,%E3%82%92%E6%9C%80%E5%A4%A7%E5%8C%96%E3%81%99%E3%82%8B%E3%81%AB

# generate input datasets and save it as in.txt

$ python generate_sample.py

# calculate the solution of knapsack problem and save it as dyout.txt

$ python knapsack_dyanamic.py

# Task for student 2 & 3

$ python compare.py

M and A will be shown at command line




