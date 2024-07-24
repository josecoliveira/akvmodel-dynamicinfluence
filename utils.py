import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from akvmodel import AKV


def get_influencer_history(
    influence_graph_history: list[list[list[float]]], agent: int
) -> list[list[float]]:
    return [influence_graph[agent] for influence_graph in influence_graph_history]


def get_belief_array_history(
    belief_state_history: list[list[list[float]]],
) -> list[list[float]]:
    return [belief_state[0] for belief_state in belief_state_history]


def is_flow_conservative(influence_graph, num_agents):
    for i in range(num_agents):
        if not np.isclose(np.sum(influence_graph[i, :]), np.sum(influence_graph[:, i])):
            return False
    else:
        return True


def draw_graph(model: AKV) -> None:
    _, ax = plt.subplots(1, 1, figsize=(10, 5))

    step = 0
    ax[step].axis("off")
    DG0 = nx.DiGraph()
    DG0.add_nodes_from(list(range(model.number_of_agents)))
    DG0.add_weighted_edges_from(
        [
            (i, j, round(model.influence_graph_history[step][i][j], 2))
            for i in range(model.number_of_agents)
            for j in range(model.number_of_agents)
            if model.influence_graph_history[step][i][j] != 0 and i != j
        ],
        weight="weight",
    )
    pos = nx.spring_layout(DG0)
    nx.draw_networkx_nodes(DG0, pos, ax=ax[step])
    nx.draw_networkx_labels(DG0, pos, ax=ax[step])
    nx.draw_networkx_edges(DG0, pos, ax=ax[step], connectionstyle="arc3,rad=0.1")
    labels = nx.get_edge_attributes(DG0, "weight")
    nx.draw_networkx_edge_labels(
        DG0, pos, edge_labels=labels, ax=ax[step], connectionstyle="arc3,rad=0.1"
    )

    step = 1
    ax[step].axis("off")
    DG1 = nx.DiGraph()
    DG1.add_nodes_from(list(range(model.number_of_agents)))
    DG1.add_weighted_edges_from(
        [
            (i, j, round(model.influence_graph_history[step][i][j], 2))
            for i in range(model.number_of_agents)
            for j in range(model.number_of_agents)
            if model.influence_graph_history[step][i][j] != 0 and i != j
        ],
        weight="weight",
    )
    # pos = nx.spring_layout(DG1)
    nx.draw_networkx_nodes(DG1, pos, ax=ax[step])
    nx.draw_networkx_labels(DG1, pos, ax=ax[step])
    nx.draw_networkx_edges(DG1, pos, ax=ax[step], connectionstyle="arc3,rad=0.1")
    labels = nx.get_edge_attributes(DG1, "weight")
    nx.draw_networkx_edge_labels(
        DG1, pos, edge_labels=labels, ax=ax[step], connectionstyle="arc3,rad=0.1"
    )

    plt.show()

def draw_graph_2(model):
    _, ax = plt.subplots(1, 1, figsize=(5, 5))

    step = 0
    ax.axis("off")
    DG0 = nx.DiGraph()
    DG0.add_nodes_from(list(range(model.number_of_agents)))
    DG0.add_weighted_edges_from(
        [
            (i, j, round(model.influence_graph_history[step][i][j], 2))
            for i in range(model.number_of_agents)
            for j in range(model.number_of_agents)
            if model.influence_graph_history[step][i][j] != 0 and i != j
        ],
        weight="weight",
    )
    pos = nx.spring_layout(DG0)
    nx.draw_networkx_nodes(DG0, pos, ax=ax)
    nx.draw_networkx_labels(DG0, pos, ax=ax)
    nx.draw_networkx_edges(DG0, pos, ax=ax)
    labels = nx.get_edge_attributes(DG0, "weight")
    # nx.draw_networkx_edge_labels(
    #     DG0, pos, edge_labels=labels, ax=ax
    # )

    plt.savefig("image.png")
    plt.show()