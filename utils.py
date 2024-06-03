def get_influencer_history(
    influence_graph_history: list[list[list[float]]], agent: int
) -> list[list[float]]:
    return [influence_graph[agent] for influence_graph in influence_graph_history]

def get_belief_array_history(
    belief_state_history: list[list[list[float]]]
) -> list[list[float]]:
    return [belief_state[0] for belief_state in belief_state_history]