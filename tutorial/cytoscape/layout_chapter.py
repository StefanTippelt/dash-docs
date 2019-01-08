import math
from textwrap import dedent

import dash_cytoscape
import dash_core_components as dcc
import dash_html_components as html

from .utils import CreateDisplay


nodes = [
    {
        'data': {'id': short, 'label': label},
        'position': {'x': 20*lat, 'y': -20*long}
    }
    for short, label, long, lat in (
        ('la', 'Los Angeles', 34.03, -118.25),
        ('nyc', 'New York', 40.71, -74),
        ('to', 'Toronto', 43.65, -79.38),
        ('mtl', 'Montreal', 45.50, -73.57),
        ('van', 'Vancouver', 49.28, -123.12),
        ('chi', 'Chicago', 41.88, -87.63),
        ('bos', 'Boston', 42.36, -71.06),
        ('hou', 'Houston', 29.76, -95.37)
    )
]

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in (
        ('van', 'la'),
        ('la', 'chi'),
        ('hou', 'chi'),
        ('to', 'mtl'),
        ('mtl', 'bos'),
        ('nyc', 'boston'),
        ('to', 'hou'),
        ('to', 'nyc'),
        ('la', 'nyc'),
        ('nyc', 'bos')
    )
]

elements = nodes + edges


Display = CreateDisplay({
    'dash_cytoscape': dash_cytoscape,
    'elements': elements,
    'math': math
})


layout = html.Div([

    dcc.Markdown(dedent('''
    # Layouts
    
    ## Layout Declaration
    
    The layout parameter of `dash_cytoscape.Cytoscape` takes as argument a
    dictionary specifying how the nodes should be positioned on the screen.
    Every graph requires this dictionary with a value specified for the 
    `name` key. It represents a built-in display method, which is one of the 
    following:
    - `preset`
    - `random`
    - `grid`
    - `circle`
    - `concentric`
    - `breadthfirst`
    - `cose`
    
    All these layouts (along with their options), are [described in the
    documentation](http://js.cytoscape.org/#layouts).
    
    If the value of `name` is set to `'preset'`, the positions will be rendered based on the positions
    specified in the elements. Otherwise, the positions will be computed by 
    Cytoscape.js behind the scenes, based on the given layout
    dictionary. Let's start with an example of declaring a graph with a preset
    layout:
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        elements=elements,
        style={'width': '100%', 'height': '350px'},
        layout={
            'name': 'preset'
        }
    )
    '''),

    dcc.Markdown(dedent('''
    > Here, we provided toy elements using geographically positioned nodes. If
    > you'd like to reproduce this example by yourself, check out the code 
    > below.
    
    ''')),

    html.Details(open=False, children=[
        html.Summary('View Elements Declaration'),
        dcc.SyntaxHighlighter(dedent('''
        nodes = [
            {
                'data': {'id': short, 'label': label}, 
                'position': {'x': 20*lat, 'y': -20*long}
            }
            for short, label, long, lat in (
                ('la', 'Los Angeles', 34.03, -118.25),
                ('nyc', 'New York', 40.71, -74),
                ('to', 'Toronto', 43.65, -79.38),
                ('mtl', 'Montreal', 45.50, -73.57),
                ('van', 'Vancouver', 49.28, -123.12),
                ('chi', 'Chicago', 41.88, -87.63),
                ('bos', 'Boston', 42.36, -71.06),
                ('hou', 'Houston', 29.76, -95.37)
            )
        ]
        
        edges = [
            {'data': {'source': source, 'target': target}}
            for source, target in (
                ('van', 'la'),
                ('la', 'chi'),
                ('hou', 'chi'),
                ('to', 'mtl'),
                ('mtl', 'bos'),
                ('nyc', 'boston'),
                ('to', 'hou'),
                ('to', 'nyc'),
                ('la', 'nyc'),
                ('nyc', 'bos')
            )
        ]
        
        elements = nodes + edges
        '''))
    ]),

    dcc.Markdown(dedent('''
    ## Display Methods
    
    In most cases, the positions of the nodes will not be given. In these
    cases, one of the built-in methods can be used. Let's see what happens 
    when the value of `name` is set to `'circle'` or `'grid'`
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        elements=elements,
        style={'width': '100%', 'height': '350px'},
        layout={
            'name': 'circle'
        }
    )
    '''),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        elements=elements,
        style={'width': '100%', 'height': '350px'},
        layout={
            'name': 'grid'
        }
    )
    '''),

    dcc.Markdown(dedent('''
    
    ## Finetuning the Layouts
    
    For any given `name` item, a collection of keys are accepted by the layout 
    dictionary. For example, the `grid` layout will accept `row` and
    `cols`, the `circle` layout accepts `radius` and `startAngle`, and so 
    forth. Here's the grid layout with the same graph as above, but
    with different layout options:
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        elements=elements,
        style={'width': '100%', 'height': '350px'},
        layout={
            'name': 'grid',
            'rows': 3
        }
    )
    '''),

    dcc.Markdown(dedent('''
    Similarly for the circle layout, we can force the nodes to start and end at
    a certain angle in radians (import `math` for this example):
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        elements=elements,
        style={'width': '100%', 'height': '350px'},
        layout={
            'name': 'circle',
            'radius': 250,
            'startAngle': math.pi * 1/6,
            'sweep': math.pi * 2/3
        }
    )
    '''),

    dcc.Markdown(dedent('''
    For the `breadthfirst` layout, a tree is created from the existing nodes
    by performing a breadth-first search of the graph. By default, the root(s)
    of the tree is inferred, but can also be specified as an option. Here is
    how the graph looks like if we choose New York City as the root:
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        elements=elements,
        style={'width': '100%', 'height': '350px'},
        layout={
            'name': 'breadthfirst',
            'roots': '[id = "nyc"]'
        }
    )
    '''),

    dcc.Markdown(dedent('''
    Here is what would happen if we choose Montreal and Vancouver instead:
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        elements=elements,
        style={'width': '100%', 'height': '350px'},
        layout={
            'name': 'breadthfirst',
            'roots': '#van, #mtl'
        }
    )
    '''),

    dcc.Markdown(dedent('''
    > Notice here that we are not giving the ID of the nodes to the `roots`
    > key, but instead use a specific syntax to select the desired elements. 
    > This concept of selector will be further explored in part 3, and is 
    > [extensively documented in Cytoscape.js](http://js.cytoscape.org/#selectors).
    > We follow the same syntax as the Javascript library.
    
    ## Physics-based Layouts
    
    Additionally, the `cose` layout can be used to position the nodes using
    a force-directed layout by simulating attraction and repulsion among the
    elements, based on the paper by 
    [Dogrusoz et al, 2009](https://dl.acm.org/citation.cfm?id=1498047).
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        elements=elements,
        style={'width': '100%', 'height': '350px'},
        layout={
            'name': 'cose'
        }
    )
    ''')
])
