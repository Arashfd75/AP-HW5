import math

class pyGausssolver:
    #m_pf = m_A = m_B = m_N = 0

    def __init__(self, pf, a, b, n):
        self.m_pf = pf
        self.m_A = a
        self.m_B = b
        self.m_N = n

    def legendre(self, m_N, x):
        #print(m_N)
        if m_N == 0 :
            return 1
        elif m_N == 1:
            return x
        else:
            return ((2.0 * m_N - 1) / m_N) * x * self.legendre(m_N - 1, x) - ((1.0 * m_N - 1) / m_N) * self.legendre(m_N - 2, x)

    def dLegendre(self, m_N, x):
        dLegendre = (1.0 * m_N / (x * x - 1)) * ((x * self.legendre(m_N, x)) - self.legendre(m_N - 1, x))
        return dLegendre

    def legendreZeroes(self, m_N, i):
        #print("lenegndreZeros start")
        
        xold1 = math.cos(math.pi * (i - 1 / 4.0) / (m_N + 1 / 2.0))
        xnew1 = xold1 + 1
        iteration = 1
        while(1 + math.fabs(xnew1 - xold1)) > 1.:
            if(iteration != 1):
                xold1 = xnew1
            xnew1 = xold1 - self.legendre(m_N, xold1) / self.dLegendre(m_N, xold1)
            iteration += 1
        #    print("xold: ",xold1)
        #    print("xnew: ",xnew1)
        #    print('iteration: ',iteration)
        #print("lenegndreZeros end")
        return xnew1

    def weight(self, m_N, x):
            weightI = 2 / ((1 - x**2) * (self.dLegendre(m_N, x))**2)
            return weightI

    def exec(self):
            integral = 0
            for i in range(self.m_N):
                #print("i :",i)
                #print('m_N :' ,self.m_N)
                integral = integral + self.m_pf(self.legendreZeroes(self.m_N, i + 1)) * self.weight(self.m_N, self.legendreZeroes(self.m_N, i + 1))
            self.m_Result = ((self.m_B - self.m_A) / 2.0) * integral
        
    def getResult(self):
            return self.m_Result