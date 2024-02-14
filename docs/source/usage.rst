Quick Usage
===========

After installation, you can execute the code using the provided bash script in the main folder::

    ./run.sh

Upon running the script, you will be presented with four **options**::

1. Calculate nvoids

2. Calculate VPF

3. Calibrate formalism

4. Constrain sigma8 and gamma


3.1 Running Options 1 and 2
---------------------------

If you choose option 1 or 2, you will we ask the following parameters
    * omega_lambda: dark energy density parameter (float)
    * omega_m: matter density parameter (float)
    * sigma8: linear spectrum of density fluctuations (float)
    * gamma: shape of the spectrum (float)
    * Mass: (float)
    * n: number density of dark matter particles, dark matter haloes o galaxies (float)
    * z: redshift (float)
    * space: real or redshift (string)
    * rmin: minimun radius for the calculation of nvoids or VPF (float)
    * rmax: maximum radius for the calculation of nvoids or VPF (float)
    * deltar: radius bin width (float)
    * output_file: name of the file where radius and nvoids or VPF will be saved (string)

When you run Option 1 or 2, two files will be generated in formalism/ folder. The first one is the ```output_file``` with two columns: radius and nvoids or VPF. The second file is a .png plot called nvoids_function.png or vpf_function.png. 

3.2 Running Option 3
--------------------

If you choose to run option 3, you will be given 3 options more:

1. Using Uchuu halo simulation box
2. Using Uchuu-SDSS galaxy simulation box
3. Using Uchuu-SDSS galaxy light-cones

If you choose option 1 (option 2), then you will be able to constrain sigma8 and gamma in other halo (galaxy) simulation boxes. If you choose 3, then you will be able to constrain sigma8 and gamma in a redshift survey, like SDSS.

If you choose option 1 or 2, you will have to enter real or redshift space (string), and the enter the minimum and maximum values and bin width for sigma8 and gamma (these will be the values used to constrain sigma8 and gamma in Maximum Likelihood Test). If you choose option 3, only redshift space is available.  

In future versions you will be able to calibrate the formalism with your own simulations.

***Note: It is necessary to run this Option before running optin 4!!!!***


3.3 Running Option 4
--------------------

If you intend to use option 4, ensure that you have executed option 3 first, as the file generated in step 3 is necessary for step 4.

When you choose Option 4, you will be given 7 options more:

1. Uchuu halo box
2. P18 halo box
3. Low halo box
4. VeryLow halo box
5. Uchuu-SDSS galaxy box
6. Uchuu-SDSS light-cones
7. SDSS

These are different simulation boxes (Options 1-5), light-cones (Option 6) and redshift surveys (Option 7) you can use to infer their sigma8 and gamma values. If you choose a simulation box, you can choose between real and redshift space. If you choose light-cones or SDSS redshift space is automatically established.
