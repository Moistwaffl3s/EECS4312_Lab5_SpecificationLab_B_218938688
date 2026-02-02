## Student Name: Ajit sanghera
## Student ID: 218938688

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Args:
        resources : Dict[str, Number], Mapping from resource name to total available capacity.
        requests : List[Dict[str, Number]], List of requests. Each request is a mapping from resource name to the amount required.

    Returns:
        True if the allocation is feasible, False otherwise.

    """

    if not isinstance(resources, dict):
        raise ValueError("must be a distionary")

    if not isinstance(requests, list):
        raise ValueError("must be a list")

    for req in requests:

        if not isinstance(req, dict):
            raise ValueError("must be a dictionary")

        for resource, amount in req.items():

            if resource not in resources:
                return False

            if amount < 0:
                raise ValueError(f" the allocation cannot be less than 0")

            if not isinstance(resource, str):
                raise ValueError("resource must be a string")

            if not isinstance(amount, int):
                raise ValueError("resource must be a integer")

            if amount > resources.get(resource)
                return False 
    return True

    # TODO: Implement this function
    raise NotImplementedError("suggest_slots function has not been implemented yet")