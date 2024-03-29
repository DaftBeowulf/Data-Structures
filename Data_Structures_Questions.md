Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
   O(1) -- performs one execution regardless of current Queue length

2. What is the runtime complexity of `dequeue`?
   O(1) -- performs one execution regardless of current Queue length

3. What is the runtime complexity of `len`?
   O(n) -- loop through the length of the LinkedList used for storage before returning a value

## Binary Search Tree

1. What is the runtime complexity of `insert`?
   averages out to O(log n) -- each check it performs at the current node eliminates needing to traverse half the remaining tree

2. What is the runtime complexity of `contains`?
   averages out to O(log n) -- each check it performs at the current node eliminates needing to traverse half the remaining tree (is either in left or right of current node, if not AT current node)

3. What is the runtime complexity of `get_max`?
   averages out to O(log n) -- each check it performs eliminates the left branch of the current node (all the lower values)

## Heap

1. What is the runtime complexity of `_bubble_up`?
   approximately O(log n) -- it could potentially have to bubble up all the way from a leaf to the root node, but the path it would take to get there would eliminate more than half of the comparisons in a standard list

2. What is the runtime complexity of `_sift_down`?
   O(log n) -- the reverse of bubble_up but remains the same, even if the values have to sift all the way down to a distant leaf, it would be cutting the comparisons in half with each step

3. What is the runtime complexity of `insert`?
   O(log n) -- it only appends the new value to the end and then runs \_bubble_up

4. What is the runtime complexity of `delete`?
   O(log n) -- it only swaps and deletes the end values and then runs \_sift_down

5. What is the runtime complexity of `get_max`?
   O(1) -- it always it at the first index, so constant time

## Doubly Linked List

1.  What is the runtime complexity of `ListNode.insert_after`?
    O(1) -- operation has same function execution count regardless of LinkedList's current size

2.  What is the runtime complexity of `ListNode.insert_before`?
    O(1) -- operation has same function execution count regardless of LinkedList's current size

3.  What is the runtime complexity of `ListNode.delete`?
    O(1) -- operation has same function execution count regardless of LinkedList's current size

4.  What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    O(1) -- operation has same function execution count regardless of LinkedList's current size

5.  What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    O(1) -- operation has same function execution count regardless of LinkedList's current size

6.  What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    O(1) -- operation has same function execution count regardless of LinkedList's current size

7.  What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    O(1) -- operation has same function execution count regardless of LinkedList's current size

8.  What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    O(1) -- operation has same function execution count regardless of LinkedList's current size

9.  What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    O(1) -- operation has same function execution count regardless of LinkedList's current size

10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(1) -- operation has same function execution count regardless of LinkedList's current size

        a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

The JS splice method has a worst-case complexity O(n) since under the hood, it has to change the index of every item in the array that gets moved. For instance, if the first item is sliced, every other item in the array has to be operated on to lower their index by one and move them closer to the front. This would have to occur n-1 times and is therefore worse than the linked lists' delete method since its runtime stays the same no matter the size of the list
