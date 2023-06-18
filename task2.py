# Author: Paavan Mayurkumar Parekh
# ID    : 201901067
# Course: Blockchain and Cryptocurrency
# Mentor: Prof. Anish Mathuria
######################### Logic ~ Task2 ################################################
# Input : document file
# Output: proof.txt that produce proof of membership
# proof of membership for a given document at position
# k consists of a list of nodes that allows the verifier to recompute the hashes in
# the path from the k-th leaf to the root.
# To generate proof of membership for given document we should have some information
# about its parent and its sibling node,so i have created adjacency list data structure.
#
# adjacency list : adj[(l,cnt)]=[((l1,c1),'c'),((l2,c2),'c'),((l3,c3),'p')] where
# 'c'=child and 'p'=parent of node represented by (l,cnt).l=level and cnt=number of node
# at that level.After creating adjacency list, document whose proof is needed is entered
# by user.now corresponding to that document parent is extracted from adjacency list.
# then similarly node which we are going to push in "proof.txt" is extracted.
# so from kth node(position of our document) to root proof nodes are added to "proof.txt",
# recursively.

import numpy as np
import hashlib
import string

mrkfile = open("tree.txt", 'r')
data = mrkfile.readlines()
i = 1
tree_arr = []
hashmap = {}
for address in data:
    if i != 1:
        k1 = address.split(":")[0]
        k2 = address.split(":")[1]
        k3 = address.split(":")[2][:-1]
        tree_arr.append((k1, k2, k3))
        hashmap[(k1, k2)] = k3
    else:
        n = address.split(":")[2]
    i = i+1
mrkfile.close()


adj = {}
start = int(n)
i = int(n)
j = 0
parent_map = {}

for ki in range(0, i):
    adj[('0', str(ki))] = [((-1, -1), 'c')]

while(j < len(tree_arr) and i < len(tree_arr)):
    n1 = (tree_arr[j][0], tree_arr[j][1])
    if j == start:
        start = i
    if j+1 < start:
        n2 = (tree_arr[j+1][0], tree_arr[j+1][1])
        adj[(tree_arr[i][0], tree_arr[i][1])] = [(n1, 'c'), (n2, 'c')]
        adj[n1].append(((tree_arr[i][0], tree_arr[i][1]), 'p'))
        adj[n2].append(((tree_arr[i][0], tree_arr[i][1]), 'p'))
        j = j+2
    else:
        adj[(tree_arr[i][0], tree_arr[i][1])] = [(n1, 'c')]
        adj[n1].append(((tree_arr[i][0], tree_arr[i][1]), 'p'))
        j = j+1
        start = i+1
    i = i+1

adj[(tree_arr[start][0], tree_arr[start][1])].append(((-1, -1), 'p'))


datafile = input("Enter document name: ")
docno = datafile[3:-4]
doctup = ('0', docno)

for jj in range(len(adj[doctup])):
    if(adj[doctup][jj][1] == 'p'):
        node = adj[doctup][jj][0]

parent_doc = ('0', '0')
proof_file = open('proof.txt', 'w')
while(node != (-1, -1)):

    if len(adj[node]) != 2:

        if adj[node][0][1] != 'p' and adj[node][0][0] != doctup:
            str = adj[node][0][0][0]+":"+adj[node][0][0][1] + \
                ":"+hashmap[adj[node][0][0]]+"\n"
        elif adj[node][1][1] != 'p' and adj[node][1][0] != doctup:
            str = adj[node][1][0][0]+":"+adj[node][1][0][1] + \
                ":"+hashmap[adj[node][1][0]]+"\n"
        elif adj[node][2][1] != 'p' and adj[node][2][0] != doctup:
            str = adj[node][2][0][0]+":"+adj[node][2][0][1] + \
                ":"+hashmap[adj[node][2][0]]+"\n"
        if adj[node][0][1] == 'p':
            parent_doc = adj[node][0][0]
        elif adj[node][1][1] == 'p':
            parent_doc = adj[node][1][0]
        else:
            parent_doc = adj[node][2][0]
        proof_file.write(str)

    else:
        if adj[node][0][1] == 'p':
            parent_doc = adj[node][0][0]
        else:
            parent_doc = adj[node][1][0]

    doctup = node
    node = parent_doc
proof_file.close()
