from typing import Generator, Tuple
from experiments.utils import observables, equivalent_eca_rules, parallel_map
from src.o1_test_for_chaos import O1TestForChaos

def classify_eca_rules(
    n_angles:int, lattice_width:int,
    n_iterations:int, initial_condition:int, 
    ignore_initial_transient:int   
) -> Generator[Tuple[int,float],None,None]:
    return parallel_map(
        lambda rule: classify_eca_rule(
            rule=rule,
            n_angles=n_angles, 
            lattice_width=lattice_width,
            n_iterations=n_iterations, 
            initial_condition=initial_condition, 
            ignore_initial_transient=ignore_initial_transient   
        ),
        equivalent_eca_rules()
    )

def classify_eca_rule(
    rule:int,
    n_angles:int, lattice_width:int,
    n_iterations:int, initial_condition:int, 
    ignore_initial_transient:int   
) -> Tuple[int,float]:
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
