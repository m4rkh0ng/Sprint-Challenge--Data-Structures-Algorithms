Add your answers to the Algorithms exercises here.
Exercise I:
a) Running time of this appears to be O(n^3) at worst since it's assessing n * n * n.
b) O(n^3) since it's nesting each time that the loops are comparing the continuation point where n is involved.
c) O(n) where n is the value of bunnies, as it will be recursively called until it reaches 0.

Exercise II:
Start from floor 0, and drop egg. If egg does not break, increment floor count by one.
Recursively then call egg drop on the next floor and repeat going up floors until it breaks.
On break, store the floor number that we have incremented to. This will tell us what the threshold is for _f_.
Then return saying something like, "An egg gets broken if it's thrown off of floor _f_ of higher."