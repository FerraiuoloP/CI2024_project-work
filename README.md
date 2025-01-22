<!-- omit in toc -->
# Symbolic Regression using Genetic Programming
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Contributors](https://img.shields.io/badge/Contributors-4-brightgreen)
![Python](https://img.shields.io/badge/python-3.10-blue)

## Important: commits and logs
**I worked in a group with [my colleagues](#contributors), the official repository that contains every commit I made is [CI2024_Project](https://github.com/FerraiuoloP/CI2024_Project).**

## Description
An implementation of a Symbolic Regression algorithm, using a tree-based **Genetic Programming** (GP) evolutionary technique has been proposed. The algorithm evolves mathematical expressions in order to find the model that best fits a given set of data in the form $(X, y)$. By leveraging *selection*, according to a fitness measure, *mutation* and *crossover*, the SR algorithm generates mathematical formulas that are able to capture the complex patterns present in the input data.

## Key Features
- **Tree-Based Representation**
  - The evolutionary algorithm iteratively evolves a population of mathematical formulas, represented as full and grow trees.
  - Internal nodes are randomly chosen from function set (arithmetic, trigonometric, logarithmic and exponential operators), while leaves are randomly chosen from terminal set (constants and variables).
  
- **Population constraint**: every individual/formula in the population has to be valid:
	- Contains at least one instance of each variable of the problem set.
	- Must be consistent with the fundamental principles of the mathematical system (e.g. no divisions by 0). This boundary is checked by trying to compute the MSE for each one of them, and catching errors.

- **Island Model Genetic Algorithm**
  - The population is divided into a certain number of **subpopulations** (a.k.a. *islands*) which evolve separately and can occasionaly exchange individuals (a.k.a *migration*) in order to avoid local optima and rapid convergence;
  - At each migration event, according to a migration rate parameter, one or more individuals migrate from the source island to another random island, as a way to ensure equal chance of genetic mixing across islands.
  - The  migration happens in a probablistic way, at every iteration a random individual could be selected to migrate from an island to another one. 

- **Elitism**
  - To preserve high-quality solutions, the best individuals (a.k.a. *elites*) are directly duplicated to the next generation, without being subjected to any change. 

- **Parents Selection**
  - Different parents selection strategies are implemented and can be selected as hyperparameter: fitness-proportional, rank based and tournament selection.
  
- **Mutation and Crossover**

  - Various mutation mechanisms are implemented. Replace a subtree with a new one (`mutate_subtree`) or modify a single node (`mutate_single_node`) in the selected parent tree. The mutations are implemented in such a way to assure that the resulting tree is still valid.
  
  - Combine two different trees for generating new offsprings. This allows the algorithm to explore new regions in the search space, encouraging exploration instead of exploitation.

- **Collapse strategy**
	- A tree can be collapsed with some probability: certain branches are pruned or reduced in depth, generating a new formula that remains equivalent to the original one.

- **Take over detection**
	- Since an elitism strategy is implemented, it could happen that most of the population in an island will be composed of the same individual. To address this, and promote diversity, the population is trimmed by keeping only unique individuals and generating the rest of the population.

## How it works
- **Initialization**
  - A population of individuals (*trees*) is initialized on each island. Depending on the value assigned to the variable `grow_full_ratio`, each island's population is initialized with a number of full trees and grow trees;
  - In each of the `ISLAND_NUM` islands, there are `ISLAND_POPULATION` individuals.
- **Selection**
  - Parents are selected based on their fitness (in which measure the mathematical formula represented by the tree fits well the data provided as input), using various strategies (*e.g.* rank-based selection).
- **Reproduction**
  - Offspring are generated through mutation and crossover genetic operators.
- **Evolution**
  - Over the course of generations, populations on the islands evolve and only the best performing trees survive.
- **Convergence**
  - The evolutionary process continues for a certain number of generations (`MAX_GENERATIONS`).

## Project Structure
The project is organized as follows:

- `src/sym_reg.ipynb`: The Jupyter notebook through which it is possible to experiment with Symbolic Regression using Genetic Programming. Thank to parent selection, mutation and crossover genetic operators, it is possible to find a mathematical formula that well fit the given dataset.
  
  ```python
  x[0] + np.sin(x[1]) / 5   # a simple mathematical formula for problem 0
  ```
  
- `src/tree.py`: The .py file that contains the **Tree** class, the main component of the project. This class provides methods for generating grow and full trees, methods for computing the fitness and methods for mutation and crossover.

- `data/`:  A folder that contains eight different input problems (*npz* files). Each problem is represented by a dataset that can be used to train and test the model.

- `src/pyproject.toml`: The configuration file containing dependencies and metadata for the project. *Poetry* is used for package management.

## Results

Note: 
- **Each formula contains at least one instance of each variable.**
- The formulas have been found using np operators, and then the basic operators (+,-,/,*) have been replaced
	(using the flag `use_std_operators` in the code) to enhance the readability.
- A balanced approach between formula complexity (in depth) and MSE has been prioritized.
- Different hyperparameters have been used during different runs.

### Problem 1

**MSE**: 7.125940794232773e-34

	`np.sin(x[0])`

### Problem 2

**MSE**: 715200995203.6115

```python
(((((-51.81814669987016  + (x[0]  * x[1])) + np.maximum((x[0] * x[1]), -4.884217383927211)) + ((4.893313914157078  * x[0]) * np.reciprocal((1.5827088050437421  / x[2])))) * (((x[1]  *  4.953136254469275) - (-4.884217383927211  * x[2])) + (9.996265568395703  * np.minimum(x[0], 4.356894927194286)))) * ((((x[1]  *  18.649830776786864) * np.reciprocal((-3.493460646283637  / x[2]))) + ((x[0]  * (2.510264066743016  * x[2])) -  -248.23328707719287)) * (((-82.50101783674046  + (x[0]  * x[1])) + np.absolute((-9.996265568395703  * x[0]))) /  3.0042241506957357)))
```

### Problem 3

**MSE**: 2.1040318682789047e-07

```python
((np.arctan((((x[2] -  -2.065621497047198) /  3.7609747965545135) +  14.11482758558892))  *  2.6622227984463516) +  -((((np.square(x[0])  *  -2.0) + (3.503326125821749  / np.reciprocal(x[2]))) + (x[1]  * np.square(x[1])))))
```

### Problem 4

**MSE**: 8.414776260505279e-12

```python
((7.000000614701995  * np.cos(np.reciprocal(np.reciprocal(x[1])))) - ((((x[0]  + x[0]) -  3.1292631691925386) /  21.99978866375695) -  3.1371774184176267))
```

### Problem 5

**MSE**: 1.2025552044142602e-22

```python
(4.356153822762008e-11  * ((0.18873497848879503  + (-4.311704549797579  + np.power(np.sqrt(x[0]), x[1]))) / (-4.311704549797579  / (3.8872132896946994  + np.power(np.sqrt(x[0]), x[1])))))
```

### Problem 6

**MSE**: 2.5369781053059546e-12

```python
((0.6946269287372357  * (-0.9998472454638713  * np.minimum(8.692112438892295, x[0]))) + (-7.69887037157223  / (-4.543393686903389  / x[1])))
```

### Problem 7

**MSE**: 30.24296185210098

```python
(np.power(np.power(np.square((x[1] - x[0])), (x[0] /  -5.239844422536422)), (np.minimum(1.896493075050202, x[0]) + np.remainder(x[1], 0.17997037571963403)))  - ((0.5318365347088865  * np.square(x[1])) / (-1.0085421764494056  + np.cos((x[1] - x[0])))))
```

### Problem 8

**MSE**: 7931.582292760899

```python
((((-7540.826857026908  - (np.square(x[1])  - (x[2]  + x[0]))) / ((-19.741842726315273  * np.exp(x[5])) *  -3.9779795080988234)) + (((np.square(x[5])  *  -32.660938490698086) *  -1.6690374979040925) + ((-18.385241718800962  / np.exp(x[4])) - (-4.963012888395526  * np.sinh(x[3]))))) + (((x[5]  - np.power(0.9422005781130904, np.exp(x[5]))) * ((np.square(x[5])  * np.square(x[5])) - (-16.345502872293693  * np.exp(x[5])))) + ((((x[5]  *  17.60134866937029) + (x[5]  *  17.60134866937029)) /  -0.26962500598603156) - ((np.exp(x[4])  *  18.34079626746933) - (122.0987615004006  + (9.539347080016679  * x[3]))))))
```



## Contributors
<table>
  <tr>
    <td align="center" style="border: none;">
      <a href="https://github.com/AgneseRe">
        <img src="https://github.com/AgneseRe.png" width="50px" style="border-radius: 50%; border: none;" alt=""/>
        <br />
        <sub>AgneseRe</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/GDennis01">
        <img src="https://github.com/GDennis01.png" width="50px" style="border-radius: 50%; border: none;" alt=""/>
        <br />
        <sub>GDennis01</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/XhoanaShkajoti">
        <img src="https://github.com/XhoanaShkajoti.png" width="50px" style="border-radius: 50%; border: none;" alt=""/>
        <br />
        <sub>XhoanaShkajoti</sub>
      </a>
    </td>
  </tr>
</table>

## License
This project is licensed under the MIT License.
