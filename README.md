# coauthors_search
An package for finding coauthors from different sources for  example Google Scholar.

fetch_author_by_name(name: str) - method in Fetch class returns list of Author objects.

create_tree(root: Author, goal: Author) - method in Tree class builds dict with pathes from root to coauthors and
when it finds goal it returns this dict.

generate_graph(tree: Tree, target: Author, configuration: Dict[str, Any]) - create picture that represents graph.
This graph is a path from root to goal with some of their additional coauthors.
configuration:
    graph_type - describes that graph will be directed or not.
    format - describes image file format PNG, JPG, PDF, etc.
    additional_nodes - describes how many additional coauthors will be displayed.
    addition_branch_color - describes the colors of links between main branch node and additional coauthor node.
    main_branch_color - describes the color of links between main branch nodes.


You need to download graphviz exe from: https://www.graphviz.org/download/