
**Problem Statement: Write a command line driven text search engine**
```
Solution:  This solution creates an In Memory Trie to  search the input words
           and then rank the files based on number of words found in a file.
           During the testing this solution assumes that words are from
           English language. It will work for any language, but I haven't
           tested.

Ranking Algorithm: Each file is ranked based on the total no of words  found in that
file. rank = (word found/Total words as input)*100

Assumptions: The solution looks only for all the ".txt" file extension under the top level path
             For example if a path contains subdirectory it will walk through all
             of them.
             A space seprated text is considered as a single word.
             Every space seprated word is marked in a trie relative to its file.

Limitation: There is no restriction put on memory usage and dictionary size as
of now.

How to run the program:
************************

To Run:
python SchibstedWork.py "/Users/vkumar/Test/"

OutPut:
Path:/Users/vkumar/Test/:Total files scanned:6
search>Watching  the  lush  world Vipin
"Test1/elite.txt" : 80 %
"Test/100west.txt" : 20 %
"Test/13chil.txt" : 20 %
"Test/mytest.txt" : 20 %
```


