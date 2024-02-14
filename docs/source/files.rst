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

  python3 calibration_data.py --omega_lambda 0.7 --omega_m 0.3 --sigma8 0.8 --gamma 0.2 --M 7.5 --n 3e-3 --z 0.092


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

  python3 calibration_mocks.py --omega_lambda 0.7 --omega_m 0.3 --sigma8 0.8 --gamma 0.2 --M 7.5 --n 3e-3 --z 0.092 --space real --particles Haloes

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

  python3 constraints.py --sim [21.9375, 12.125, 6.3125, 2.78125, 0.90625, 0.0625]



direct_formalism.py
---------------------

The `direct_formalism.py` script facilitates the calculation of the Void Probability Function (VPF) and the number of voids (nvoids) for a given cosmological model. It offers the flexibility to choose between the two functions and allows customization of various cosmological parameters and analysis settings.

Usage
.....

To perform the calculations, users can run the script `direct_formalism.py` with the following command-line arguments:

- `function`: Choose between "nvoids" or "P0" to calculate the respective function.
- `--omega_lambda`: Value for omega_lambda.
- `--omega_m`: Value for omega_m.
- `--sigma8`: Value for sigma8.
- `--gamma`: Value for gamma.
- `--M`: Value for M.
- `--n`: Value for n.
- `--z`: Value for z (redshift).
- `--space`: Real or Redshift space.
- `--rmin`: Minimum value for r.
- `--rmax`: Maximum value for r.
- `--deltar`: Spacing between r values.
- `--output_file`: Name of the file to save the table.

Functionality
.............

The script computes the chosen function, generates a table with results, and saves the table to a file if specified. Additionally, it produces a plot illustrating the calculated function.

Example Command
...............

::
  python3 direct_formalism.py nvoids --omega_lambda 0.7 --omega_m 0.3 --sigma8 0.8 --gamma 0.2 --M 7.5 --n 3e-3 --z 0.092 --space real --rmin 1 --rmax 10 --deltar 0.1 --output_file nvoids_results.txt



Functions.py
--------------




likelihood.py
----------------


The `likelihood.py` module contains classes for handling the calibration of the formalism (`CalibratedFormalism`) and calculating likelihoods based on simulation data (`Likelihood`). This module is a key component for assessing the statistical agreement between the calibrated formalism and the simulated data.

`CalibratedFormalism` Class
...........................

The `CalibratedFormalism` class initializes a calibrated cosmological model using specified parameters. It calculates function values, including Void Probability Function (VPF), and saves the results to a file. The class also includes methods for calculating `ap` and `a` values necessary for likelihood computations.

`Likelihood` Class
..................

The `Likelihood` class reads a calibrated formalism file and simulation values, then calculates the likelihood for different combinations of sigma8 and gamma parameters. It produces a likelihood table, saves it to a file, and generates a contour plot illustrating the confidence levels.

Example Usage
.............

Calibrating Formalism:
.....................

::

  calibrated_model = CalibratedFormalism(0.7, 0.3, 0.8, 0.2, 1e14, 0.95, 0.5, True)
  calibrated_model.calculate_function_vals(r_values, sigma_values, gamma_values, uchuu_data)

Calculating Likelihood:
.....................

::

  likelihood_calculator = Likelihood('calibrated_formalism.txt', simulation_values)
  likelihood_calculator.calculate_likelihood()


run.py
-------


The `run.py` script provides a command-line interface to perform various tasks related to the cosmological simulations, formalism calibration, and parameter constraints. The script allows users to choose from different options:

1. Calculate Nvoids or VPF
..........................

- **Option 1:** Calculate Nvoids
    - Calculates the Void Probability Function (VPF) using the direct formalism.
    - Users provide cosmological parameters, simulation details, and output file information.

- **Option 2:** Calculate VPF
    - Calculates the Volume Probability Function (VPF) using the direct formalism.
    - Users provide cosmological parameters, simulation details, and output file information.

2. Calibrate Formalism
.......................

- **Option 3:** Calibrate Formalism
    - Calibration of the formalism based on high-resolution simulations (Uchuu halo simulation box, Uchuu-SDSS galaxy simulation box, or Uchuu-SDSS light-cone).
    - Users choose the type of simulation and space (real or redshift).

3. Constrain Sigma8 and Gamma
.............................

- **Option 4:** Constrain Sigma8 and Gamma
    - Constrain cosmological parameters (Sigma8 and Gamma) using likelihood calculations.
    - Users choose the simulation sample to constrain and specify whether it's in real or redshift space.

Notes
.....
- Ensure necessary dependencies are installed, including `numpy`, `subprocess`, and other project-specific modules.
- Follow the provided prompts for input parameters and options.
- Option 4 requires prior calibration (Option 3) for accurate parameter constraints.



simulations.py
----------------
This module contains classes that define different cosmological simulations for both halo and galaxy datasets. The simulations include various parameters such as mass (M), number density (n), redshift (z), and cosmological parameters (omega_lambda, omega_m, sigma8, gamma).

`HaloSimulations` Class
........................

- The `HaloSimulations` class represents simulations of dark matter haloes.
- **Attributes:**
    - `name`: Name of the simulation (e.g., 'Uchuu', 'P18', 'Low', 'VeryLow').
    - `space`: Space in which the simulation is conducted ('real' or 'redshift').
    - `M`: Mass parameter for the simulation.
    - `n`: Number density parameter for the simulation.
    - `z`: Redshift parameter for the simulation.
    - `sim`: Array representing the simulation results for different radial bins.
    - Cosmological parameters (omega_lambda, omega_m, sigma8, gamma) specific to each simulation.

`GalaxySimulations` Class
.........................

- The `GalaxySimulations` class represents simulations of galaxies.
- **Attributes:**
    - `name`: Name of the simulation (e.g., 'Uchuu').
    - `space`: Space in which the simulation is conducted ('real' or 'redshift').
    - `M`: Mass parameter for the simulation.
    - `n`: Number density parameter for the simulation.
    - `z`: Redshift parameter for the simulation.
    - `sim`: Array representing the simulation results for different radial bins.
    - Cosmological parameters (omega_lambda, omega_m, sigma8, gamma) specific to each simulation.

Example Usage:
.............

::
  # Example usage of HaloSimulationsuchuu_halo_real = HaloSimulations('Uchuu', 'real')
  print(f"Simulation Name: {uchuu_halo_real.name}")
  print(f"Simulation Space: {uchuu_halo_real.space}")
  print(f"Number Density: {uchuu_halo_real.n}")
  print(f"Simulation Results: {uchuu_halo_real.sim}")

::
  # Example usage of GalaxySimulations
  uchuu_galaxy_real = GalaxySimulations('Uchuu', 'real')
  print(f"Simulation Name: {uchuu_galaxy_real.name}")
  print(f"Simulation Space: {uchuu_galaxy_real.space}")
  print(f"Number Density: {uchuu_galaxy_real.n}")
  print(f"Simulation Results: {uchuu_galaxy_real.sim}")





