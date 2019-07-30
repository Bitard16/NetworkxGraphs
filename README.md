# NetworkxGraphs
Graphs and algorithms

The first distinction is that Dijkstra’s algorithm solves a different problem than Kruskal and Prim. Dijkstra solves the shortest path problem (from a specified node), while Kruskal and Prim finds a minimum-cost spanning tree. The following is a modified form of a description I wrote at this page: Graph algorithms.

    For any graph, a spanning tree is a collection of edges sufficient to provide exactly one path between every pair of vertices. This restriction means that there can be no circuits formed by the chosen edges.
        A minimum-cost spanning tree is one which has the smallest possible total weight (where weight represents cost or distance). There might be more than one such tree, but Prim and Kruskal are both guaranteed to find one of them.
        For a specified vertex (say X), a shortest path tree is a spanning tree such that the path from X to any other vertex is as short as possible (i.e., has the minimum possible weight).

Prim and Dijkstra "grow" the tree out from a starting vertex. In other words, they have a "local" focus; at each step, we only consider those edges adjacent to previously chosen vertices, choosing the cheapest option which satisfies our needs. Meanwhile, Kruskal is a "global" algorithm, meaning that each edge is (greedily) chosen from the entire graph. (Actually, Dijkstra might be viewed as having some global aspect, as noted below.)

To find a minimum-cost spanning tree:

    Kruskal (global approach): At each step, choose the cheapest available edge anywhere which does not violate the goal of creating a spanning tree.
    Prim (local approach): Choose a starting vertex. At each successive step, choose the cheapest available edge attached to any previously chosen vertex which does not violate the goal of creating a spanning tree.

To find a shortest-path spanning tree:

    Dijkstra: At each step, choose the edge attached to any previously chosen vertex (the local aspect) which makes the total distance from the starting vertex (the global aspect) as small as possible, and does not violate the goal of creating a spanning tree.
