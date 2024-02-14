.. _formalism_folder:

Formalism Folder
================

This folder contains several files that play essential roles in the formalism of the project. Below is a brief overview of each file:

calibration_data.py
--------------------

The `calibration_data.py` file serves as a crucial component for calibrating a redshift survey (SDSS) within the project's formalism. It provides a command-line interface for user interaction and leverages the `CalibratedFormalism` class from the `likelihood` module and the `CosmologyModel` class from `Functions` module.

Usage
.....

To initiate calibration, users can run the script `calibration_data.py` with the following optional command-line arguments:

- `--omega_lambda`: Value for omega_lambda
- `--omega_m`: Value for omega_m
- `--sigma8`: Value for sigma8
- `--gamma`: Value for gamma
- `--M`: Value for M
- `--n`: Value for n
- `--z`: Value for z (redshift)

Calibration Process
...................

The script prompts the user to input minimum and maximum values along with step sizes for sigma8 and gamma. It then utilizes the `Uchuu` simulation data and the `CalibratedFormalism` class to calibrate the formalism, producing a successful calibration of the project's formalism.

Example Command
...............

::

  python calibration_data.py --omega_lambda 0.7 --omega_m 0.3 --sigma8 0.8 --gamma 0.2 --M 1e14 --n 0.95 --z 0.5


calibration_mocks.py
---------------------
Contains a perform_calibration(args) function in order to calibrate mocks (dark matter particles, dark matter haloes or galaxies) using CalibratedFormalism class from likelihood.py file. In order to run this code, the following line has to be written in shell::

  python3 calibration_mocks.py --omega_lambda {omega_lambda} --omega_m {omega_m} --sigma8 {sigma8} --gamma {gamma} --M {M} --n {n} --z {z} --space {space} --particles {particles}

constraints.py
---------------
Defines and manages constraints applied within the formalism of the project.

direct_formalism.py
---------------------
Implements the direct formalism aspects crucial to the project.

Functions.py
--------------
Houses various functions utilized across the formalism for efficient code organization.

likelihood.py
----------------
Handles the calculation of likelihood values for the project.

run.py
-------
Serves as the main script to execute the project, orchestrating the overall workflow.

simulations.py
----------------
Manages the simulations carried out as part of the project.

Feel free to refer to the respective files for detailed information on their functions and usage.

