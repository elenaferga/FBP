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

  python calibration_data.py --omega_lambda 0.7 --omega_m 0.3 --sigma8 0.8 --gamma 0.2 --M 7.5 --n 3e-3 --z 0.092


calibration_mocks.py
---------------------
The `calibration_mocks.py` script plays a vital role in calibrating mocks, specifically targeting Uchuu dark matter haloes or Uchuu-SDSS galaxies within the project's formalism. It utilizes command-line arguments to customize the calibration process based on various cosmological parameters and simulation details.

Usage
.....

To initiate the calibration of mocks, users can run the script `calibration_mocks.py` with the following optional command-line arguments:

- `--omega_lambda`: Value for omega_lambda
- `--omega_m`: Value for omega_m
- `--sigma8`: Value for sigma8
- `--gamma`: Value for gamma
- `--M`: Value for M
- `--n`: Value for n
- `--z`: Value for z (redshift)
- `--space`: Real or Redshift space
- `--particles`: Haloes or Galaxies

Calibration Process
...................

The script fetches simulation data based on user-specified space (real or redshift) and particle type (haloes or galaxies) from the Uchuu dataset. It then utilizes the `CalibratedFormalism` class to perform the calibration, prompting the user to input minimum and maximum values along with step sizes for sigma8 and gamma.

Example Command
...............

::

  python calibration_mocks.py --omega_lambda 0.7 --omega_m 0.3 --sigma8 0.8 --gamma 0.2 --M 7.5 --n 3e-3 --z 0.092 --space real --particles Haloes

constraints.py
---------------

The `constraints.py` script is designed to compute constraints on the parameters sigma8 and gamma based on the likelihood calculations using calibrated formalism. It serves as a crucial step in the project, providing insights into the statistical likelihood of parameter values given the observational data.

Usage
.....

To execute the constraints calculation, users can run the script `constraints.py` with the following optional command-line argument:

- `--sim`: An array representing simulation data for the likelihood calculation.

Constraints Calculation
.......................

The script checks for the existence of the file `calibrated_formalism.txt` in the `/formalism` folder. If the file is found, it utilizes the `Likelihood` class from the `likelihood` module to calculate the log-likelihood based on the provided simulation data array. The results offer valuable constraints on the sigma8 and gamma parameters.

Example Command
...............

::

  python constraints.py --sim [0.7, 0.3, 0.8, 0.2, 1e14, 0.95, 0.5, True]





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

