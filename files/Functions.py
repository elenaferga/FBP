import numpy as np
from scipy.integrate import quad, quad_vec
import math

class CosmologyModel:
    def __init__(self, omega_lambda, omega_m, omega_c, sigma8, h, M, n, z, space):
        #First, the cosmological parameters omega_lambda, omega_m, sigma8 and h have to be defined
        #M is the mass
        #n is the number density of galaxies
        #z is redshift
        #space is Boolean: True if Real space, False if Redshift space.

        self.omega_lambda = omega_lambda
        self.omega_m = omega_m
        self.sigma8 = sigma8
        self.h = h
        self.gamma = h*omega_c
        self.M = M
        self.n = n
        self.z = z
        self.space = space

    def Qfun(self, x, r):
        return r * (1 + self.DELT(x))**(1/3)

    def AA(self, x, r):  # A7
        p1 = 1.577 - 0.298 * self.Qfun(x, r) / 8
        p2 = (0.0557 + 0.00447 * self.Qfun(x, r) / 8) * np.log(self.M)
        p3 = (0.00565 + 0.0018 * self.Qfun(x, r) / 8) * (np.log(self.M))**2
        return p1 - p2 - p3

    def BB(self, x, r):  # A8
        p1 = 0.0025 - 0.00146 * self.Qfun(x, r) / 8
        p2 = (0.121 - 0.0156 * self.Qfun(x, r) / 8) * self.M**(0.335 + 0.019 * self.Qfun(x, r) / 8)
        return p1 + p2

    def A(self, x, r):  # A5
        return self.AA(x, r) * ((self.D(self.z) * self.sigma8 / 0.9)**0.88) * ((self.gamma / 0.21)**0.174)

    def B(self, x, r):  # A6
        return self.BB(x, r) * ((self.D(self.z) * self.sigma8 / 0.9)**(-2.55)) * ((self.gamma / 0.21)**(-0.82))

    def DELT(self, x):  # A4
        return (1 - 0.607 * x)**(-1.66) - 1

    def DELK(self, x):
        cte = 1.676 / 1.68647
        p1 = 1.68647
        p2 = 1.35 * (1 + x)**(-2/3)
        p3 = 1.12431 * (1 + x)**(-1/2)
        p4 = 0.78785 * (1 + x)**(-0.58661)
        return cte * (p1 - p2 - p3 + p4)

    def DELK_derivada(self, x):
        cte = 1.676 / 1.68647
        p2 = (-2 / 3) * 1.35 * (1 + x)**(-2/3 - 1)
        p3 = (-1 / 2) * 1.12431 * (1 + x)**(-1/2 - 1)
        p4 = (-0.58661) * 0.78785 * (1 + x)**(-0.58661 - 1)
        return cte * (-p2 - p3 + p4)

    def VEL(self, x):
        den = (1 + self.z)**3 + self.omega_lambda / self.omega_m
        der1 = 1.06 * ((1 + self.z)**(3) / den)**0.6
        cte = -1 / 3
        return cte * der1 * self.DELK(x) / ((1 + x) * self.DELK_derivada(x))

    def DELF(self, x, r):  # A3
        a = 1 + self.DELT(x)
        Q = self.Qfun(x, r)
        p1 = abs(1 - (4 / 21) * (a**(2 / 3)) * (self.sigma(Q))**2)
        return (a / p1) - 1

    def u(self, x, r):  # A2
        V = (4 / 3) * math.pi * r**3
        cte = self.n * V * self.A(x, r) * (1 + self.DELF(x, r))
        b = self.B(x, r)
        e = np.exp(-b * x**2)
        if self.space == True:
            Acte = 0
        elif self.space == False:
            Acte = 0
        else:
            raise Exception("Space variable must be boolean! True for real space and False for redshift space.")
        return cte * e * (1 + Acte * (1.4 / r)**2)

    def sigma(self, y):  # A13
        p1 = 2.01 + 3.9 * self.gamma
        p2 = 0.2206 + 0.361 * self.gamma**1.5
        p3 = 0.182 + 0.0411 * np.log(self.gamma)
        return self.sigma8 * p1 * y**(-p2 - p3 * np.log(y)) * self.D(self.z) / self.D(0)

    def alfa(self, x, r):  # A12
        p1 = 0.173 * np.log(self.Qfun(x, r) / 10)
        return 0.54 + p1

    def P(self, x, r):  # A12
        a = r * (1 + self.DELF(x, r))**(1 / 3)
        den = self.sigma(a)**2
        p1 = np.exp(-0.5 * x**2 / den)
        p2 = (1 + self.DELF(x, r))**(-1 + self.alfa(x, r) / 2)

        der = 1.00001
        cte_aux = 1 / (der - 1)
        cte = cte_aux / x

        b = r * (1 + self.DELF(der * x, r))**(1 / 3)
        sigmaa = self.sigma(a)
        sigmab = self.sigma(b)

        derivada = (der * x / sigmab - x / sigmaa) * cte
        return p1 * p2 * derivada / np.sqrt(2 * math.pi)

    def P0(self, r):
        integrand = lambda x: self.P(x, self.ERRE(r, x))*np.exp(-self.u(x, self.ERRE(r, x)))
        return quad_vec(integrand, -7, -0.0001)[0]

    def E(self, redshift):
        result = np.sqrt(self.omega_m * (1 + redshift) ** 3 + self.omega_lambda)
        return result

    def D(self, redshift):
        integrand = lambda x: (1 + x) / self.E(x)**3
        I = quad(integrand, redshift, np.inf)[0]
        norm = self.E(0) * quad(integrand, 0, np.inf)[0]
        return self.E(redshift) * I / norm

    def ERRE(self, r, x):
        if self.space == True:
            epsilon = 0
        elif self.space == False:
            epsilon = 0.85
        else:
            raise Exception("Space variable must be boolean! True for real space and False for redshift space.")
        return r * (1 + self.VEL(self.DELT(x)))**(-epsilon / 3)

    def K(self, r):
        cte = -1 / 3
        delt = 1.00001
        frac = np.log(self.P0(r * delt) / self.P0(r)) / np.log(delt)
        return (cte * frac)**3 * self.P0(r)

    def nvoids(self, r):
        a = self.K(r)
        nu = 0.558
        cte1 = 1.6708
        cte2 = 0
        V = (4 / 3) * math.pi * r**3
        cte = nu * a / V
        sup = -cte1 * a * (1 - cte2 * a)
        condition = (a <= 0.46)
        result = np.where(condition, cte * np.exp(sup), 0.313 / V)
        return result



    def omega(self, nvoids, rbarra):
        cte1 = 32*math.pi/3
        res = []
        for i in range(len(nvoids)):
            cte2 = (2.73*nvoids[i]*32*math.pi*rbarra**3)/3
            cte3 = (3*nvoids[i]**(-1/3))/(4*2*rbarra)
            cte4 = ((nvoids[i]/(2*rbarra))**2)/8
            aux = cte1*(1+cte2*(1-cte3+cte4))**(-1)
            res.append(aux)
        return res

    def rmsP0(self, vpf, nvoids, rbarra, nvoidssim, M):
        res = []
        om = self.omega(nvoids, rbarra)
        for i in range(len(vpf)):
            cte1=9.2*(1-om[i]*nvoids[i])*(vpf[i]**2)/nvoidssim[i]
            cte2 = vpf[i]/M
            res.append(cte1+cte2)
        return res
