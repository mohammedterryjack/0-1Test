from typing import List,Optional,Generator, Any, Iterable
from concurrent.futures import ThreadPoolExecutor, as_completed
from csv import DictReader

from matplotlib.pyplot import imshow, plot, show, xlabel, ylabel
from eca import OneDimensionalElementaryCellularAutomata

def observables(
    max_time:int, dimension:int, eca_rule:int, 
    ic:Optional[str]=None, display:bool=False
) -> List[float]:
    max_value = 2**dimension
    ca = OneDimensionalElementaryCellularAutomata(lattice_width=dimension,initial_configuration=ic)
    for _ in range(max_time):
        ca.transition(rule_number=eca_rule)
    x,y = zip(*ca.trajectory())
    x_normalised = list(map(
        lambda value:value/max_value,
        x
    ))
    y_normalised = list(map(
        lambda value:value/max_value,
        y
    ))
    if display:
        imshow(ca.evolution(),cmap='gray')
        xlabel('dimension')
        ylabel('time')
        show()
        plot(x_normalised,y_normalised,c='orange')
        xlabel('observable_t')
        ylabel('observable_t+1')
        show()
    return x_normalised


def equivalent_eca_rules() -> Generator[int,None,None]:
    with open('experiments/results/wolfram.csv') as csvfile:
        for row in DictReader(csvfile):
            yield int(row['rule'])

def parallel_map(process: callable, iterable: Iterable) -> Generator[Any, None, None]:
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = []
        for item in iterable:
            results.append(executor.submit(process, item))
        for completed_result in as_completed(results):
            yield completed_result.result()
