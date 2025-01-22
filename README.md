<!-- omit in toc -->
# Symbolic Regression using Genetic Programming
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Contributors](https://img.shields.io/badge/Contributors-4-brightgreen)
![Commits](https://img.shields.io/badge/Commits-28-blue)
![Python](https://img.shields.io/badge/python-3.10-blue)


This repository contains an implementation of a Symbolic Regression algorithm, using a tree-based **Genetic Programming** (GP) evolutionary technique. The algorithm evolves mathematical expressions in order to find the model that best fits a given set of data in the form $(X, y)$. By leveraging *selection*, according to a fitness measure, *mutation* and *crossover*, the SR algorithm generates mathematical formulas that are able to capture the complex patterns present in the input data.

## Key Features
- **Island Model Genetic Algorithm**
  - The population is divided into a certain number of **subpopulations** (a.k.a. *islands*) which evolve separately and can occasionaly exchange individuals (a.k.a *migration*) in order to avoid local optima and rapid convergence;
  - At each migration event, according to a migration rate parameter, one or more individuals migrate from the source island to another random island, as a way to ensure equal chance of genetic mixing across islands.
- **Tree-Based Representation**
  - The evolutionary algorithm iteratively evolves a population of mathematical formulas, represented as full and grow trees;
  - Internal nodes are randomly chosen from function set (arithmetic, trigonometric, logarithmic and exponential operators), while leaves are randomly chosen from terminal set (constants and variables).
- **Elitism**
  - To preserve high-quality solutions, the best individuals (a.k.a. *elites*) are directly inserted into the next generation, without being subjected to any change.
- **Parents Selection**
  - Different parents selection strategies are implemented. Fitness-proportional, rank based and tournament selection.
- **Mutation and Crossover**
  - Various mutation mechanisms are implemented. Replaced a subtree with a new one (`mutate_subtree`) or modify a single node (`mutate_single_node`) in the selected parent tree;
  - Combine two different trees for generating new offsprings. This allows the algorithm to explore new regions in the search space, encouraging exploration instead of exploitation.

## How it works
- **Initialization**
  - A population of individuals (*trees*) is initialized on each island. Depending on the value assigned to the variable `grow_full_ratio`, each island's population is initialized with a number of full trees and grow trees;
  - In each of the `ISLAND_NUM` islands, there are `ISLAND_POPULATION` individuals.
- **Selection**
  - Parents are selected based on their fitness (in which measure the mathematical formula represented by the tree fits well the data provided as input), using various strategies (*e.g.* rank-based selection).
- **Reproduction**
  - Offsprings are generated through mutation and crossover genetic operators.
- **Evolution**
  - Over the course of generations, populations on the islands evolve and only the best performing trees survive.
- **Convergence**
  - The evolutionary process continues for a certain number of generations (`MAX_GENERATIONS`).

## Project Structure
The project is organized as follows:
- `sym_reg.ipynb`
  - The Jupyter notebook through which it is possible to experiment with Symbolic Regression using Genetic Programming. Thank to parent selection, mutation and crossover genetic operators, it is possible to find a mathematical formula that well fit the given dataset.
  ```python
  x[0] + np.sin(x[1]) / 5   # a simple mathematical formula for problem 0
  ```
- `tree.py`
  - The .py file that contains the **Tree** class, the main component of the project. This class provides methods for generating grow and full trees, methods for computing the fitness and methods for mutation and crossover.
- `data/`
  - A folder that contains eight different input problems (*npz* files). Each problem is represented by a dataset that can be used to train and test the model.
- `pyproject.toml`
  - The configuration file containing dependencies and metadata for the project. *Poetry* is used for package management.


## Results

### Problem 1

**MSE**: 7.125940794232773e-34

`np.sin(x[0])`

### Problem 2

**MSE**: 988168974158.1375

`(((((-62.24357039260542 + (x[0] * x[1])) + ((x[0] * x[1]) + 6.459417617857545)) + ((5.517038333390751 * x[0]) * np.reciprocal((1.5827088050437421 / x[2])))) * (((x[1] * 4.978572892293439) - ((7.885793211722174 * x[2]) / -1.641003402164408)) + (9.63237170280645 * x[0]))) * ((((x[1] * 18.649830776786864) * np.reciprocal((-3.6182647063354416 / x[2]))) + ((x[0] * (2.6184311110488068 * x[2])) +253.6732340675021)) * (((-82.29170605396563 + (x[0] * x[1])) + np.absolute((-9.996265568395703 * x[0]))) / 3.340770779277813)))`

### Problem 3

**MSE**: 2.1040318682789047e-07

`((np.arctan((((x[2] -  -2.065621497047198) /  3.7609747965545135) +  14.11482758558892))  *  2.6622227984463516) +  -((((np.square(x[0])  *  -2.0) + (3.503326125821749  / np.reciprocal(x[2]))) + (x[1]  * np.square(x[1])))))`

### Problem 4

**MSE**: 2.549390095890441e-10

`((np.cos(x[1])  *  7.000000792991886) + (((1.6102655062320324  - np.power((15.27657903079583  + x[0]), -4.681065427551907)) - np.power(2.2239667716288487, (-10.64590793887777  - np.power(1.4396983786605233, x[0])))) * ((-8.731509378683597  + ((14.312198011080312  - x[0]) /  -2.490229650218498)) /  -7.108999793736638)))`

### Problem 5

**MSE**: 1.2025552044142602e-22

`(4.356153822762008e-11  * ((0.18873497848879503  + (-4.311704549797579  + np.power(np.sqrt(x[0]), x[1]))) / (-4.311704549797579  / (3.8872132896946994  + np.power(np.sqrt(x[0]), x[1])))))`

### Problem 6

**MSE**: 9.43339182827304e-10

`(((9.570811396234019  / (3.2990756682061715  / x[1])) /  1.7120363063134838) + (((x[0]  *  -0.342886656605085) /  0.9853790256442974) *  1.9959027865438197))`

### Problem 7

**MSE**: 33.49950798557632

`(np.power(np.power(np.square((x[1] - x[0])), (x[0] /  -5.56363914354592)), (x[0] +  0.09503004875559984))  - ((0.5529900399168103  * np.absolute((x[1] * x[0]))) / (-1.0085421764494056  + np.cos((x[1] - x[0])))))`

### Problem 8

**MSE**: 11036.894432056677

`((((-7540.826857026908  - (np.power(2.2224115547003684, x[1])  - (x[0]  - x[2]))) / ((-19.741842726315273  * np.exp(x[5])) *  -3.9779795080988234)) + (((np.square(x[5])  *  -32.660938490698086) *  -1.6711840162616087) + ((-18.385241718800962  / np.exp(x[4])) - (1.3232421025458017  * (x[3]  *  -19.98753306315633))))) + (((x[5]  - np.power(0.9422005781130904, np.exp(x[5]))) * ((np.square(x[5])  * np.square(x[5])) - (-16.345502872293693  * np.exp(x[5])))) + ((((x[5]  *  17.60134866937029) + (x[5]  *  17.60134866937029)) /  -0.26962500598603156) - ((np.exp(x[4])  *  18.34079626746933) - (125.55888927167379  - (x[3]  *  -18.55592643985281))))))`



## Contributing
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
      <a href="https://github.com/FerraiuoloP">
        <img src="https://github.com/FerraiuoloP.png" width="50px" style="border-radius: 50%; border: none;" alt=""/>
        <br />
        <sub>FerraP</sub>
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