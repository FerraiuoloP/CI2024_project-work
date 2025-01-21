<!-- omit in toc -->
# Symbolic Regression using Genetic Programming
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Contributors](https://img.shields.io/badge/Contributors-4-brightgreen)
![Python](https://img.shields.io/badge/python-3.10-blue)

## Commits and logs
**I worked in a group with [my colleagues](#contributors), the official repository that contains all the commits I made is [CI2024_Project](https://github.com/FerraiuoloP/CI2024_Project).**

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
  - To preserve high-quality solutions, the best individuals (a.k.a. *elites*) are directly inserted into the next generation, without being subjected to any change.

- **Parents Selection**
  - Different parents selection strategies are implemented and can be selected as hyperparameter: fitness-proportional, rank based and tournament selection.
  
- **Mutation and Crossover**

  - Various mutation mechanisms are implemented. Replace a subtree with a new one (`mutate_subtree`) or modify a single node (`mutate_single_node`) in the selected parent tree. The mutations are implemented in such a way to assure that the resulting tree is still valid.
  
  - Combine two different trees for generating new offsprings. This allows the algorithm to explore new regions in the search space, encouraging exploration instead of exploitation.

- **Mutation and Crossover**

  - Various mutation mechanisms are implemented. Replace a subtree with a new one (`mutate_subtree`) or modify a single node (`mutate_single_node`) in the selected parent tree. The mutations are implemented in such a way to assure that the resulting tree is still valid.
  
  - Combine two different trees for generating new offsprings. This allows the algorithm to explore new regions in the search space, encouraging exploration instead of exploitation.

- **Collapse strategy**
	- A tree can be collapsed with some probability: certain branches are pruned or reduced in depth, generating a new formula that remains equivalent to the original one.

- **Take over detection**
	- If in an island most of the individuals are the same the population is trimmed and new individuals are generated.

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

- `sym_reg.ipynb`: The Jupyter notebook through which it is possible to experiment with Symbolic Regression using Genetic Programming. Thank to parent selection, mutation and crossover genetic operators, it is possible to find a mathematical formula that well fit the given dataset.
  
  ```python
  x[0] + np.sin(x[1]) / 5   # a simple mathematical formula for problem 0
  ```
  
- `tree.py`: The .py file that contains the **Tree** class, the main component of the project. This class provides methods for generating grow and full trees, methods for computing the fitness and methods for mutation and crossover.
- `data/`:  A folder that contains eight different input problems (*npz* files). Each problem is represented by a dataset that can be used to train and test the model.
- `pyproject.toml`: The configuration file containing dependencies and metadata for the project. *Poetry* is used for package management.

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
