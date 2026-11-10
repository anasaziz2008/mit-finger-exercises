class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []

    def size(self):
        """
        Returns the length of the container list
        """
        # Your code here
        return len(self.myList)

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        # Your code here
        self.myList.append(elem)

class Stack(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The newest element in the container list is removed
        Returns the element removed or None if the queue contains no elements
        """
        if self.size() < 1:
            return None
        return self.myList.pop()
        
# L = Container()
# L.add(1)
# L.add(2)
# L.add(3)
# L.add(4)

# print(L.size())
# print(L.myList)

# L.add(5)

# print(L.size())
# print(L.myList)


# L1 = Stack()
# L1.add(1)
# L1.add(2)
# L1.add(3)
# L1.add(4)
# print(L1.size())
# print(L1.myList)

# L1.remove()
# print(L1.size())
# print(L1.myList)

