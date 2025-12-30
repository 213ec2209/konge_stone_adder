import os
import random
from pathlib import Path
import cocotb
from cocotb import start_soon
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, NextTimeStep, ReadOnly, RisingEdge, Timer
from cocotb_tools.runner import get_runner

@cocotb.test()
async def example_test(dut):
    pass
def test_konge_stone_adder_runner():
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent.parent
    sources = [proj_path / "sources/konge_stone_adder.v"]
    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="konge_stone_adder",
        always=True,
    )
    runner.test(hdl_toplevel="konge_stone_adder", test_module="test_konge_stone_adder")
