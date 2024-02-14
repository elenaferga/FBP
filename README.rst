FBP-formalism
=============

1. Overview
------------

(nombre) is a Python-based project designed for efficient cosmological computations. The project predicts the Void Probability Function (VPF, i.e, the probability that a randomly placed sphere with radius $r$ is empty of objects -- galaxies or dark matter) and the number density of voids larger than $r$, $\bar{n}_{v}(r)$. Additionally, given $\bar{n}_{v}(r)$, the code is able to constrain the values of sigma8 and gamma using the Maximum Likelihood test.

2. Installation
---------------

First, you have to download this repository and cd to the folder::

    git clone https://github.com/elenaferga/FBP.git
    cd FBP

To install the necessary dependencies, including CGAL (https://www.cgal.org/) and DIVE (https://github.com/cheng-zhao/DIVE), follow these steps::

    python3 install.py


3. Usage
--------

After installation, you can execute the code using the provided bash script::

    ./run.sh

Upon running the script, you will be presented with four **options**::

1. Calculate nvoids

2. Calculate VPF

3. Calibrate formalism

4. Constrain sigma8 and gamma


3.1 Running Options 1 and 2
---------------------------

If you choose option 1 or 2, you will we ask the following parameters
- omega_lambda: dark energy density parameter (float)
- omega_m: matter density parameter (float)
- sigma8: linear spectrum of density fluctuations (float)
- gamma: shape of the spectrum (float)
- Mass: (float)
- n: number density of dark matter particles, dark matter haloes o galaxies (float)
- z: redshift (float)
- space: real or redshift (string)
- rmin: minimun radius for the calculation of nvoids or VPF (float)
- rmax: maximum radius for the calculation of nvoids or VPF (float)
- deltar: radius bin width (float)
- output_file: name of the file where radius and nvoids or VPF will be saved (string)

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

4. Citations
------------

Please, if you use this code in your work, cite 
    * mi paper :)

If you use Uchuu halo box in your work, cite 
    * The Uchuu Simulations: Data Release 1 and Dark Matter Halo Concentrations by [Ishiyama, T., Prada, F., Klypin, A., et al. (2021)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.506.4210I/abstract)

If ou use Uchuu-SDSS galaxy box or Uchuu-SDSS light-cones in your work, cite 
    * Uchuu-SDSS galaxy lightcones: a clustering, RSD and BAO study by [Dong-Páez, C. A., Smith, A., Szewciw, A. O., et al. 2024,](https://ui.adsabs.harvard.edu/abs/2021MNRAS.506.4210I/abstract)

***ME FALTA MENCIONAR QUE REFERENCIEN AL PAPER AL USAR AL CÓDIGO O AL USAR ALGUNA DE LAS SIMULACIONES NUEVAS ***


*For additional information or inquiries, feel free to contact the project contributors.*

*Note: This README provides a brief overview and installation guide. Detailed documentation and explanations can be found within the project files.*
