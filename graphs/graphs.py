from functools import singledispatch


class TreeNode:
    """"
    A basic tree implementation.

    Observe that a tree is simply a collection of connected TreeNodes.

    Parameters
    ----------
    value:
        An arbitrary value associated with this node.
    children:
        The TreeNodes which are the children of this node.
    """
    def __init__(self, value, *children):
        self.value = value
        self.children = children

    def __repr__(self):
        """Return the canonical string representation."""
        return f"{type(self).__name__}{(self.value,)+self.children}"

    def __str__(self):
        """Serialise the tree recursively as parent -> (children)."""
        childstring = ", ".join(map(str, self.children))
        return f"{self.value!s} -> ({childstring})"


def postvisitor(tree, fn):
    """
    Traverse tree in post-order applying a function to every node.

    Parameters
    ----------
    tree: TreeNode
        The tree to be visited.
    fn: function(node, *fn_children)
        A function to be applied at each node. The function should take
        the node to be visited as its first argument, and the results
        of vising its children as any further arguments.
    """
    return fn(tree, *(postvisitor(c, fn) for c in tree.children))


def previsitor(tree, fn, fn_parent=None):
    """
    Traverse tree in pre-order applying a function to every node.

    Parameters
    ----------
    tree: TreeNode
        The tree to be visited.
    fn: function(node, fn_parent)
        A function to be applied at each node. The function should take
        the node to be visited as its first argument, and the result of
        visiting its parents as the second.
    """
    fn_out = fn(tree, fn_parent)

    for child in tree.children:
        previsitor(child, fn, fn_out)


@singledispatch
def evaluate(expr, *o, **kwargs):
    """
    Evaluate an expression node.

    Parameters
    ----------
    expr: Expression
        The expression node to be evaluated
    *o: numbers.Number
        The results of evaluating the operands of expr
    **kwargs:
        Any keyword arguments required to evaluate specific types of
        expression.
    symbol_map: dict
        A dictionary mapping Symbol names to numerical values, for
        example:
        {'x': 1}
    """
    raise NotImplementedError(
        f"Cannot evaluate a{type(expr).__name__}")

# Complete expressions package


def postvisitor_expanded(expr, fn, **kwargs):
    '''
    Visit an Expression in post-order applying a function every node

    Parameters
    ----------
    expr: Expression
        The expression to be visited.
    fn: function(node, *0, **kwargs)
        A function to be applied at each node. The function should take
        the node to be visited as its first argument, and the result of
        visiting its operands as any further positional arguments. Any
        additional information that the visitor requires can be passed
        as keyword arguments.
    **kwargs:
        Any additional keyword arguments to be passed to fn.
    '''
    return fn(expr,
              *(postvisitor_expanded(c, fn, **kwargs) for c in expr.operands),
              **kwargs)
