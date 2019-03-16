import os
import sys
from typing import Tuple
import logging

logger = logging.getLogger()
class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.files = set()
        self.word_finished = False
        self.counter = 1

def add(root,word:str,filename):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True
    node.files.add(filename)

def find_prefix(root, prefix: str):
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
      3. If yes then how may files has the same words
    """
    node = root
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, 0
    # Well, we are here means we have found the prefix.
    return True, node.counter, node.files

def createTrie(path):
    textFiles = walkTheDirectory(path)
    for files in textFiles: # obtain list of files in directory
        splitPath = files.split("/")
        length = len(splitPath)
        name = '\"' + splitPath[length-2] + "/" + splitPath[length-1] + '\"'
        with open(files, 'r') as f:
            for line in f:
                for word in line.split():
                    add(root, word, name)

def walkTheDirectory(path):
    textFiles = [os.path.join(root, name) for root, dirs, files in os.walk(path) for name in files if name.endswith((".txt"))]
    logger.error("Path:" + path + ":Total files scanned:" + str(len(textFiles)))
    return textFiles

def displayRank(words):
    rank = {};
    for i in words:
        tup = find_prefix(root, i)
        if(not tup[0]):
            continue
        for items in tup[2]:
            if items in rank:
                rank[items] += 1
            else:
                rank[items] = 1
    if(len(rank) == 0):
        logger.error("Words do not exist")
        return

    sorted_by_value = sorted(rank.items(), key=lambda kv: kv[1], reverse = True)
    count = 0
    for i in range (0,len(sorted_by_value)):
        if(count < 10):
            pc = (sorted_by_value[i][1]/len(words))*100
            print(sorted_by_value[i][0], ":", round(pc),"%")
            count +=1
        else:
            break

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        logger.error("Directory name is expected")
    dirName = sys.argv[1]
    logger.info("dir Name:" + dirName)
    if(not os.path.isdir(dirName)):
        logger.error("Not a valid directory path")
        exit()

    root = TrieNode('*')
    createTrie(dirName)

    trigger = True
    while (trigger == True):
        try:
            name = input("search>")
            data = name.split()
            displayRank(data)
        except KeyboardInterrupt:
            trigger = False

    if(trigger == False):
        logger.error("Program was interupted, shutdown initialized")
        logger.error("shutdown complete")
        exit()
