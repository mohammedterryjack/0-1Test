from typing import List,Generator,Optional
from math import e,pi,log
from scipy.stats import linregress
from statistics import median, stdev

from numpy import cumsum
from matplotlib.pyplot import imshow, plot, show, xlabel,ylabel

class O1TestForChaos:
    @staticmethod
    def _transform(observables:List[float],angle:float) -> Generator[complex,None,None]:
        for t,phi_t in enumerate(observables):
            yield phi_t * e**(1j*t*angle)

    @staticmethod
    def transform(observables:List[float],angle:float,display:bool=False) -> List[complex]:
        z = cumsum(list(O1TestForChaos._transform(observables=observables,angle=angle)))
        if display:
            plot(z.real,z.imag)
            xlabel("Real(z)")
            ylabel("Imag(z)")
            show()
        return z.tolist()

    @staticmethod
    def _mean_square_displacement_term(a:complex) -> float:
        return a.real **2 + a.imag **2

    @staticmethod
    def _mean_square_displacement(transformed_data:List[complex], N:int) -> Generator[float,None,None]:
        T = len(transformed_data)
        for n in range(1,N):        
            m = sum(map(
                lambda t:O1TestForChaos._mean_square_displacement_term(
                    a = transformed_data[n+t] - transformed_data[t]
                ), 
                range(T-N)
            ))
            yield m/(T-N)

    @staticmethod
    def mean_square_displacement(transformed_data:List[complex], N:int, display:bool=False) -> List[float]:
        M = list(O1TestForChaos._mean_square_displacement(transformed_data=transformed_data,N=N)) 
        if display:
            plot(M)
            xlabel("n")
            ylabel("M")
            show()
        return M

    @staticmethod
    def correlation_coefficient(mean_square_displacement:List[float], N:int, display:bool=False) -> float:
        log_M = list(map(lambda M_n:log(M_n) if M_n else 0.0,mean_square_displacement))
        log_N = list(map(log,range(1,N)))
        slope, intercept, K, _, _ = linregress(log_N, log_M)
        if display:
            best_fit = list(map(lambda value:slope*value+intercept, log_N))
            plot(log_N,log_M)
            plot(log_N, best_fit)
            xlabel("log N")
            ylabel("log M")
            show()
        return K

    @staticmethod
    def _test_for_chaos(observables:List[float],n_angles:int,N:int,display:bool) -> Generator[float,None,None]:
        for n in range(1,n_angles+1):
            z = O1TestForChaos.transform(observables=observables, angle=2*pi/n,display=display and n==n_angles)
            M = O1TestForChaos.mean_square_displacement(transformed_data=z, N=N,display=display and n==n_angles) 
            K = O1TestForChaos.correlation_coefficient(mean_square_displacement=M, N=N, display=display and n==n_angles)
            yield K

    @staticmethod
    def test_for_chaos(observables:List[float],n_angles:int,N:Optional[int]=None,display:bool=False) -> float:
        Ks = sorted(O1TestForChaos._test_for_chaos(
            observables=observables,
            n_angles=n_angles,
            N=len(observables)//10 if N is None else N,
            display=display
        ))
        if display:
            angles = list(map(lambda n:2*pi/n,  range(1,len(Ks)+1)))
            plot(angles,Ks)
            xlabel("angle")
            ylabel("K")
            show()
        return median(Ks)
