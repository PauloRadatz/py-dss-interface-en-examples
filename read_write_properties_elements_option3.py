import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"compile [{dss_file}]")

dss.circuit_set_active_element("Line.650632")

switch = dss.dssproperties_read_value(str(dss.cktelement_all_property_names().index("Switch") + 1))

print(f"Is {dss.cktelement_name()} a switch? {switch}")