from typing import Tuple
from experiments.utils import observables
from src.o1_test_for_chaos import O1TestForChaos

def classify_eca_rule(
    rule:int,
    n_angles:int, lattice_width:int,
    n_iterations:int, initial_condition:int, 
    ignore_initial_transient:int   
) -> Tuple[int,float]:
    print(f"rule:{rule} = ...calculating")
    result = O1TestForChaos.test_for_chaos(
        n_angles=n_angles,
        observables=observables(
            max_time=n_iterations+ignore_initial_transient,
            eca_rule=rule,
            dimension=lattice_width, 
            ic=initial_condition
        )[ignore_initial_transient:]
    )
    print(f"rule:{rule} = {result}")
    return rule,result
