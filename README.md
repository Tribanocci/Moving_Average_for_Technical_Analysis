# Moving_Average_for_Technical_Analysis

A **Flask** project of a web-application that implements a stock's buy/sell policy simulation on actual data from stock's timeseires.

The project is deployed and running, [here](https://konstantinos2.pythonanywhere.com/).

## Table of Contents

- [Moving\_Average\_for\_Technical\_Analysis](#moving_average_for_technical_analysis)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Project Website](#project-website)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)


## Description

The policy that is simulated in the web-app utilizes the Moving Average (MA) technique for prediction changes in the trend of the timeseries. The parametres that can be controlled is the MA window, the initial capital, and the percentage of the capital that will be invested in each buy decision. Also, for more accurate results the buy or sell decision will be made after a number of *days* that the trend has not changed.

**This project is under development with the objective of making a database that stores users trials for comparison and conclusions**

## Project Website

Visit the [Project Website](https://example.com), where the app is up and running.

## Installation

In order to use modify and run the web-app locally, you must:

1. Install *VS Code*.
2. Install dependencies (Flask and plotly), using the VS code terminal.
   1.  pip install Flask
   2.  pip install --user Flask plotly
3. Run the app, *python -m flask run*     

## Usage

This policy is not a reccomended or guarented method for invseting your capital, but rather a developing project for educational purposes of implementing computational *Python* scripts in *Web* enviroments and using the *Flask* framework. 

## Contributing

By testing the running up, discovering issues. Also there is an open issue of making a database that keeps track of the parameters that a user has tried, so the comparison and conclusion process is easier and more user-friendly.

