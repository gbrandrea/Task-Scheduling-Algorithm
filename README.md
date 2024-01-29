# Task Scheduling Algorithm <a name="top"></a>

An algorithm for task scheduling with resource constraints.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction <a name="introduction"></a>

This project implements two task scheduling algorithms. The first one uses a brute-force approach to find the optimal schedule (Branch&Bound), while the second one employs the A* search algorithm for an optimized solution.

## Features <a name="features"></a>

- Brute-force task scheduling
- A* search-based task scheduling
- Support for task dependencies, durations, resources, and constraints

## Getting Started <a name="getting-started"></a>

### Prerequisites <a name="prerequisites"></a>

- Python 3.x
- NumPy library

### Installation <a name="installation"></a>

1. **Clone the repository:**

    ```bash
    git clone https://github.com/gbrandrea/task-scheduling-algorithm.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd task-scheduling-algorithm
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    This project relies on the NumPy library. The requirements file ensures that you have all the necessary dependencies installed.

4. **Explore the project:**

    You're all set! Feel free to explore and use the task scheduling algorithms.

## Usage <a name="usage"></a>

This project should be used by running the "useYourTasks" class. You will be asked to give the basic information for the task, and you will
have to choose the algorithm you want to use. Then an array of the "instant to begin each task" will be given to you. You can also execute the "algEx" class to run the examples
and check how this works!

## License <a name="license"></a>

This project is licensed under the GNU General Public License v2.0 - see the [LICENSE](LICENSE) file for details.
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)

[Back to Top](#top)

