import easylatex2image
from easylatex2image import latex_to_image

packages_and_commands = r"""\usepackage[parfill]{parskip}
\usepackage[german]{varioref}
\usepackage{url}
\usepackage{amsmath} 
\usepackage{dcolumn}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows}
\usetikzlibrary{intersections}
\usepackage[all,cmtip]{xy}
"""

content = r"""
$y=x^2$
"""
pillow_image = latex_to_image(packages_and_commands,content,"output.png",dpi=500,img_type="PNG")