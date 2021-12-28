import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"compile [{dss_file}]")

line_name = "650632"
property_name = "switch"

switch = dss.text(f"? line.{line_name}.{property_name}")
print(f"Is line {line_name} a switch? {switch}")

dss.text(f"edit line.650632 switch=True")
switch = dss.text(f"? line.{line_name}.{property_name}")
print(f"Is line {line_name} a switch? {switch}")