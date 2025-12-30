`timescale 1ns / 1ps

module konge_stone_adder (
    input  wire [15:0] A,
    input  wire [15:0] B,
    input  wire        Carry_in,
    output wire [16:0] Sum
);

    wire [15:0] P0, G0;
    assign P0 = A ^ B;
    assign G0 = A & B;

    wire [15:0] P1, G1, P2, G2, P3, G3, P4, G4;

    genvar i;

    // Stage 1
    generate
        for (i = 0; i < 16; i = i + 1) begin
            if (i == 0) begin
                assign P1[i] = P0[i];
                assign G1[i] = G0[i];
            end else begin
                assign P1[i] = P0[i] & P0[i-1];
                assign G1[i] = G0[i] | (P0[i] & G0[i-1]);
            end
        end
    endgenerate

    // Stage 2
    generate
        for (i = 0; i < 16; i = i + 1) begin
            if (i < 2) begin
                assign P2[i] = P1[i];
                assign G2[i] = G1[i];
            end else begin
                assign P2[i] = P1[i] & P1[i-2];
                assign G2[i] = G1[i] | (P1[i] & G1[i-2]);
            end
        end
    endgenerate

    // Stage 3
    generate
        for (i = 0; i < 16; i = i + 1) begin
            if (i < 4) begin
                assign P3[i] = P2[i];
                assign G3[i] = G2[i];
            end else begin
                assign P3[i] = P2[i] & P2[i-4];
                assign G3[i] = G2[i] | (P2[i] & G2[i-4]);
            end
        end
    endgenerate

    // Stage 4
    generate
        for (i = 0; i < 16; i = i + 1) begin
            if (i < 8) begin
                assign P4[i] = P3[i];
                assign G4[i] = G3[i];
            end else begin
                assign P4[i] = P3[i] & P3[i-8];
                assign G4[i] = G3[i] | (P3[i] & G3[i-8]);
            end
        end
    endgenerate

    // Carry computation
    wire [16:0] C;
    assign C[0] = Carry_in;

    generate
        for (i = 0; i < 16; i = i + 1)
            assign C[i+1] = G4[i] | (P4[i] & Carry_in);
    endgenerate

    // Sum
    assign Sum[0] = P0[0] ^ Carry_in;
    generate
        for (i = 1; i < 16; i = i + 1)
            assign Sum[i] = P0[i] ^ C[i];
    endgenerate

    assign Sum[16] = C[16];

endmodule
