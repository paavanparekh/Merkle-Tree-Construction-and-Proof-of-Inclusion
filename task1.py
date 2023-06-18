# Author: Paavan Mayurkumar Parekh
# ID    : 201901067
# Course: Blockchain and Cryptocurrency
# Mentor: Prof. Anish Mathuria
######################### Logic ~ Task1 ##############################################
# Input : n data files doc0.dat,doc1.dat,....
# Output: tree.txt representing Merkle tree corresponding to data files
# Leaves of the Merkle tree are Hashes of document files so first i
# have created array of Hash(doc.dat) as "Leaves".After creating Leaves
# of the tree(last level of the tree), to make upper level of tree we
# have to merge two leaves.If we don't have two leaves for merging
# operation than take only one leaf.Node on the level above the leaves
# is created as Hash(leaf1+leaf2) or Hash(leaf).Similarly, all levels
# upto root is created by merging two nodes of the lower level creating
# node of the upper level.Output file "tree.txt" is generated as
# mentioned in the hw2.pdf.
#
# Example Merkle tree for 2 documents:
#                 2.0
#           /             \
#         1.0             1.1
#      /      \            |
#  0.0         0.1        0.2
# doc0.dat   doc1.dat   doc2.dat
#
# Similar Merkle tree in "tree.txt" file looks like:
#
# MerkleTree:sha1:3:3:cb394702be57d813a794edc1ed3cc7e7a2692cd98d10739382ab8bd9fb693de1
# 0:0:e363e15b2d3325106a6eebfb86ce3eeb42cde8099ff8b19b0416d8d1418df9cb
# 0:1:a2e1fdb18e9677a8eac3b5e091d7d164ef1a6e03abfd25039c1abdf330f696da
# 0:2:42c531199696b2241d3aa2abafc49aea8cc6a9f0746725d7cd21072b8cd3dfea
# 1:0:ce82e216f5b0dff23f5b952f02ac593f9062835716bb6576891eb09cffd064fe
# 1:1:d8973dde486055e0c3d914c5bbd0d786a78961603ca653d9398a7d847988c48d
# 2:0:cb394702be57d813a794edc1ed3cc7e7a2692cd98d10739382ab8bd9fb693de1
import numpy as np
import hashlib
import random
import string

n = int(input('Total number of documents : '))
Leaves = []
mrkfile = open("tree.txt", 'w')
for i in range(0, n):
    filename = "doc"+str(i)+".dat"
    file = open(filename, 'w')
    data = ''.join((random.choice(string.ascii_lowercase)
                    for x in range(50)))
    file.write(data)
    Hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
    Leaves.append(Hash)
    mrkfile.write("0:"+str(i)+":"+Hash+"\n")
Nodes = Leaves

level = 1
while len(Nodes) != 1:
    array = []
    cnt = 0
    for i in range(0, len(Nodes), 2):
        node1 = Nodes[i]
        if i+1 < len(Nodes):
            node2 = Nodes[i+1]
            str1 = (node1+node2).encode('utf-8')
            Hash12 = hashlib.sha256(str1).hexdigest()
        else:
            str2 = (node1).encode('utf-8')
            Hash12 = hashlib.sha256(str2).hexdigest()

        array.append(Hash12)
        mrkfile.write(str(level)+":"+str(cnt)+":"+Hash12+"\n")
        cnt = cnt + 1

    Nodes = array
    level = level+1

mrkfile.close()

fileptr = open("tree.txt", 'r+')
lines = fileptr.readlines()
lines.insert(0, "MerkleTree:sha1:"+str(n)+":"+str(level)+":"+Nodes[0]+"\n")
fileptr.seek(0)
fileptr.writelines(lines)
