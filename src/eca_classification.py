from typing import Generator, Dict
from json import dumps 

from src.utils import observables


def classify_eca_rules(
    n_angles:int, n_rules:int, lattice_width:int,
    n_iterations:int, initial_condition:int    
) -> Dict[int,float]:
    measurements = _chaos_test_on_eca_rules(
        n_angles=n_angles,
        n_rules=n_rules,
        lattice_width=lattice_width,
        n_iterations=n_iterations,
        initial_condition=initial_condition
    )
    return dict(zip(range(n_rules),measurements))

def _chaos_test_on_eca_rules(
    n_angles:int, n_rules:int, lattice_width:int,
    n_iterations:int, initial_condition:int
) -> Generator[float,None,None]:
    for rule in range(n_rules):
        phi = observables(max_time=n_iterations,eca_rule=rule,dimension=lattice_width, ic=initial_condition)
        yield O1TestForChaos.test_for_chaos(observables=phi,n_angles=n_angles)
        
        
        
        
if __name__ == "__main__":
    results = classify_eca_rules(
        n_angles=10,
        n_rules=256,
        lattice_width=637,
        n_iterations=318,
        initial_condition=157772325949337114751228396077633682068852574612949832419054851897545068335997284508864138640431125523412626177597802569043207131753005708372421948440114274698313298513533339618679949586869846
    )
    with open("results/classification.json","w") as results_file:
        results_file.write(dumps(results,indent=2))
