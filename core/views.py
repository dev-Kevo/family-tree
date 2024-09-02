from django.shortcuts import render
from .models import Node

def build_tree(node):
    return {
        'node' : node,
        'children' : [build_tree(child) for child in node.get_children()]
    }

def roadmap_view(request):
    root_nodes = Node.objects.filter(parent_node__isnull=True)
    tree = [build_tree(node) for node in root_nodes]
    # print(tree)

    context = {
        'tree' : tree
    }

    return render(request, 'core/roadmap.html', context)
