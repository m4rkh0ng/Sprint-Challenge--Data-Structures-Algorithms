Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
  A: O(n) since we'll visit each node once by the end of the traversal.

2. What is the space complexity of your `depth_first_for_each` function?
  A: O(h), where h is the height of the tree.

3. What is the runtime complexity of your `breadth_first_for_each` method?
  A: O(n) since we'll visit each node once by the end of the traversal.

4. What is the space complexity of your `breadth_first_for_each` method?
  A: O(w), where w is the width of the tree.

5. What is the runtime complexity of your `heapsort` function?
  A: O(n log(n))

6. What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data. What would be the space complexity if your function instead altered the input array?
  A: At worst, it should be a constant array, so O(1). Altering the input array, it would still be constant as it's updating, so O(1) from what I can tell (at worst). It could get really big, but the input array itself is not getting any bigger or smaller (the indices change to sort things in the right places in that case).