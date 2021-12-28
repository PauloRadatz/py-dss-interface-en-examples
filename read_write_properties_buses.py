import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"compile [{dss_file}]")

dss.circuit_set_active_bus("671")

bus_kv = dss.bus_kv_base()

print(f"Bus {dss.bus_name()} has a voltage base of {bus_kv} kV")

new_x_coord = dss.bus_write_x(10)
new_y_coord = dss.bus_write_y(10)