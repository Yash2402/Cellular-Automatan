# Cellular-Automatan

A Cellular Automaton consists of a regular grid of cells, each in one of a finite number of states, such as on and off (in contrast to a coupled map lattice). The grid can be in any finite number of dimensions. For each cell, a set of cells called its neighborhood is defined relative to the specified cell. An initial state (time t = 0) is selected by assigning a state for each cell. A new generation is created (advancing t by 1), according to some fixed rule (generally, a mathematical function) that determines the new state of each cell in terms of the current state of the cell and the states of the cells in its neighborhood. Typically, the rule for updating the state of cells is the same for each cell and does not change over time, and is applied to the whole grid simultaneously, though exceptions are known, such as the stochastic cellular automaton and asynchronous cellular automaton.

# Cellular Automaton Simulation

Simulate cellular automata with this project, allowing you to explore and visualize dynamic patterns emerging from simple rules.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Configuring Rules](#configuring-rules)
  - [Running the Simulation](#running-the-simulation)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

Cellular automata are discrete, abstract mathematical models that consist of a grid of cells. Each cell evolves over time based on a set of predefined rules, creating fascinating and complex patterns. This project provides a platform to simulate and observe cellular automata in action.

## Getting Started

Follow these steps to get started with the Cellular Automaton Simulation.

### Prerequisites

Ensure you have the following prerequisites installed:

- Python 3.X
- Pygame 2.1.2

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Yash2402/Cellular-Automaton.git

   ```

2. Navigate to the directory Cellular-Automaton:
   ```bash
   cd Cellular-Automaton
   ```
3. Install requirements:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
4. Run the python file `main.py` :
   ```bash
   python3 main.py
   ```

## Usage

### Rules

1. To select different elements:
   - `1` : Sand
   - `2` : Water
   - `3` : Smoke
   - `4` : Wall
2. To pause the simulation:
   - `space`
3. To reset:
   - `r`
