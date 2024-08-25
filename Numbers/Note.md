# Difference between repr(),str(),print()
In Python, repr(), str(), and print() are related but serve different purposes:

1. repr():
    - Returns a string representation of an object, intended for debugging and logging.
    - Should ideally be a valid Python expression that could recreate the object.
    - Typically includes the object's type and its attributes.
    - Example: repr([1, 2, 3]) returns "[1, 2, 3]"
2. str():
    - Returns a human-readable string representation of an object.
    - Meant for end-users, not debugging.
    - Should be concise and informative.
    - Example: str([1, 2, 3]) returns "[1, 2, 3]"
3. print():
    - Outputs text to the console or a file.
    - Can take any object as an argument, which is then converted to a string using str().
    - Adds a newline character at the end, unless specified otherwise.
    - Example: print([1, 2, 3]) outputs "[1, 2, 3]" followed by a newline.

## Key differences:

- repr() is for debugging, while str() is for human-readable output.
- repr() should be a valid Python expression, while str() is more flexible.
- print() outputs text, while repr() and str() return strings.

## When to use each:

- repr(): Logging, debugging, or when you need a string that can recreate the object.
- str(): User-facing output, like GUI labels or console messages.
- print(): Outputting text to the console or a file, often using the result of str().