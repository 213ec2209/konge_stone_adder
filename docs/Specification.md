# Kogge–Stone Adder Documentation

## Overview

Addition is one of the most fundamental operations in digital systems and plays a critical role in processors, digital signal processors (DSPs), cryptographic engines, and hardware accelerators. The performance of an adder directly impacts the overall speed and throughput of a system. Traditional adders such as ripple-carry adders suffer from long propagation delays because each carry bit must wait for the previous bit to complete.

To overcome this limitation, **Parallel Prefix Adders (PPAs)** are widely used in high-performance digital designs. Among them, the **Kogge–Stone Adder (KSA)** is a fast adder architecture that computes carry signals in parallel using a prefix tree structure. It achieves logarithmic carry propagation delay, making it one of the fastest known adder designs. The Kogge–Stone adder trades increased wiring complexity and area for very high speed, which makes it suitable for timing-critical arithmetic paths.

The Kogge–Stone adder described in this document is a **16-bit combinational parallel prefix adder** that supports an external carry-in and produces a 17-bit sum output along with carry signals.

---

## Functionality

### Kogge–Stone Addition Algorithm

In order to understand the Kogge–Stone adder operation, the following parameters are required:

1. First operand (A)
2. Second operand (B)
3. Carry input (Carry_in)
4. Propagate signals (P)
5. Generate signals (G)
6. Carry outputs (Carry_Out)
7. Sum output (Sum)

The Kogge–Stone addition algorithm works as follows:

**Step 1 — Propagate and Generate computation**

For each bit position *i*:

Pᵢ = Aᵢ ⊕ Bᵢ  
Gᵢ = Aᵢ · Bᵢ

**Step 2 — Parallel prefix carry computation**

For each prefix stage *j*, group propagate and generate signals are computed using:

Pⱼ,ᵢ = Pⱼ₋₁,ᵢ ∧ Pⱼ₋₁,ᵢ₋ₖ  
Gⱼ,ᵢ = (Pⱼ₋₁,ᵢ ∧ Gⱼ₋₁,ᵢ₋ₖ) ∨ Gⱼ₋₁,ᵢ

where:

k = 2^(j−1)

**Step 3 — Carry calculation**

Carry_Out₁ = Carry_in

Carry_Outᵢ = (Carry_in ∧ P_group,ᵢ) ∨ G_group,ᵢ

**Step 4 — Sum computation**

Sumᵢ = Carry_Outᵢ ⊕ Pᵢ

The most significant bit of the sum captures the final carry-out.

---

### Signal Interpretation

⊕ : XOR operation  
∧ : AND operation  
∨ : OR operation  
A, B : Input operands  
P : Propagate signal  
G : Generate signal  
Carry_in : External carry input  
Carry_Out : Internal and final carry signals  
Sum : Final addition result

All operations are purely combinational and evaluated in parallel.

---

### FSM-Controlled Process

The Kogge–Stone adder does **not** require a multi-state finite state machine.

- The design is fully combinational
- There are no clock or reset signals
- All outputs update immediately based on changes in inputs

Each input change triggers a complete evaluation of the adder logic.

---

## Working Example

### Kogge–Stone Addition

Let us consider the following parameters:

A = 16'h000F  
B = 16'h0001  
Carry_in = 1'b0

**Solution:**

Initial operands:  
A = 0000 0000 0000 1111  
B = 0000 0000 0000 0001

Binary addition:

Sum = A + B + Carry_in = 16'h0010

Carry propagation occurs in parallel through the prefix tree.

**Final Outputs:**

Sum = 17'h00010  
Carry_Out[17] = 0

---

### Example with Carry-In

A = 16'hFFFF  
B = 16'h0001  
Carry_in = 1'b1

Sum = FFFF + 0001 + 1 = 1_0001

Final result:

Sum = 17'h10001

---
## Summary

The Kogge–Stone adder is a high-speed parallel prefix adder that efficiently computes sum and carry outputs using propagate and generate logic combined with a multi-stage prefix tree. This Verilog implementation provides fast and deterministic addition for 16-bit operands with an external carry-in, making it well suited for performance-critical arithmetic datapaths and HUD evaluation b