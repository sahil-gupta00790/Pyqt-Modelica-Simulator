# OpenModelica Desktop Application

## Overview

A Python based desktop application for executing Openmodelica simulations. This application provides a GUI to run OpenModelica model executables with customizable start and stop times.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [1. Install OpenModelica](#1install-openmodelica)
  - [2. Clone the repository](#2clone-the-repository)
  - [3. Install the dependencies](#3install-the-dependencies)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
    - [1. Launch the application](#1launch-the-application)
    - [2. Using the interface](#2using-the-interface)
- [Project Structure](#project-structure)
- [Development](#development)
  - [Code Standards](#code-standards)
  - [OOP Implementation](#oop-implementation)
- [Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)

## Features

- File selection for OpenModelica executables
- Configurable start and stop time
- Model execution with parameters

## Prerequistes

- Windows 10/11
- Python 3.6 or higher
- OpenModelica(latest version)

## Installation

### 1. Install Openmodelica

Download from https://openmodelica.org/

### 2. Clone the repository

```bash
git clone https://github.com/sahil-gupta00790/Pyqt-Modelica-Simulator
cd Pyqt-Modelica-Simulator
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

## Usage

## Running the Application

### 1. Launch the application

```bash
python main.py
```

### 2. Using the interface 
-Click "Browse" to select your OpenModelica Executable, or choose the inbuilt TwoConnectedTanks model by checking the default button 

-Enter Start and Stop Time(0<=Start time<Stop time<5>) 

-Additionally, you can choose whether you want '.mat' or '.csv' file as output 

-Click on "Execute Simulation" to execute 

-You can also download the result in the directory you wish 


## Project Structure
```
PyQt-Modelica-Simulator/
├── model/                          # Model-related files and executables
│   ├── executables/                # Contains compiled OpenModelica executables
│   │   └── TwoConnectedTanks.exe   # Main simulation executable
│   └── NonInteractingTanks/        # Non-interacting tanks model files
│
├── src/                            # Source code directory
│   ├── gui/                        # GUI-related components
│   │   └── widgets/                # Custom PyQt widgets and UI elements
│   └── utils/                      # Utility functions and helper modules
│
└── requirements.txt                # Python package dependencies
```

## Development

### Code Standards

This project follows PEP8 standards for Python code.

### OOP Implementation

The application is built using Object-Oriented Programming Principles:

-Encapsulation of GUI components
 
-Inheritance of widgets 

-Reusebale code structure 

## TroubleShooting

### Common Issues

1.OpenModelica Executable Not Found: 

-Ensure the executable path is correct 

-Check file permissions 


2.Simulation Error 

-Check for OpenModelica installlation 

-Add Path to OpenModelica's bin to environment variables 

---
Developed as part of the FOSSEE screening task




