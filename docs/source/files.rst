.. _formalism_folder:

Formalism Folder
================

This folder contains several files that play essential roles in the formalism of the project. Below is a brief overview of each file:

calibration_data.py
--------------------
Contains a perform_calibration(args) function in order to calibrate redshift survey (SDSS) using CalibratedFormalism class from likelihood.py file. In order to run this code, the following line has to be written in shell::

  python3 calibration_data.py --omega_lambda {omega_lambda} --omega_m {omega_m} --sigma8 {sigma8} --gamma {gamma} --M {M} --n {n} --z {z} --space {space}

calibration_mocks.py
---------------------
Handles the generation and manipulation of calibration mocks for the project.

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

