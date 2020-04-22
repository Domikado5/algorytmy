from browser import document, console, alert, window, html
import avl
import bst

tree = None
def create_nav():
    n = html.NAV(id='nav')
    n <= html.INPUT(id='insert')
    n <= html.BUTTON("Insert", id='insert-btn')
    n <= html.INPUT(id='delete')
    n <= html.BUTTON('Delete', id='delete-btn')
    return n

def get_type(e):
    global tree
    if e.target.value == 'avl':
        tree = avl.Tree()
        del document['nav']
        n = create_nav()
        document['container'] <= n
        document['container'] <= html.DIV(id = 'tree')
        document['insert-btn'].bind('click', insert_event)
        document['delete-btn'].bind('click', delete_event)
    elif e.target.value == 'bst':
        tree = bst.Tree()
        del document['nav']
        n = create_nav()
        n <= html.BUTTON('DSW', id='dsw-btn')
        document['container'] <= n
        document['container'] <= html.DIV(id = 'tree')
        document['insert-btn'].bind('click', insert_event)
        document['delete-btn'].bind('click', delete_event)
        document['dsw-btn'].bind('click', dsw_event)
    else:
        alert("Something went wrong. Please refresh this page.")

def build_tree(e):
    if e is None:
        tmp = html.DIV(html.P(""), Class='leaf')
    else:
        tmp = html.DIV(html.P(e.value), Class='leaf')
        tmp <= build_tree(e.left)
        tmp <= build_tree(e.right)
    return tmp

def update_tree(e):
    document['tree'].clear()
    document['tree'] <= build_tree(e)
    
def insert_event(e):
    global tree
    value = document['insert'].value
    value = int(value)
    tree.insert(avl.Leaf(value), tree.root)
    result = tree.toDICT(tree.root)
    console.log(result)
    update_tree(tree.root)

def delete_event(e):
    global tree
    value = document['delete'].value
    value = int(value)
    tree.delete(value, tree.root)
    result = tree.toDICT(tree.root)
    console.log(result)
    update_tree(tree.root)

def dsw_event(e):
    global tree
    tree.dsw(tree.root)
    result = tree.toDICT(tree.root)
    console.log(result)
    update_tree(tree.root)

document['avl'].bind('click', get_type)
document['bst'].bind('click', get_type)