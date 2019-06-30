# This file is Copyright (c) 2019 David Shah <dave@ds0.me>
# License: BSD

from litex.build.generic_platform import *
from litex.build.lattice import LatticePlatform
from litex.build.lattice.programmer import LatticeProgrammer

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("clk100", 0, Pins("B29"), IOStandard("LVDS")),
    ("clk12", 0, Pins("B3"), IOStandard("LVCMOS33")),
    ("clkref", 0, Pins("E17"), IOStandard("LVCMOS33")),

    ("user_btn", 0, Pins("Y32"), IOStandard("SSTL135_I")),
    ("user_btn", 1, Pins("W31"), IOStandard("SSTL135_I")),
    ("user_btn", 2, Pins("AD30"), IOStandard("SSTL135_I")),
    ("user_btn", 3, Pins("AD29"), IOStandard("SSTL135_I")),

    ("user_dip", 0, Pins("AE31"), IOStandard("SSTL135_I")),
    ("user_dip", 1, Pins("AE32"), IOStandard("SSTL135_I")),
    ("user_dip", 2, Pins("AD32"), IOStandard("SSTL135_I")),
    ("user_dip", 3, Pins("AC32"), IOStandard("SSTL135_I")),
    ("user_dip", 4, Pins("AB32"), IOStandard("SSTL135_I")),
    ("user_dip", 5, Pins("AB31"), IOStandard("SSTL135_I")),
    ("user_dip", 6, Pins("AC31"), IOStandard("SSTL135_I")),
    ("user_dip", 7, Pins("AC30"), IOStandard("SSTL135_I")),

    ("user_led",  0, Pins("C26"), IOStandard("LVCMOS33"), Misc("PULLMODE=NONE")),
    ("user_led",  1, Pins("D26"), IOStandard("LVCMOS33"), Misc("PULLMODE=NONE")),
    ("user_led",  2, Pins("A28"), IOStandard("LVCMOS33"), Misc("PULLMODE=NONE")),
    ("user_led",  3, Pins("A29"), IOStandard("LVCMOS33"), Misc("PULLMODE=NONE")),
    ("user_led",  4, Pins("A30"), IOStandard("LVCMOS33"), Misc("PULLMODE=NONE")),
    ("user_led",  5, Pins("AK29"), IOStandard("LVCMOS33"), Misc("PULLMODE=NONE")),
    ("user_led",  6, Pins("AH32"), IOStandard("LVCMOS33"), Misc("PULLMODE=NONE")),
    ("user_led",  7, Pins("AH30"), IOStandard("LVCMOS33"), Misc("PULLMODE=NONE")),
    ("user_led",  8, Pins("AH28"), IOStandard("LVCMOS33"), Misc("PULLMODE=NONE")),
    ("user_led",  9, Pins("AG30"), IOStandard("LVCMOS33"), Misc("PULLMODE=NONE")),
    ("user_led", 10, Pins("AG29"), IOStandard("LVCMOS33"), Misc("PULLMODE=NONE")),
    ("user_led", 11, Pins("AK30"), IOStandard("LVCMOS33"), Misc("PULLMODE=NONE")),

    ("serial", 0,
        Subsignal("rx", Pins("AM28"), IOStandard("LVCMOS33")),
        Subsignal("tx", Pins("AL28"), IOStandard("LVCMOS33")),
    ),

    ("ftdi", 0,
        Subsignal("dq", Pins("AM28 AL28 AM29 AK28 AK32 AM30 AJ32 AL30"), IOStandard("LVCMOS33")),
        Subsignal("txe_n", Pins("AM31"), IOStandard("LVCMOS33")),
        Subsignal("rxf_n", Pins("AJ31"), IOStandard("LVCMOS33")),
        Subsignal("rd_n", Pins("AL32"), IOStandard("LVCMOS33")),
        Subsignal("wr_n", Pins("AG28"), IOStandard("LVCMOS33")),
        Subsignal("siwu_n", Pins("AJ28"), IOStandard("LVCMOS33")),
    ),

    ("ddram", 0,
        Subsignal("a", Pins(
            "E30 F28 C32 E29 F32 D30 E32 D29",
            "D32 C31 H32 F31 F29 B32 D31"),
            IOStandard("SSTL135_I")),
        Subsignal("ba", Pins("H31 H30 J30"), IOStandard("SSTL135_I")),
        Subsignal("ras_n", Pins("K31"), IOStandard("SSTL135_I")),
        Subsignal("cas_n", Pins("K30"), IOStandard("SSTL135_I")),
        Subsignal("we_n", Pins("J32"), IOStandard("SSTL135_I")),
        Subsignal("cs_n", Pins("K29"), IOStandard("SSTL135_I")),
        Subsignal("dm", Pins("R26 L27 Y27 U31"), IOStandard("SSTL135_I")),
        Subsignal("dq", Pins(
            " V26  R27  V27  T26  U28  T27  T29  U26",
            " P27  K28  P26  L26  K27  N26  L29  K26",
            "AC27  W28 AC26  Y26 AB26  W29 AD26  Y28",
            " T32  U32  P31  V32  P32  W32  N32  U30"),
            IOStandard("SSTL135_I"),
            Misc("TERMINATION=75")),
        Subsignal("dqs_p", Pins("R29 N30 AB28 R32"), IOStandard("SSTL135D_I"), Misc("TERMINATION=OFF"), Misc("DIFFRESISTOR=100")),
        Subsignal("clk_p", Pins("L31"), IOStandard("SSTL135D_I")),
        Subsignal("cke", Pins("K32"), IOStandard("SSTL135_I")),
        Subsignal("odt", Pins("J29"), IOStandard("SSTL135_I")),
        Subsignal("reset_n", Pins("L32"), IOStandard("SSTL135_I")),
        Misc("SLEWRATE=FAST"),
    ),

     ("dram_vtt_en", 0, Pins("E25"), IOStandard("LVCMOS33")),


    ("eth_clocks", 0,
        Subsignal("tx", Pins("A15")),
        Subsignal("rx", Pins("C17")),
        Subsignal("ref", Pins("A17")),
        IOStandard("LVCMOS33")
    ),

    ("eth", 0,
        Subsignal("rst_n", Pins("D16")),
        Subsignal("int_n", Pins("E16")),
        Subsignal("mdio", Pins("F17")),
        Subsignal("mdc", Pins("B17")),
        Subsignal("rx_ctl", Pins("A16")),
        Subsignal("rx_data", Pins("C16 B16 B14 F16")),
        Subsignal("tx_ctl", Pins("D15")),
        Subsignal("tx_data", Pins("A14 F15 C15 C14")),
        IOStandard("LVCMOS33")
    ),

    ("clkgen", 0,
        Subsignal("sda", Pins("C22")),
        Subsignal("scl", Pins("A22")),
        Subsignal("sd_oe", Pins("A2")),
        IOStandard("LVCMOS33")
    ),


    ("pcie_x2", 0,
        Subsignal("clk_p", Pins("AM14")),
        Subsignal("clk_n", Pins("AM15")),
        Subsignal("rx_p", Pins("AM8 AK12")),
        Subsignal("rx_n", Pins("AM9 AK13")),
        Subsignal("tx_p", Pins("AK9 AM11")),
        Subsignal("tx_n", Pins("AK10 AM12")),
        Subsignal("perst", Pins("D22"), IOStandard("LVCMOS33")),
        Subsignal("wake_n", Pins("A23"), IOStandard("LVCMOS33")),
    ),

    ("m2", 0,
        Subsignal("clk_p", Pins("AM23")),
        Subsignal("clk_n", Pins("AM24")),
        Subsignal("rx_p", Pins("AM17 AK21")),
        Subsignal("rx_n", Pins("AM18 AK22")),
        Subsignal("tx_p", Pins("AK18 AM20")),
        Subsignal("tx_n", Pins("AK19 AM21")),

        Subsignal("clksel", Pins("N3"), IOStandard("LVCMOS33")),

        Subsignal("sdio_clk", Pins("L4"), IOStandard("LVCMOS33")),
        Subsignal("sdio_cmd", Pins("K4"), IOStandard("LVCMOS33")),
        Subsignal("sdio_dq", Pins("L7 N4 L6 N6"), IOStandard("LVCMOS33")),

        Subsignal("uart_tx", Pins("P6"), IOStandard("LVCMOS33")),
        Subsignal("uart_rx", Pins("K5"), IOStandard("LVCMOS33")),
        Subsignal("uart_rts_n", Pins("N7"), IOStandard("LVCMOS33")),
        Subsignal("uart_cts_n", Pins("P7"), IOStandard("LVCMOS33"))
    ),

    ("sdcard", 0,
        Subsignal("data", Pins("AG1 AJ1 AH1 AK1")),
        Subsignal("clk", Pins("AK3")),
        Subsignal("cmd", Pins("AH3")),
        IOStandard("LVCMOS33")
    ),

    ("spiflash4x", 0,
        Subsignal("clk", Pins("AM3")),
        Subsignal("cs_n", Pins("AJ3")),
        Subsignal("dq", Pins("AK2 AJ2 AM2 AL1")),
        IOStandard("LVCMOS33")
    ),

    ("spiflash", 0,
        Subsignal("clk", Pins("AM3")),
        Subsignal("cs_n", Pins("AJ3")),
        Subsignal("mosi", Pins("AK2")),
        Subsignal("miso", Pins("AJ2")),
        Subsignal("wp", Pins("AM2")),
        Subsignal("hold", Pins("AL1")),
        IOStandard("LVCMOS33")
    ),

    ("ulpi", 0,
        Subsignal("clk", Pins("A18")),
        Subsignal("stp", Pins("D18")),
        Subsignal("dir", Pins("C18")),
        Subsignal("nxt", Pins("F18")),
        Subsignal("reset", Pins("D17")),
        Subsignal("data", Pins("C20 C19 E19 D20 A20 B19 D19 A19")),
        IOStandard("LVCMOS33")
    ),

    ("hdmi", 0,
        Subsignal("d", Pins(
            "C11 A11 B11 A10 B10 C10 A8 B7",
            "B8 A7 C8 C9 F11 E11 E10 D10",
            "F10 F9 D9 D8 C7 F8 E8 D11")),
        Subsignal("de", Pins("F14")),
        Subsignal("clk", Pins("A9")),
        Subsignal("vsync", Pins("E14")),
        Subsignal("hsync", Pins("F13")),
        Subsignal("sda", Pins("D13")),
        Subsignal("scl", Pins("C13")),
        IOStandard("LVCMOS33")
    ),
]

_connectors = [
    ("pmoda", "F19 F20 B22 C23 D14 A13 E22 D23"),
    ("pmodb", "C25 A26 F23 F25 B25 D25 F22 F24"),
    ("pmodx", "A24 C24 D24 B23 D23 A25"),

    ("ext0", "T1 U1 AE5 AE4 AB5 AB6 Y5 W5 W2 Y1 AB7 AC6 AB3 AB4 AD3 AE3 AB1 AC1 AD1 AE1 AD6 AE6 AC7 AD7"),
    ("ext1", "P5 P4 R7 T7 R6 T6 U6 U7 R4 T5 T4 U5 U4 V4 V6 V7 P2 P3 R3 T3 N1 P1 U2 U3"),
    ("ext2", "K6 K7 J7 J6 H6 H5 F4 F5 F3 E3 C4 C3 C5 D5 D3 D2 H2 H3 J3 K3 B1 C2 F1 H1")

]

# Platform -----------------------------------------------------------------------------------------

class Platform(LatticePlatform):
    default_clk_name = "clk100"
    default_clk_period = 10

    def __init__(self, **kwargs):
        LatticePlatform.__init__(self, "LFE5UM5G-85F-8BG756C", _io, _connectors, **kwargs)

    def do_finalize(self, fragment):
        try:
            self.add_period_constraint(self.lookup_request("eth_clocks", 0).rx, 1e9/125e6)
        except ConstraintError:
            pass

    def create_programmer(self, with_ispclock=True):
        _xcf_ispclock = """
        <Device>
            <SelectedProg value="FALSE"/>
            <Pos>2</Pos>
            <Vendor>Lattice</Vendor>
            <Family>ispCLOCK</Family>
            <Name>ispPAC-CLK5406D</Name>
            <IDCode>0x00191043</IDCode>
            <Operation>Erase,Program,Verify</Operation>
            <Bypass>
                <InstrLen>8</InstrLen>
                <InstrVal>11111111</InstrVal>
                <BScanLen>1</BScanLen>
                <BScanVal>0</BScanVal>
            </Bypass>
        </Device>
"""

        _xcf_template = """
<?xml version='1.0' encoding='utf-8' ?>
<!DOCTYPE        ispXCF    SYSTEM    "IspXCF.dtd" >
<ispXCF version="3.4.1">
    <Comment></Comment>
    <Chain>
        <Comm>JTAG</Comm>
        <Device>
            <SelectedProg value="TRUE"/>
            <Pos>1</Pos>
            <Vendor>Lattice</Vendor>
            <Family>ECP5UM5G</Family>
            <Name>LFE5UM5G-45F</Name>
            <IDCode>0x81112043</IDCode>
            <File>{{bitstream_file}}</File>
            <Operation>Fast Program</Operation>
        </Device>{ispclock}
    </Chain>
    <ProjectOptions>
        <Program>SEQUENTIAL</Program>
        <Process>ENTIRED CHAIN</Process>
        <OperationOverride>No Override</OperationOverride>
        <StartTAP>TLR</StartTAP>
        <EndTAP>TLR</EndTAP>
        <VerifyUsercode value="FALSE"/>
    </ProjectOptions>
    <CableOptions>
        <CableName>USB2</CableName>
        <PortAdd>FTUSB-0</PortAdd>
        <USBID>LATTICE ECP5_5G VERSA BOARD A Location 0000 Serial Lattice ECP5_5G VERSA Board A</USBID>
    </CableOptions>
</ispXCF>
""".format(ispclock=_xcf_ispclock if with_ispclock else "")

        return LatticeProgrammer(_xcf_template)
