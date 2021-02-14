# knapsack-problem-simpleai
Solving knapsack problem via simpleai




A- Problem Formulation

At first the program asks the user to enter the number of items, knapsack capacity, weights of each item, and values of each item.

In the def randomCharChange method, a random character in the list is assigned to the variable initNmber and makes 1 if its value is 0, and 0 if it is 1.

In the def actions method, randomCharChange method is called and the current state is sent and it is assigned to changedState variable. Then changedState is returned. This method is used for hill climbing search and hill climbing with random restarts.

In the def result method, randomCharChange method is returned. This method is used for hill climbing search and hill climbing with random restarts.

In the def value method, values list is converted to string and it assigned to listValues, the values in listValues is assigned to lv. The values in lv and listValues are multiplied and cumulatively added with totalValue. In the same way, weights list is converted to string and it assigned to listWeights, the weights in listWeights is assigned to lw. The in lw and listWeights are multiplied and cumulatively added with totalWeights. If totalWeights is greater than knapsackCapacity returned 0. Else returned totalValue.

In the def generate_random_state method, there is a variable called numbers which is contains 0 and 1. These numbers generates a list called resultStr and then resultStr is returned.

In the def crossover method, two cut points are randomly determined and they are crossed with each other (they are replaced and combined) to assign a variable named child. Then child is returned. This method is used for genetic algorithms.

In the def mutate method, a mutation_point is determined and if current state is equals to mutation_point 0’s are made 1, 1’s are made 0. This method is used for genetic algorithms.


B-  Discussion on the Results

Local search algorithms do not have a frontier, there is an only the current state and i try to make better it by looking at neighboring nodes. In this way, it is faster and memory efficient because it takes up much less space in memory with a single state. In these algorithms, i start from a random initial state and define an objective function for each state. Objective function (value) gives information about how good that state is.
 
1-	Hill Climbing Search

In this search algorithm, a random initial point is determined and which is better is preferred by looking at the neighbors. This algorithm always moves uphill. If its neighbor’s value is smaller or equal than itself, it returns the current state. This algorithm is usually complete but if the current state did not return where the current state’s value is equal to its neighbor’s value and continued to go to its neighbor, it would be incomplete when the neighbor was infinite. Also, this algorithm works fast, however generally i can get stuck in local maximum and cannot find the global maximum. So, the solution i found may not always be optimal. In the knapsack problem, i could not find the optimal solution in this reason.

An example;

Number of items: 4

Knapsack capacity: 25

Weights of each item: 24 – 18 – 18 – 10

Values of each item: 24 – 10 – 10 – 7

When i gave the initial state as 0101, the solution returned 0001 but the optimal solution was 1000.

Another example with different inputs:

Number of items: 3

Knapsack capacity: 50

Weights of each item: 10 – 20 – 30

Values of each item: 60 – 100 – 120

When i gave the initial state as 0101, the solution returned 0111 but the optimal solution was 0011.So with the different input values i tried, hill climbing did not give an optimal result.


2-	Hill Climbing with Random Restarts

In order to solve the local maximum problem that i experience in hill climbing search, with the new starting points i randomly choose, i can apply the solution repeatedly until i find the optimal solution.

An example:

Number of items: 4

Knapsack capacity: 25

Weights of each item: 24 – 18 – 18 – 10

Values of each item: 24 – 10 – 10 – 7
 

When i gave the initial state as 0101 and restarts limit as 10, the solution gave the result 1000 which was optimal. But when i gave the restarts limit as 5, it gave the result 0100 and again could not find the optimal result. So, the higher i give the restarts limit, the greater our chances of finding the optimal solution.

Another example with different inputs:

Number of items: 3

Knapsack capacity: 50

Weights of each item: 10 – 20 – 30

Values of each item: 60 – 100 – 120

When i gave the initial state as 0101 and restarts limit as 5, the solution gave the result 0011 which was optimal. In the previous example with different input values, when i gave the restart limit as 5, i could not find the optimal, but in this example i could find the optimal solution.

3-	Genetic Algorithm

In this search algorithm, combining parent states generates a successor state and states are called individual. There are k randomly generated individuals in terms of a single state. These individuals generate population. Each individual in the population has a chromosome. There is an objective function is also called fitness function and the higher the fitness function, the better the genes of that individual. New generations are created with selection, crossover and mutation.

After crossover and mutation, the fitness function of each individual of the new generation is calculated and a new population is created again, and it continues in a loop. According to the fitness function, two random individuals are selected and crossed, mutated with a small possibility. New individuals formed are added to the population. This loop continues until i find a fit enough individual. In this algorithm, i may not always find or reach the optimal result. The algorithm returns the individual with best fitness function.

An example:

Number of items: 4

Knapsack capacity: 25

Weights of each item: 24 – 18 – 18 – 10

Values of each item: 24 – 10 – 10 – 7

When i gave the initial state as 0101 and mutation chance as 0.001 the solution gave the result 1000 which was optimal.

Another example with different inputs:

Number of items: 3

Knapsack capacity: 50

Weights of each item: 10 – 20 – 30

Values of each item: 60 – 100 – 120
 

When i gave the initial state as 0101 and mutation chance as 0.9 the solution gave the result 0011 which was optimal. Although i increased the mutation chance, it still gave the optimal solution.
