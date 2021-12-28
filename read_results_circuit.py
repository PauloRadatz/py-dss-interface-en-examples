import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"compile [{dss_file}]")
dss.text("solve")

print(f"Total powers are: {-dss.circuit_total_power()[0]} kW and {-dss.circuit_total_power()[1]} kvar")