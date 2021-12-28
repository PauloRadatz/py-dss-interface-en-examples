import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"compile [{dss_file}]")

dss.lines_write_name("650632")
bus1 = dss.lines_read_bus1()
dss.lines_write_length(1000)
new_length = dss.lines_read_length()

print(f"Line {dss.lines_read_name()} connected between buses ({bus1}, {dss.lines_read_bus2()}) has a new length of {new_length}")