import unittest
import string

class BinTreeNode(object):
 
    def __init__(self, value, freq): #O(1)
        """Defines object binary tree node that has pointers to nodes below to the left and right"""
        """
        Title: Binary Tree implementation Author: Hintea, D.
        Date: 2018
        Availability: http://moodle.coventry.ac.uk
        """
        self.value=value
        self.left=None
        self.right=None
        #My code to keep track of the parent node and to store the frequency in that node
        self.parent=None
        self.freq=freq
       
def tree_insert(tree, item, freq): #O(n)
    """Takes a tree, and item and its frequency and creates a node object and stores it in the tree"""
    if freq < 1:
        raise ValueError("Frequency must be >= 1")
    if tree==None:                                          #If tree is empty create new tree
        tree = BinTreeNode(item, freq)
    else:
        if(item < tree.value):                              #If the frequency of the node trying to insert is less than the frequency of top node move to left sub-tree
            if(tree.left==None):                            #If the there is no value in the left node insert there
                tree.left=BinTreeNode(item, freq)
                tree.left.parent = tree
            else:                                           #Else try insert again only in left sub-tree
                tree_insert(tree.left,item,freq)
        else:                                               #If the frequency of the node trying to insert is greter than the tip node move to the right sub-tree
            if(tree.right==None):                           #If the there is no value in the left node insert there
                tree.right=BinTreeNode(item, freq)
                tree.right.parent = tree
            else:
                tree_insert(tree.right,item,freq)           #Else try insert again only in right sub-tree
    return tree
 
def postorder(tree): #O(n)
    """Function that takes a binary tree as input and prints in in post order"""
    """
    Title: Post Order Implementation Author: Hintea, D.
    Date: 2018
    Availability: http://moodle.coventry.ac.uk
    """
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 
def in_order(tree): #O(n)
    """Function that takes a binary tree as input and prints in in order"""
    """
    Title: Doubly Linked List Implementation Author: Hintea, D.
    Date: 2018
    Availability: http://moodle.coventry.ac.uk
    """
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)

def pre_order(tree): #O(n)
    """Function that takes a binary tree as input and prints in in pre-order"""
    print (tree.value)
    if(tree.left!=None):
        pre_order(tree.left)
    if(tree.right!=None):
        pre_order(tree.right)

def pre_orderReturn(tree, result): #O(n)
    """Function that takes a binary tree and returns a pre_order list"""
    result.append(tree.value)
    if(tree.left!=None):
        pre_orderReturn(tree.left, result)
    if(tree.right!=None):
        pre_orderReturn(tree.right, result)
    return result

def searchRec(tree, target): #O(log(n))
    """Searches a binary tree for the target. Prints path to item and returns True if in and False if not and prints the path"""
    try:
        if(type(target) == str):                        #If the input is a string converts all to upper case for consistency when searching 
            target = target.upper()
        if(tree.value == target) or (tree == 0):        #If the target value is at the top of the tree returns True
            print("Found")                              #Prints found to show that item is in the tree
            return True
        elif(target < tree.value):                      #If the target value is less than the item at the top of the tree search the sub-tree left of the node
            print("Left")                               #Prints left to show that it took left path
            return searchRec(tree.left, target)
        else:                                           #If the traget value is greater than the item at the top of the tree search the sub-tree right of the node
            print("Right")                              #Prints right to show it took the right path
            return searchRec(tree.right, target)        
        return False                                    #Returns false if not in tree
    except TypeError:                                   #Catches error when trying to search for something that is of different data type to the node in the tree
        print("ERROR! The value you search for must be the same data type as the nodes in the tree")
        return False
    except AttributeError:                              #Catches error when string not in tree
        print("Item not in tree")
        return False
    
def search(tree, target): #O(log(n))
    """Searches a binary tree for the target. Returns True if in and False if not"""
    try:
        if(type(target) == str):                        #If the input is a string converts all to upper case for consistency when searching 
            target = target.upper()
        if(tree.value == target) or (tree == 0):        #If the target value is at the top of the tree returns True
            return tree
        elif(target < tree.value):                      #If the target value is less than the item at the top of the tree search the sub-tree left of the node
            return search(tree.left, target)
        else:                                           #If the traget value is greater than the item at the top of the tree search the sub-tree right of the node
            return search(tree.right, target)
        return False                                    #Returns false if not in tree
    except TypeError:                                   #Catches error when trying to search for something that is of different data type to the node in the tree
        print("ERROR! The value you search for must be the same data type as the nodes in the tree")
        return False
    except AttributeError:                              #Catches error when string not in tree
        return False
    
def splitFile(file): #O(n)
    """reads an input from a file and splits at each word then returns a list of these words"""
    try:
        f=open(file, "r")
        contents = (f.read()).upper()                               #Converts the whole string to upper case and assigns to contents"The specified file was not found! Make sure the file is in the same folder as this file"
        f.close()                                                   #Closes the file
        translator = str.maketrans('', '', string.punctuation)      #Removes punctuation from the string
        contents = contents.translate(translator)       
        split = contents.split(" ")                                 #Creates a list of words from the file
    except FileNotFoundError:                                       #If python doesn't find the file prints error message
        print("The specified file was not found! Make sure the file is in the same folder as this file")
        split = None
    return split                                                    #Returns list of words in file

def countWords(listOfWords): #O(n)
    "Function takes in a string of words and returns a dictionary with the word as the key and the number of instances as the value"""
    wordDict = {}
    for word in listOfWords:
        if word in wordDict:                            #If a word is in the dictionary add 1 to its value
            wordDict[word] = wordDict[word] + 1
        else:                                           #Else add the value to the dictionary and give it a value of 1
            wordDict[word] = 1
    return wordDict                                     #Returns the dictionary                                            
    

def buildTree(wordDict): #O(n^2)
    """Function takes a dictionary and passes each item to the tree_insert() function then returns the tree"""
    if(wordDict == {}):
        raise ValueError("The dictionary has is empty. A tree can't be made from this")
    initialised = False                                 #A tracker to see if there is a tree to insert into
    for word in wordDict:                              
        if initialised == False:                        #If there is no tree then it creates a tree with the first element
            initialised = True                          #Changes tracker to indicate that a tree exists
            t = tree_insert(None, word, wordDict[word])
        else:                                           #If there is a tree inserts element into the pre-existing tree t
            tree_insert(t, word, wordDict[word])
    return t                                            #Returns created binary tree        

def countChildren(node): #O(1)
    """Takes a node and returns the count of its children"""
    count = 0
    if node.left != None:
        count = count + 1
    if node.right != None:
        count = count + 1
    return count

def getMin(tree): #O(n)
    """Input is a tree and returns the minimum node in the tree"""
    while tree.left != None:
        tree = tree.left
    return tree

def delNode(tree, value): #O(nlog(n))
    """Inputs are a tree and a value returns tree with value removed from it"""
    node = search(tree, value)                  #Search for the value in the tree
    if node == False:
        raise ValueError("Item was not found in the tree")
    if countChildren(node) == 0:                #If the node has no children delete the node
        if node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None
    elif countChildren(node) == 1:              
        try:                                    #Try to set the value of the tree to the tree stored in left child
            node = node.left
        except AttributeError:
            node = node.right
    else:                                       #When node has two children
        minNode = getMin(node.right)
        node.value = minNode.value
        delNode(node.right, minNode.value)
    return tree

def binTree(file): #O(n^2log(n))
    """Input is a file name and returns a binary tree of every word in file and frequency it appears"""
    split = splitFile(file)                             #Splits the words in the file into a list of words
    wordDict = countWords(split)                        #Creates a dictionary of words and the number of occurences of this word
    tree = buildTree(wordDict)                          #Creates a binary tree from the dictionary comparing number of occourences
    return tree                                         #Returns the created binary tree


"""Testing is done under this line"""

class TestBST(unittest.TestCase):

    def setUp(self):
        """Defining lists, dictionaries trees to be used in future tests"""
        self.list1 = ["CHERRY", "BANANA", "BANANA", "BANANA", "BANANA", "BANANA", "APPLE", "APPLE", "LIME", "LIME", "LIME", "GRAPE", "GRAPE", "GRAPE", "GRAPE", "GRAPE", "GRAPE", "POMEGRANATE"]
        self.list2 = ["0", "1", "2", "2", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "5", "6", "6", "6", "6", "6", "6"]
        self.dict1 = {'CHERRY' : 1, 'BANANA' : 5, 'APPLE' : 2, 'LIME' : 3, 'GRAPE' : 6, 'POMEGRANATE' : 1}
        self.dict2 = {'0' : 1, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6}
        self.tree1 = buildTree(self.dict1)
        self.tree2 = buildTree(self.dict2)
        
    def test_splitFile(self):
        #Test 1 on search.txt file
        self.assertEqual(splitFile("search.txt"), self.list1)
        #Test 2 on numText.txt file
        self.assertEqual(splitFile("numText.txt"), self.list2)
        #Test 3 on a file that doesn't exist
        self.assertEqual(splitFile("NotAFile.txt"), None)
        #Test 4 on an empty file
        self.assertEqual(splitFile("empty.txt"), [''])

    def test_countWords(self):
        #Test 1
        self.assertEqual(countWords(self.list1), self.dict1)
        #Test 2
        self.assertEqual(countWords(self.list2), self.dict2)
        #Test 3 with empty list as input
        self.assertEqual(countWords([]), {})
        #Test 4 with empty string in list
        self.assertEqual(countWords(['']), {'' : 1})

    def test_buildTree(self):
        #Test 1
        tree1 = buildTree(self.dict1)
        self.assertEqual(tree1.left.value, 'BANANA')
        self.assertEqual(tree1.right.value, 'LIME')
        #Test 2 when top of tree has no value in left
        tree2 = buildTree(self.dict2)
        with self.assertRaises(AttributeError):
            tree2.left.value
        self.assertEqual(tree2.right.value, '1')
        #Test 3 trying to build empty tree
        with self.assertRaises(ValueError):
            buildTree({})

    def test_tree_insert(self):
        #Inserting first number into the tree
        tree1 = tree_insert(None, 1, 1)
        self.assertEqual(pre_orderReturn(tree1, []), [1])
        #Inserting another number into the tree
        tree_insert(tree1, 2, 2)
        self.assertEqual(pre_orderReturn(tree1, []), [1, 2])
        #Trying to insert a value with a negative frequency
        with self.assertRaises(ValueError):
            tree_insert(tree1, 5, -1)

    def test_search(self):
        self.assertEqual(search(self.tree1, "Cherry").value, "CHERRY")
        self.assertFalse(search(self.tree1, "Hello"))
        self.assertFalse(search(self.tree1, 1))
        self.assertFalse(search(self.tree1, True))

    def test_parentsAndFrequency(self):
        #Check the top of the tree's parent and freq values
        self.assertEqual(self.tree1.freq, 1)
        self.assertEqual(self.tree1.parent, None)
        #Check the right of the tree's freq value
        right = self.tree1.right
        self.assertEqual(right.freq, 3)
        #Check the left of the tree's freq value
        left = self.tree1.left
        self.assertEqual(left.freq, 5)
        #Check the right of the tree's parent node
        self.assertEqual(right.parent, self.tree1)
        #Check the left of the tree's parent node
        self.assertEqual(left.parent, self.tree1)

    def test_countChildren(self):
        self.assertEqual(countChildren(self.tree1), 2)
        banana = search(self.tree1, "banana")
        self.assertEqual(countChildren(banana), 1)
        apple = search(self.tree1, "apple")
        self.assertEqual(countChildren(apple), 0)
        
    def test_getMin(self):
        self.assertEqual(getMin(self.tree1).value, "APPLE")
        self.assertEqual(getMin(self.tree1.right).value, "GRAPE")
    
    def test_delNode(self):
        delApple = delNode(self.tree1, "APPLE")
        self.assertEqual(pre_orderReturn(delApple, []), ["CHERRY", "BANANA", "LIME", "GRAPE", "POMEGRANATE"])
        delCherry = delNode(self.tree1, "CHERRY")
        self.assertEqual(pre_orderReturn(delCherry, []), ["GRAPE", "BANANA", "LIME", "POMEGRANATE"])
        with self.assertRaises(ValueError):
            delNothing = delNode(self.tree1, "Nothing")

if __name__ == '__main__':
    unittest.main(buffer=True)

