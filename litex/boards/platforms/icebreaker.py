from litex.build.generic_platform import *
from litex.build.lattice import LatticePlatform
from litex.build.lattice.programmer import IceStormProgrammer


_io = [
    ("user_led", 0, Pins("11"), IOStandard("LVCMOS33")),
    ("user_led", 1, Pins("37"), IOStandard("LVCMOS33")),
    ("user_led", 2, Pins("27"), IOStandard("LVCMOS33")),
    ("user_led", 3, Pins("21"), IOStandard("LVCMOS33")),
    ("user_led", 4, Pins("26"), IOStandard("LVCMOS33")),
    ("user_led", 5, Pins("23"), IOStandard("LVCMOS33")),

    ("user_btn", 0, Pins("10"), IOStandard("LVCMOS33")),
    ("user_btn", 1, Pins("19"), IOStandard("LVCMOS33")),
    ("user_btn", 2, Pins(" 9"), IOStandard("LVCMOS33")),
    ("user_btn", 3, Pins("18"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("rx", Pins("6")),
        Subsignal("tx", Pins("9"), Misc("PULLUP")),
        IOStandard("LVCMOS33"),
    ),

    ("spiflash", 0,
        Subsignal("cs_n", Pins("16"), IOStandard("LVCMOS33")),
        Subsignal("clk", Pins("15"), IOStandard("LVCMOS33")),
        Subsignal("mosi", Pins("14"), IOStandard("LVCMOS33")),
        Subsignal("miso", Pins("17"), IOStandard("LVCMOS33"))
    ),

    ("clk12", 0, Pins("35"), IOStandard("LVCMOS33"))
]

_connectors = [
    ("PMOD1A", " 4  2 47 45  3 48 46 44"),
    ("PMOD1B", "43 38 34 31 42 36 32 28"),
]


class Platform(LatticePlatform):
    default_clk_name = "clk12"
    default_clk_period = 83.333

    def __init__(self):
        LatticePlatform.__init__(self, "ice40-up5k-sg48", _io, _connectors,
                                 toolchain="icestorm")

    def create_programmer(self):
        return IceStormProgrammer()
