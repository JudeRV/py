# ===============================================================
# Name: Jude Vargas
# Date: 10/27/2023
# Algorithm: N/A
# References: N/A
# ===============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
        print(result)

    def is_empty(self):
        """
        Function is_empty returns True if the linked list is empty, else False
        Parameters: None
        Returns: True if the linked list is empty, else False
        """
        return self.head == None

    def size(self):
        """
        Function size returns an int representing the length of the linked list
        Parameters: None
        Returns: an int representing the length of the linked list
        """
        return self.length

    def __iter__(self):
        """
        Function __iter__ allows the linked list to be iterated over by something like a for loop
        Parameters: None
        Returns: None (yields each item in the linked list for iterators)
        """
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def add(self, item):
        """
        Function add adds the specified item (as a node) to the beginning (head) of the linked list
        Parameters:
            item: the item to add to the linked list
        Returns: None
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self, item):
        """
        Function append adds the specified item (as a node) to the end (tail) of the linked list
        Parameters:
            item: the item to append to the linked list
        Returns: None
        """
        if self.is_empty():
            self.add(item)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(item)
            self.length += 1

    def pop(self, pos = None):
        """
        Function pop removes the item at the specified position (or the last position if pos = None)
        Parameters:
            pos (optional) = an int representing the position (index) of the item to remove
        Returns: the item that has been removed from the linked list (or None if no item was removed)
        """
        previous, current = self.head, self.head

        if self.is_empty() or (pos is not None and pos >= self.length):
            raise IndexError("Error: List index out of range")
        elif pos is not None and pos < 0:
            raise IndexError("Error: List index out of range - index cannot be negative")
        
        if self.length == 1:
            self.head = None
        elif pos is not None:
            if pos == 0:
                self.head = current.next
            else:
                count = 0
                while count != pos:
                    previous = current
                    current = current.next
                    count += 1
                previous.next = current.next
        else:
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
        self.length -= 1
        return current


    def search(self, item):
        """
        Function search returns True if the specified item is found within the linked list, else False
        Parameters:
            item: the specified item to search for within the linked list
        Returns: True if the specified item is found within the linked list, else False
        """
        if self.is_empty():
            return False

        current = self.head
        while current is not None:
            if current.data == item:
                return True
            else:
                current = current.next
        return False


    def remove(self, item):
        """
        Function remove removes the specified item from the linked list (if it is found within the list)
        Parameters:
            item: the specified item to remove from the linked list
        Returns: None
        """
        previous, current = self.head, self.head
        if self.is_empty():
            raise ValueError("Error: List is already empty")
        while current is not None:
            if current.data == item:
                previous.next = current.next
                self.length -= 1
                return
            else:
                previous = current
                current = current.next
        raise ValueError("Error: Item could not be found within the list")