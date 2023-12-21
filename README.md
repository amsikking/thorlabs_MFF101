# thorlabs_MFF101
Python device adaptor: motorized filter flip mount with Ø1" optic holder.
## Quick start:
- Download the Kinesis (or APT) software GUI from Thorlabs and run/check the flipper...
- To enable the COM port go to Device Manager, find Thorlabs 'APT USB device' (under USB controllers) and on the 'advanced' tab select the **'load VCP'** check box.
- Run the test code at the end of 'thorlabs_MFF101.py' with the correct COM port.
## Details:
- To toggle the flipper with the remote button connect the cable to 'DIG I/O 1' SMA.
- The flipper can also be toggled with the built in surface button (which is easy to accidentally press!).
