#!/usr/bin/python3
'''Implemented singly linked list in python'''


class Node:
    '''Nodes of sll'''
    def __init__(self, data, next_node=None):
        '''
        __init__ gets attribute and sets it

        Args:
            data: data
            next_node: next node
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''data getter'''
        return self.__data

    @data.setter
    def data(self, value):
        '''
        data setter

        Args:
            value: value in the node
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''next_node getter'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
        next_node setter

        Args:
            value: next_node
        '''
        if not (isinstance(value, Node) or value is None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''Singly linked list'''
    def __init__(self):
        '''__init__ gets attribute from user'''
        self.__head = None

    def sorted_insert(self, value):
        '''
        sorted_insert inserts nodes to singly linked list.

        Args:
            value: data
        '''
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        elif value > self.__head.data:
            current_node = self.__head
            while current_node.next_node is not None:
                if current_node.next_node.data < value:
                    '''doing this because of 80 character limit'''
                    current_node = current_node.next_node
                else:
                    break
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        '''__str__ helps class to be printable and prints nodes.'''
        string = ""
        temp = self.__head
        while temp is not None:
            string = string + str(temp.data)
            if temp.next_node is not None:
                string = string + "\n"
            temp = temp.next_node
        return string
