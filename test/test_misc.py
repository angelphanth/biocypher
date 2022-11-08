import biocypher._misc as _misc

example_tree = {
    'B': 'A',
    'C': 'A',
    'D': 'B',
    'E': 'B',
    'F': 'C',
    'G': 'C',
    'H': 'E',
    'I': 'G',
}


def test_tree_vis():

    tree_vis = _misc.tree_figure(example_tree)

    assert tree_vis.DEPTH == 1
    assert tree_vis.WIDTH == 2
    assert tree_vis.root == 'A'


if __name__ == '__main__':
    # to look at it
    print(_misc.tree_figure(example_tree).show())
