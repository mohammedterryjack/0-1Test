# 0-1Test
The 0-1 Test for Chaos

### Example using 1D ECAs
```python
phi_regular = observables(max_time=5000,dimension=300,eca_rule=1,display=True)
phi_edge = observables(max_time=5000,dimension=300,eca_rule=110,display=True)
phi_chaos = observables(max_time=5000,dimension=300,eca_rule=30,display=True)
```
<img src="https://github.com/mohammedterryjack/0-1Test/blob/ea60778ba171a6e989d0cc9b3bd9eea0e603e24b/images/trajectories.png" width=30% height=30%>
<img src="https://github.com/mohammedterryjack/0-1Test/blob/ea60778ba171a6e989d0cc9b3bd9eea0e603e24b/images/observables.png" width=30% height=30%>

```python
O1TestForChaos.test_for_chaos(observables=phi_regular,n_angles=10,display=True)
```

<img src="https://github.com/mohammedterryjack/0-1Test/blob/73b1190cb6cbe57e066155129b201e23c20251bf/images/regular.png" width=40% height=40%>

> -0.007966913897599062

```python
O1TestForChaos.test_for_chaos(observables=phi_edge,n_angles=10,display=True)
```

<img src="https://github.com/mohammedterryjack/0-1Test/blob/ec9fd4e51731063f6fe5372e6d8feb44110512f5/images/edge.png" width=40% height=40%>

> 0.7877953946027167

```python
O1TestForChaos.test_for_chaos(observables=phi_chaos,n_angles=10,display=True)
```

<img src="https://github.com/mohammedterryjack/0-1Test/blob/ec9fd4e51731063f6fe5372e6d8feb44110512f5/images/chaos.png" width=40% height=40%>

> 0.9917596040504413

### Appendix: Loading in 1D-ECA data
```pip install eca```

```python
from typing import List

from matplotlib.pyplot import imshow, plot, show, xlabel, ylabel 
from eca import OneDimensionalElementaryCellularAutomata

def observables(max_time:int, dimension:int, eca_rule:int, display:bool=False) -> List[float]:
    max_value = 2**dimension
    ca = OneDimensionalElementaryCellularAutomata(lattice_width=dimension)
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
        plot(x_normalised,y_normalised)
        xlabel('observable_t')
        ylabel('observable_t+1')
        show()
    return x_normalised
```
