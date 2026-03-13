# Aerodesign Control Surface Calculator

Python tool developed to assist in the preliminary sizing of control surfaces for RC aircraft used in Aerodesign projects.

The program calculates tail volumes and proposes possible geometric configurations for stabilizers and control surfaces based on common aerodynamic design guidelines.

## Features

The code performs calculations for:

* Horizontal Stabilizer (EH)
* Vertical Stabilizer (EV)
* Ailerons
* Rudder
* Elevator

It also:

* Calculates tail areas based on tail volume coefficients
* Computes rudder lift using aerodynamic coefficients
* Generates aerodynamic plots using `matplotlib`
* Provides multiple configuration options for design exploration

## Project Background

This tool was developed in **2021** during an **Aerodesign project** with the goal of automating preliminary design calculations for control surfaces of an RC aircraft.

Instead of manually testing multiple geometry combinations, the script generates several feasible configurations for the stabilizers and control surfaces.

## Aerodynamic Parameters Used

The code uses standard aerodynamic design parameters such as:

* Wing span
* Wing chord
* Wing area
* Tail volume coefficients
* Air density
* Flight velocity
* Aerodynamic coefficients (`Cl`, `Cn`)

## Required Files

The program reads aerodynamic data from three external files:

```
Cl (A x L).txt
Cl (Cn x L).txt
Cn.txt
```

These files must contain one coefficient value per line.

Example:

```
0.1
0.2
0.3
0.4
```

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/aerodesign-control-surfaces.git
```

Install required dependencies:

```
pip install matplotlib
```

## Running the Program

Run the script:

```
python main.py
```

You will see a menu in the terminal:

```
[0] Tail volumes
[1] Control surface dimensions
[2] Aerodynamic graphs
[3] Exit
```

## Example Outputs

The program can display:

* Tail volume areas
* Possible control surface dimensions
* Lift vs Cl plots
* Cn vs Cl plots

## Authors

Developed in 2021 by:

* **Eliaquim Lima**
* **Giovanni Gonçalves**

## License

This project is released under the MIT License.
