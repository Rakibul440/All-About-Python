# Random Module
Here are some examples of using the Python random module:

1. Generate a random float between 0.0 and 1.0
```
import random
print(random.random())
```
2. Generate a random integer between 1 and 10
```
import random
print(random.randint(1, 10))
```

3. Choose a random element from a list
```
import random
my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))
```

4. Shuffle a list
```
import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
```

5. Generate a random sample from a population
```
import random
population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.sample(population, 3))
```

6. Generate a random float between -10.0 and 10.0
```
import random
print(random.uniform(-10.0, 10.0))
```

7. Generate a random integer between -5 and 5
```
import random
print(random.randint(-5, 5))
```

8. Choose a random element from a list with weights
```
import random
my_list = ['apple', 'banana', 'cherry']
weights = [0.5, 0.3, 0.2]
print(random.choices(my_list, weights=weights)[0])
```

9. Seed the random number generator
```
import random
random.seed(42)
print(random.random())
```

These examples demonstrate various ways to use the random module in Python. You can use these functions to generate random data for testing, simulations, or other purposes.