import subprocess
from simulations import HaloSimulations, GalaxySimulations
import numpy as np

def calculate_nvoids(omega_lambda, omega_m, sigma8, gamma, M, n, z, space, rmin, rmax, deltar, output_file):
    command = f"python3 direct_formalism.py nvoids --omega_lambda {omega_lambda} --omega_m {omega_m} --sigma8 {sigma8} --gamma {gamma} --M {M} --n {n} --z {z} --space {space} --rmin {rmin} --rmax {rmax} --deltar {deltar} --output_file {output_file}"
    subprocess.run(command, shell=True)

def calculate_VPF(omega_lambda, omega_m, sigma8, gamma, M, n, z, space, rmin, rmax, deltar, output_file):
    command = f"python3 direct_formalism.py P0 --omega_lambda {omega_lambda} --omega_m {omega_m} --sigma8 {sigma8} --gamma {gamma} --M {M} --n {n} --z {z} --space {space} --rmin {rmin} --rmax {rmax} --deltar {deltar} --output_file {output_file}"
    subprocess.run(command, shell=True)


def calibrate_mocks(omega_lambda, omega_m, sigma8, gamma, M, n, z, space, particles):
    command = f"python3 calibration_mocks.py --omega_lambda {omega_lambda} --omega_m {omega_m} --sigma8 {sigma8} --gamma {gamma} --M {M} --n {n} --z {z} --space {space} --particles {particles}"
    subprocess.run(command, shell=True)


def calibrate_data(omega_lambda, omega_m, sigma8, gamma, M, n, z, space):
    command = f"python3 calibration_data.py --omega_lambda {omega_lambda} --omega_m {omega_m} --sigma8 {sigma8} --gamma {gamma} --M {M} --n {n} --z {z} --space {space}"
    subprocess.run(command, shell=True)



def constrain(sim):
    sim = np.array(sim, dtype=float)
    command = f"python3 constraints.py --sim {sim}"
    subprocess.run(command, shell=True)



def main():
    print("Options:")
    print("1. Calculate nvoids")
    print("2. Calculate VPF")
    print("3. Calibrate formalism")
    print("4. Constrain sigma8 and gamma (Step 3 is necessary in order to run constrain the parameters!)")

    option = input("Enter your choice (1-4): ")

    if option == "1":
        omega_lambda = float(input("Enter omega_lambda: "))
        omega_m = float(input("Enter omega_m: "))
        sigma8 = float(input("Enter sigma8: "))
        gamma = float(input("Enter gamma: "))
        M = float(input("Enter Mass: "))
        n = float(input("Enter n: "))
        z = float(input("Enter z: "))
        space = input("Enter space: ")
        rmin = float(input("Enter rmin: "))
        rmax = float(input("Enter rmax: "))
        deltar = float(input("Enter deltar: "))
        output_file = input("Enter output_file: ")

        calculate_nvoids(omega_lambda, omega_m, sigma8, gamma, M, n, z, space, rmin, rmax, deltar, output_file)

    elif option == "2":
        omega_lambda = float(input("Enter omega_lambda: "))
        omega_m = float(input("Enter omega_m: "))
        sigma8 = float(input("Enter sigma8: "))
        gamma = float(input("Enter gamma: "))
        M = float(input("Enter Mass: "))
        n = float(input("Enter n: "))
        z = float(input("Enter z: "))
        space = input("Enter space: ")
        rmin = float(input("Enter rmin: "))
        rmax = float(input("Enter rmax: "))
        deltar = float(input("Enter deltar: "))
        output_file = input("Enter output_file: ")

        calculate_VPF(omega_lambda, omega_m, sigma8, gamma, M, n, z, space, rmin, rmax, deltar, output_file)



    elif option == "3":
        print('Only Uchuu available for now...')
        typesim = input("Do you want to use Uchuu halo simulation box (1), Uchuu-SDSS galaxy simulation box (2) or Uchuu-SDSS light-cone (3)?. Press 1, 2 or 3... ")
        if(typesim=='1'):
            space = input("Enter space: ")
            omega_lambda = HaloSimulations('Uchuu', space).omega_lambda
            omega_m = HaloSimulations('Uchuu', space).omega_m
            sigma8 = HaloSimulations('Uchuu', space).sigma8
            gamma = HaloSimulations('Uchuu', space).gamma
            M=HaloSimulations('Uchuu', space).M
            n=HaloSimulations('Uchuu', space).n
            z=HaloSimulations('Uchuu', space).z

            print('Setting the parameters of the high-resolution simulation box... ')
            print('Omega_lambda= ', omega_lambda)
            print('Omega_m= ', omega_lambda)
            print('sigma8= ', sigma8)
            print('Gamma= ', gamma)
            print('Mass= ', M)
            print('n= ', n)
            print('z= ', z)

            calibrate_mocks(omega_lambda, omega_m, sigma8, gamma, M, n, z, space, 'Haloes')


        if(typesim=='2'):
            print('Setting the parameters of the high-resolution simulation box... ')
            space = input("Enter space: ")
            omega_lambda = GalaxySimulations('Uchuu', space).omega_lambda
            omega_m = GalaxySimulations('Uchuu', space).omega_m
            sigma8 = GalaxySimulations('Uchuu', space).sigma8
            gamma = GalaxySimulations('Uchuu', space).gamma
            M=GalaxySimulations('Uchuu', space).M
            n=GalaxySimulations('Uchuu', space).n
            z=GalaxySimulations('Uchuu', space).z

            print('Setting the parameters of the high-resolution simulation box... ')
            print('Omega_lambda= ', omega_lambda)
            print('Omega_m= ', omega_lambda)
            print('sigma8= ', sigma8)
            print('Gamma= ', gamma)
            print('Mass= ', M)
            print('n= ', n)
            print('z= ', z)

            calibrate_mocks(omega_lambda, omega_m, sigma8, gamma, M, n, z, space, 'Galaxies')



        elif(typesim=='3'):
            print('Setting the parameters of the high-resolution simulation light-cone... ')
            omega_lambda = 0.6911
            omega_m = 0.3089
            sigma8 = 0.8159
            gamma = 0.20924886
            M=7.5
            n=3.03e-3
            z=0.079896

            print('Omega_lambda= ', omega_lambda)
            print('Omega_m= ', omega_lambda)
            print('sigma8= ', sigma8)
            print('Gamma= ', gamma)
            print('Mass= ', M)
            print('n= ', n)
            print('z= ', z)
            space = 'redshift'

            calibrate_data(omega_lambda, omega_m, sigma8, gamma, M, n, z, space)


    elif option == "4":
        print("Which sample do you want to constrain?")
        print("Options:")
        print("1. Uchuu halo box")
        print("2. P18 halo box")
        print("3. Low Halo box")
        print("4. VeryLow Halo box")
        print("5. Uchuu-SDSS galaxy box")
        print("6. Uchuu-SDSS light-cones")
        print("7. SDSS")

        typesim = input("Enter your choice (1-7): ")


        if(typesim=='1'):
            option = input("In real or redshift space? Print 'real' or 'redshift... ")
            if(option=='real'):
                Uchuu = HaloSimulations('Uchuu', 'real')
                constrain(Uchuu.sim)

            elif(option=='redshift'):
                Uchuu = HaloSimulations('Uchuu', 'redshift')
                constrain(Uchuu.sim)


        elif(typesim=='2'):
            option = input("In real or redshift space? Print 'real' or 'redshift... ")
            if(option=='real'):
                P18 = HaloSimulations('P18', 'real')
                constrain(P18.sim)

            elif(option=='redshift'):
                P18 = HaloSimulations('P18', 'redshift')
                constrain(P18.sim)


        elif(typesim=='3'):
            option = input("In real or redshift space? Print 'real' or 'redshift... ")
            if(option=='real'):
                Low = HaloSimulations('Low', 'real')
                constrain(Low.sim)

            elif(option=='redshift'):
                Low = HaloSimulations('Low', 'redshift')
                constrain(Low.sim)


        elif(typesim=='4'):
            option = input("In real or redshift space? Print 'real' or 'redshift... ")
            if(option=='real'):
                VeryLow = HaloSimulations('VeryLow', 'real')
                constrain(VeryLow.sim)

            elif(option=='redshift'):
                VeryLow = HaloSimulations('VeryLow', 'redshift')
                constrain(VeryLow.sim)


        elif(typesim=='5'):
            option = input("In real or redshift space? Print 'real' or 'redshift... ")
            if(option=='real'):
                Uchuu = GalaxySimulations('Uchuu', 'real')
                constrain(Uchuu.sim)

            elif(option=='redshift'):
                Uchuu = HaloSimulations('Uchuu', 'redshift')
                constrain(Uchuu.sim)



if __name__ == "__main__":
    main()
