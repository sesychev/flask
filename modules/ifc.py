import ifcopenshell
import ifcopenshell.util
import ifcopenshell.geom
import ifcopenshell.util.element

# from ifc_viewer import ifc_viewer


# print(wall.is_a())
# print(wall.get_info())
# https://wiki.osarch.org/index.php?title=IfcOpenShell_code_examples
# https://linjiarui.net/en/posts/2020-06-15-opensource-bim-tools
# https://trimsh.org/examples.html#quick-start-ipynb
# https://github.com/ifcjs/
# https://github.com/stefkeB/ifcopenshell_examples/tree/main/3D
# https://github.com/stefkeB/ifcopenshell_examples/blob/main/3D/qt3d_minimal.py
# https://github.com/R-Rijnbeek/IFC_WebViewer/tree/master
# https://github.com/AECgeeks/ifc-pipeline/tree/master
# https://blog.skillfactory.ru/kak-napisat-veb-prilozhenie-dlya-demonstratsii-data-science-proekta-na-python/


ifc = ifcopenshell.open('static/ifc/____P0-02-070.ifc')

wall = ifc.by_type('IfcBeam')[0]
print(wall)
