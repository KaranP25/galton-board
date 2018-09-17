import random


# A Node class with single pointer to the next node
class Node:

    # Node class constructor
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    # returns the data of the node
    def get_data(self):
        return self.data

    # returns the next node
    def get_next(self):
        return self.next

    # sets the data of the node
    def set_data(self, new_data):
        self.data = new_data

    # sets the next node
    def set_next(self, new_next):
        self.next = new_next


# Class for the singly linked list
class UnorderedLinkedList:
	
    # Class constructor
    def __init__(self):
        self._head = None

    # This method adds to the linked list
    def add(self, item_to_add):
        temp_node = Node(item_to_add)
        temp_node.set_next(self._head)
        self._head = temp_node

    # This method removes a node from the linked list
    def remove(self, item):
        current_node = self._head
        previous = None
        found = False
        while not found:
            if current_node.get_data() == item:
                found = True
            else:
                previous = current_node
                current_node = current_node.get_next()

        if previous == None:
            self._head = current_node.get_next()
        else:
            previous.set_next(current_node.get_next())

    # This method returns array version of the node list.
    def to_array(self):
        arr = []
        node = self._head
        if node != None:
            while node.next != None:
                arr.append(node.data)
                node = node.next
            arr.append(node.data)
        return arr
	
	# This method returns true or false if the linked list is empty
    def isEmpty(self):
        if(self._head == None):
            return True
        else:
            return False


class Drop:
    __cur_ball = None
    __levels = None
    __drop_seq = UnorderedLinkedList

    # class constructor
    def __init__(self, ball_index, levels):
        self.__cur_ball = ball_index
        self.__levels = levels
        self.__drop_seq = UnorderedLinkedList()

    # This method starts dropping the ball
    def start_drop(self):
        ar = ["Left", "Right"]  # ball drop either left or right
        for x in range(self.__levels):
            # ball has either 50 50 chance of going either right or left
            self.__drop_seq.add(random.choice(ar))

    # this method returns the balls drop sequence
    def get_drop_seq(self):
        return self.__drop_seq

    # This method returns the total number of drops to the right
    def get_right_drop_total(self):
        count = int(self.__drop_seq.to_array().count("Right"))
        return count

    # This method returns the total number of drops to the left
    def get_left_drop_total(self):
        count = int(self.__drop_seq.to_array().count("Left"))
        return count