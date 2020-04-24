from browser import document, console, alert, window, html
import avl
import bst

tree = None
treeType = None
def create_nav():
    n = html.NAV(id='nav')
    n <= html.INPUT(id='insert')
    n <= html.BUTTON("Insert", id='insert-btn', Class='btn')
    n <= html.INPUT(id='delete')
    n <= html.BUTTON('Delete', id='delete-btn', Class='btn')
    n <= html.BUTTON('Min', id='min-btn', Class='btn')
    n <= html.BUTTON('Max', id='max-btn', Class='btn')
    n <= html.BUTTON('Inorder', id='inorder-btn', Class='btn')
    n <= html.BUTTON('Preorder', id='preorder-btn', Class='btn')
    n <= html.BUTTON('Postorder', id='postorder-btn', Class='btn')
    return n

def get_type(e):
    global tree
    global treeType
    if e.target.value == 'avl':
        tree = avl.Tree()
        del document['nav']
        n = create_nav()
        document['container'] <= n
        document['container'] <= html.DIV(id='output')
        document['container'] <= html.DIV(id = 'tree')
        document['h1'].text = 'AVL tree'
        treeType = 'AVL'
    elif e.target.value == 'bst':
        tree = bst.Tree()
        del document['nav']
        n = create_nav()
        n <= html.BUTTON('DSW', id='dsw-btn', Class='btn')
        document['container'] <= n
        document['container'] <= html.DIV(id='output')
        document['container'] <= html.DIV(id = 'tree')
        document['dsw-btn'].bind('click', dsw_event)
        document['h1'].text = 'BST tree'
        treeType = 'BST'
    else:
        alert("Something went wrong. Please refresh this page.")
    document['insert-btn'].bind('click', insert_event)
    document['delete-btn'].bind('click', delete_event)
    document['min-btn'].bind('click', min_event)
    document['max-btn'].bind('click', max_event)
    document['inorder-btn'].bind('click', inorder_event)
    document['preorder-btn'].bind('click', preorder_event)
    document['postorder-btn'].bind('click', postorder_event)

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

def min_event(e):
    global tree
    r, m = tree.minVis(tree.root)
    console.log(r,m)
    document['output'].text = ""
    document['output'] <= html.DIV(m, id="value")
    document['output'] <= html.DIV(r, id="path")
    
def max_event(e):
    global tree
    r, m = tree.maxVis(tree.root)
    console.log(r,m)
    document['output'].text = ""
    document['output'] <= html.DIV(m, id="value")
    document['output'] <= html.DIV(r, id="path")

def inorder_event(e):
    global tree
    tmp = tree.inorderVis(tree.root)
    tmp = ", ".join(tmp)
    document['output'].text = ""
    document['output'] <= html.DIV(tmp, id="order")

def preorder_event(e):
    global tree
    tmp = tree.preorderVis(tree.root)
    tmp = ", ".join(tmp)
    document['output'].text = ""
    document['output'] <= html.DIV(tmp, id="order")

def postorder_event(e):
    global tree
    tmp = tree.postorderVis(tree.root)
    tmp = ", ".join(tmp)
    document['output'].text = ""
    document['output'] <= html.DIV(tmp, id="order")

def insert_event(e):
    global tree
    value = document['insert'].value
    value = int(value)
    if treeType == 'AVL':
        tree.insert(avl.Leaf(value), tree.root)
    elif treeType == 'BST':
        tree.insert(bst.Leaf(value), tree.root)
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
    if treeType == 'AVL':
        alert("You cannot run DSW for AVL tree.")
        return
    tree.dsw(tree.root)
    result = tree.toDICT(tree.root)
    console.log(result)
    update_tree(tree.root)

document['avl'].bind('click', get_type)
document['bst'].bind('click', get_type)