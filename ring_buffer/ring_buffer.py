from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check if anything in buffer
        if self.capacity > self.storage.length:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # if current = tail, remove tail and replace, move current to head
        elif self.current is self.storage.tail:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # if current item is the head, remove and replace, move current to next item
        elif self.current is self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.current.next
        # for all other places in buffer, add "before" (to the right), replace and move current to next
        else:
            self.current.insert_before(item)
            self.current.delete()
            self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        while self.storage.head is not None:
            list_buffer_contents.append(current.value)
            if current.next is None:
                break
            else:
                current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
