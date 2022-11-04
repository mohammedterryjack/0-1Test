from typing import Generator, Tuple
from src.utils import observables, equivalent_eca_rules

def classify_eca_rules(
    n_angles:int, rules:List[int], lattice_width:int,
    n_iterations:int, initial_condition:int, ignore_initial_transient:int   
) -> Generator[Tuple[int,float],None,None]:
    for rule in rules:
        yield (
            rule, 
            O1TestForChaos.test_for_chaos(
                n_angles=n_angles,
                observables=observables(
                    max_time=n_iterations,
                    eca_rule=rule,
                    dimension=lattice_width, 
                    ic=initial_condition
                )[ignore_initial_transient:]
            )
        )

if __name__ == "__main__":
    results = list(classify_eca_rules(
        n_angles=10,
        rules=list(equivalent_eca_rules()),
        lattice_width=637,
        n_iterations=1000,
        ignore_initial_transient=10,
        initial_condition=157772325949337114751228396077633682068852574612949832419054851897545068335997284508864138640431125523412626177597802569043207131753005708372421948440114274698313298513533339618679949586869846
    ))
