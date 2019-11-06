class CircularDeque:


    def __init__(self, k: int):
        self._k = k
        self._elems = 0
        self._deque = [None]*self._k
        self._front = 0  #exclusive
        self._rear = 0  #inclusive
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        
        if not self.isFull():
            self._deque[self._front] = value
            self._front = (self._front + 1) % self._k
            self._elems += 1
            return True
        
        return False
            
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self._rear = (self._rear - 1)%self._k
            self._deque[self._rear] = value
            self._elems += 1
            return True
        
        return False        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self._front = (self._front - 1) % self._k
            self._deque[self._front] = None
            self._elems -= 1
            return True
        
        return False
  
    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self._deque[self._rear] = None
            self._rear = (self._rear + 1)%self._k
            self._elems -= 1
            return True
        
        return False        

        
    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self._deque[(self._front - 1)%self._k] if not self.isEmpty() else -1
        
    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self._deque[self._rear] if not self.isEmpty() else -1
    
        
    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not bool(self._elems)
        
    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._elems == self._k
   
