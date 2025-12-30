import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_addition_1(dut):
    """Test Kogge–Stone Adder: 15 + 1 = 16"""
    print("Kogge–Stone Adder Test 1")

    dut.A.value = 0x000F   # 15
    dut.B.value = 0x0001   # 1
    dut.Carry_in.value = 0

    await Timer(5, unit="ns")

    dut._log.info(
        "A = %d, B = %d, Carry_in = %d, Sum = %d",
        dut.A.value, dut.B.value, dut.Carry_in.value, dut.Sum.value
    )

    assert dut.Sum.value == 16, "Addition result is incorrect"


@cocotb.test()
async def test_addition_2(dut):
    """Test Kogge–Stone Adder: 255 + 1 = 256"""
    print("Kogge–Stone Adder Test 2")

    dut.A.value = 0x00FF   # 255
    dut.B.value = 0x0001   # 1
    dut.Carry_in.value = 0

    await Timer(5, unit="ns")

    dut._log.info(
        "A = %d, B = %d, Carry_in = %d, Sum = %d",
        dut.A.value, dut.B.value, dut.Carry_in.value, dut.Sum.value
    )

    assert dut.Sum.value == 256, "Addition result is incorrect"


@cocotb.test()
async def test_addition_with_carry(dut):
    """Test Kogge–Stone Adder with carry-in: 65535 + 1 + 1"""
    print("Kogge–Stone Adder Carry-in Test")

    dut.A.value = 0xFFFF   # 65535
    dut.B.value = 0x0001   # 1
    dut.Carry_in.value = 1

    await Timer(5, unit="ns")

    dut._log.info(
        "A = %d, B = %d, Carry_in = %d, Sum = %d",
        dut.A.value, dut.B.value, dut.Carry_in.value, dut.Sum.value
    )

    assert dut.Sum.value == 65537, "Carry-in addition result is incorrect"
