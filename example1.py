import py_dss_interface

dss = py_dss_interface.DSSDLL(r"C:\Program Files\OpenDSS")

dss_file = r"C:\OpenDSS_Basics\13Bus\IEEE13Nodeckt.dss"

dss.text(f"compile [{dss_file}]")

dss.text("Solve")

dss.text("Show voltages LN node")
