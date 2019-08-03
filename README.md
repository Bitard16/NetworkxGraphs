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



PageRank is an algorithm that measures the transitive influence or connectivity of nodes.

It can be computed by either iteratively distributing one node’s rank (originally based on degree) over its neighbours or by randomly traversing the graph and counting the frequency of hitting each node during these walks. 

PageRank can be applied across a wide range of domains. The following are some notable use-cases:

    Personalized PageRank is used by Twitter to present users with recommendations of other accounts that they may wish to follow. The algorithm is run over a graph which contains shared interests and common connections. Their approach is described in more detail in "WTF: The Who to Follow Service at Twitter".
    PageRank has been used to rank public spaces or streets, predicting traffic flow and human movement in these areas. The algorithm is run over a graph which contains intersections connected by roads, where the PageRank score reflects the tendency of people to park, or end their journey, on each street. This is described in more detail in "Self-organized Natural Roads for Predicting Traffic Flow: A Sensitivity Study".
    PageRank can be used as part of an anomaly or fraud detection system in the healthcare and insurance industries. It can help find doctors or providers that are behaving in an unusual manner, and then feed the score into a machine learning algorithm.

There are many more use cases, which you can read about in David Gleich’s "PageRank beyond the web"
When not to use the PageRank algorithm

There are some things to be aware of when using the PageRank algorithm:

    If there are no links from within a group of pages to outside of the group, then the group is considered a spider trap.
    Rank sink can occur when a network of pages form an infinite cycle.
    Dead-ends occur when pages have no out-links. If a page contains a link to another page which has no out-links, the link would be known as a dangling link.

If you see unexpected results from running the algorithm, it is worth doing some exploratory analysis of the graph to see if any of these problems are the cause. You can read The Google PageRank Algorithm and How It Works to learn more.
