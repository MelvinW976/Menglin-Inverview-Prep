# Array Basics

1. What is an array?
An array is a collection of items of same data type stored at contiguous memory locations. 
**easier to know the value of a paticular element by adding an offset to the base element**

2. Java vs Python
```python
pop(i) -> pop ith element
insert(i) -> insert into ith pos
remove('狗蛋') 
index('狗蛋')
reverse()
```
```Java
int[] b = new int[5];
int[] c= new int[] {5, 4, 0, 6, 1};

b.length;
```
**sort**
```java
Arrays.sort(p, (b, c) -> (b.age - c.age));

/** Return a negative (positive) number if b's first
 * name comes before (or after) c's first name.
 * If b's and c's first names are the same,
 * return b's age - c's age. */
public static int before(Person b, Person c) {
 int n= b.first.compareTo(c.first);
 if (n != 0) return n;
 return b.age - c.age;
}

Arrays.sort(p, (b, c) -> before(b, c));
```
**Insert a element**
```java
/**insert an element into the an array */

static void addPos(int[] array, int pos, int value) {
    int prev = value
    // initially set to value parameter so the first iteration, the value is replaced by it
    for(int i = pos; i < array.length; i++) {
        int tmp = array[i]
        array[i] = prev
        prev = tmp
    }
}

// if you want to delete a element, 
arr[i] = arr[i+1] 
```
