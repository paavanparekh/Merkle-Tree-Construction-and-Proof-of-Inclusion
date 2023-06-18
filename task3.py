# Author: Paavan Mayurkumar Parekh
# ID    : 201901067
# Course: Blockchain and Cryptocurrency
# Mentor: Prof. Anish Mathuria
######################### Logic ~ Task3 ################################################
# Input : document file and proof.txt file
# Output: whether input document is member of the tree or not
# The program will compute hash of the root from the given inputs and match it with the
# root hash given in the "tree.txt" file. If they match,the doc5.dat is a member of the
# tree otherwise not a member.
# For verifying inclusion of input document, take that document concatenate with node from
# "proof.txt" file and Hash concatenation of nodes.similarly hash concatenation of that
# output node with next node from "proof.txt". Do similar till you reach root.
# merkle root created from above algorithm and merkle root from "tree.txt"  is verified
# if both are same then document is included otherwise not.
import numpy as np
import hashlib
import string

prf_file = open("proof.txt", 'r')
data = prf_file.readlines()
tree_arr = []
for address in data:
    k1 = address.split(":")[0]
    k2 = address.split(":")[1]
    k3 = address.split(":")[2][:-1]
    tree_arr.append((k1, k2, k3))

prf_file.close()

mrkfile = open("tree.txt", 'r')
data = mrkfile.readlines()
i = 1
arr = []
for address in data:
    if i != 1:
        k1 = address.split(":")[0]
        k2 = address.split(":")[1]
        k3 = address.split(":")[2][:-1]
        arr.append((k1, k2, k3))
    else:
        n = address.split(":")[2]
    i = i+1
mrkfile.close()

hashtoval = {}
for i in range(len(arr)):
    hashtoval[arr[i][2]] = (arr[i][0], arr[i][1])


datafile = input("Enter filename: ")
docno = int(datafile[3:-4])
file = open(datafile, 'r')
str = file.read()
MerkleRoot_ = hashlib.sha256(str.encode('utf-8')).hexdigest()
file.close()
l = 0
i = 0

while(i < len(tree_arr)):
    if l == int(tree_arr[i][0]):
        if docno > int(tree_arr[i][1]):
            ptr = tree_arr[i][2]+MerkleRoot_
        else:
            ptr = MerkleRoot_+tree_arr[i][2]
        i = i+1
    else:
        ptr = MerkleRoot_
    MerkleRoot_ = hashlib.sha256(ptr.encode('utf-8')).hexdigest()
    if(MerkleRoot_ in hashtoval):
        docno = int(hashtoval[MerkleRoot_][1])
        l = int(hashtoval[MerkleRoot_][0])
    else:
        print('Document is not included in Merkle Tree')
        exit()

mrkfile = open('tree.txt', 'r')
MerkleRoot = mrkfile.readline().split(":")[4][:-1]
mrkfile.close()
print("Merkle root from tree.txt: ", MerkleRoot)
print("Merkle root from proof.txt: ", MerkleRoot_)
if MerkleRoot == MerkleRoot_:
    print('Document is included in Merkle Tree')
else:
    print('Document is not included in Merkle Tree')
