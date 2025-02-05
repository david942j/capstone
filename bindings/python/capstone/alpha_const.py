from . import CS_OP_INVALID, CS_OP_REG, CS_OP_IMM, CS_OP_FP, CS_OP_PRED, CS_OP_SPECIAL, CS_OP_MEM, CS_OP_MEM_REG, CS_OP_MEM_IMM, UINT16_MAX
# For Capstone Engine. AUTO-GENERATED FILE, DO NOT EDIT [alpha_const.py]

# Operand type for instruction's operands
ALPHA_OP_INVALID = CS_OP_INVALID
ALPHA_OP_REG = CS_OP_REG
ALPHA_OP_IMM = CS_OP_IMM

# Alpha registers

Alpha_REG_INVALID = 0
Alpha_REG_F0 = 1
Alpha_REG_F1 = 2
Alpha_REG_F2 = 3
Alpha_REG_F3 = 4
Alpha_REG_F4 = 5
Alpha_REG_F5 = 6
Alpha_REG_F6 = 7
Alpha_REG_F7 = 8
Alpha_REG_F8 = 9
Alpha_REG_F9 = 10
Alpha_REG_F10 = 11
Alpha_REG_F11 = 12
Alpha_REG_F12 = 13
Alpha_REG_F13 = 14
Alpha_REG_F14 = 15
Alpha_REG_F15 = 16
Alpha_REG_F16 = 17
Alpha_REG_F17 = 18
Alpha_REG_F18 = 19
Alpha_REG_F19 = 20
Alpha_REG_F20 = 21
Alpha_REG_F21 = 22
Alpha_REG_F22 = 23
Alpha_REG_F23 = 24
Alpha_REG_F24 = 25
Alpha_REG_F25 = 26
Alpha_REG_F26 = 27
Alpha_REG_F27 = 28
Alpha_REG_F28 = 29
Alpha_REG_F29 = 30
Alpha_REG_F30 = 31
Alpha_REG_F31 = 32
Alpha_REG_R0 = 33
Alpha_REG_R1 = 34
Alpha_REG_R2 = 35
Alpha_REG_R3 = 36
Alpha_REG_R4 = 37
Alpha_REG_R5 = 38
Alpha_REG_R6 = 39
Alpha_REG_R7 = 40
Alpha_REG_R8 = 41
Alpha_REG_R9 = 42
Alpha_REG_R10 = 43
Alpha_REG_R11 = 44
Alpha_REG_R12 = 45
Alpha_REG_R13 = 46
Alpha_REG_R14 = 47
Alpha_REG_R15 = 48
Alpha_REG_R16 = 49
Alpha_REG_R17 = 50
Alpha_REG_R18 = 51
Alpha_REG_R19 = 52
Alpha_REG_R20 = 53
Alpha_REG_R21 = 54
Alpha_REG_R22 = 55
Alpha_REG_R23 = 56
Alpha_REG_R24 = 57
Alpha_REG_R25 = 58
Alpha_REG_R26 = 59
Alpha_REG_R27 = 60
Alpha_REG_R28 = 61
Alpha_REG_R29 = 62
Alpha_REG_R30 = 63
Alpha_REG_R31 = 64
Alpha_REG_ENDING = 65

# Alpha instruction

Alpha_INS_INVALID = 0
Alpha_INS_ADDL = 1
Alpha_INS_ADDQ = 2
Alpha_INS_ADDSsSU = 3
Alpha_INS_ADDTsSU = 4
Alpha_INS_AND = 5
Alpha_INS_BEQ = 6
Alpha_INS_BGE = 7
Alpha_INS_BGT = 8
Alpha_INS_BIC = 9
Alpha_INS_BIS = 10
Alpha_INS_BLBC = 11
Alpha_INS_BLBS = 12
Alpha_INS_BLE = 13
Alpha_INS_BLT = 14
Alpha_INS_BNE = 15
Alpha_INS_BR = 16
Alpha_INS_BSR = 17
Alpha_INS_CMOVEQ = 18
Alpha_INS_CMOVGE = 19
Alpha_INS_CMOVGT = 20
Alpha_INS_CMOVLBC = 21
Alpha_INS_CMOVLBS = 22
Alpha_INS_CMOVLE = 23
Alpha_INS_CMOVLT = 24
Alpha_INS_CMOVNE = 25
Alpha_INS_CMPBGE = 26
Alpha_INS_CMPEQ = 27
Alpha_INS_CMPLE = 28
Alpha_INS_CMPLT = 29
Alpha_INS_CMPTEQsSU = 30
Alpha_INS_CMPTLEsSU = 31
Alpha_INS_CMPTLTsSU = 32
Alpha_INS_CMPTUNsSU = 33
Alpha_INS_CMPULE = 34
Alpha_INS_CMPULT = 35
Alpha_INS_COND_BRANCH = 36
Alpha_INS_CPYSE = 37
Alpha_INS_CPYSN = 38
Alpha_INS_CPYS = 39
Alpha_INS_CTLZ = 40
Alpha_INS_CTPOP = 41
Alpha_INS_CTTZ = 42
Alpha_INS_CVTQSsSUI = 43
Alpha_INS_CVTQTsSUI = 44
Alpha_INS_CVTSTsS = 45
Alpha_INS_CVTTQsSVC = 46
Alpha_INS_CVTTSsSUI = 47
Alpha_INS_DIVSsSU = 48
Alpha_INS_DIVTsSU = 49
Alpha_INS_ECB = 50
Alpha_INS_EQV = 51
Alpha_INS_EXCB = 52
Alpha_INS_EXTBL = 53
Alpha_INS_EXTLH = 54
Alpha_INS_EXTLL = 55
Alpha_INS_EXTQH = 56
Alpha_INS_EXTQL = 57
Alpha_INS_EXTWH = 58
Alpha_INS_EXTWL = 59
Alpha_INS_FBEQ = 60
Alpha_INS_FBGE = 61
Alpha_INS_FBGT = 62
Alpha_INS_FBLE = 63
Alpha_INS_FBLT = 64
Alpha_INS_FBNE = 65
Alpha_INS_FCMOVEQ = 66
Alpha_INS_FCMOVGE = 67
Alpha_INS_FCMOVGT = 68
Alpha_INS_FCMOVLE = 69
Alpha_INS_FCMOVLT = 70
Alpha_INS_FCMOVNE = 71
Alpha_INS_FETCH = 72
Alpha_INS_FETCH_M = 73
Alpha_INS_FTOIS = 74
Alpha_INS_FTOIT = 75
Alpha_INS_INSBL = 76
Alpha_INS_INSLH = 77
Alpha_INS_INSLL = 78
Alpha_INS_INSQH = 79
Alpha_INS_INSQL = 80
Alpha_INS_INSWH = 81
Alpha_INS_INSWL = 82
Alpha_INS_ITOFS = 83
Alpha_INS_ITOFT = 84
Alpha_INS_JMP = 85
Alpha_INS_JSR = 86
Alpha_INS_JSR_COROUTINE = 87
Alpha_INS_LDA = 88
Alpha_INS_LDAH = 89
Alpha_INS_LDBU = 90
Alpha_INS_LDL = 91
Alpha_INS_LDL_L = 92
Alpha_INS_LDQ = 93
Alpha_INS_LDQ_L = 94
Alpha_INS_LDQ_U = 95
Alpha_INS_LDS = 96
Alpha_INS_LDT = 97
Alpha_INS_LDWU = 98
Alpha_INS_MB = 99
Alpha_INS_MSKBL = 100
Alpha_INS_MSKLH = 101
Alpha_INS_MSKLL = 102
Alpha_INS_MSKQH = 103
Alpha_INS_MSKQL = 104
Alpha_INS_MSKWH = 105
Alpha_INS_MSKWL = 106
Alpha_INS_MULL = 107
Alpha_INS_MULQ = 108
Alpha_INS_MULSsSU = 109
Alpha_INS_MULTsSU = 110
Alpha_INS_ORNOT = 111
Alpha_INS_RC = 112
Alpha_INS_RET = 113
Alpha_INS_RPCC = 114
Alpha_INS_RS = 115
Alpha_INS_S4ADDL = 116
Alpha_INS_S4ADDQ = 117
Alpha_INS_S4SUBL = 118
Alpha_INS_S4SUBQ = 119
Alpha_INS_S8ADDL = 120
Alpha_INS_S8ADDQ = 121
Alpha_INS_S8SUBL = 122
Alpha_INS_S8SUBQ = 123
Alpha_INS_SEXTB = 124
Alpha_INS_SEXTW = 125
Alpha_INS_SLL = 126
Alpha_INS_SQRTSsSU = 127
Alpha_INS_SQRTTsSU = 128
Alpha_INS_SRA = 129
Alpha_INS_SRL = 130
Alpha_INS_STB = 131
Alpha_INS_STL = 132
Alpha_INS_STL_C = 133
Alpha_INS_STQ = 134
Alpha_INS_STQ_C = 135
Alpha_INS_STQ_U = 136
Alpha_INS_STS = 137
Alpha_INS_STT = 138
Alpha_INS_STW = 139
Alpha_INS_SUBL = 140
Alpha_INS_SUBQ = 141
Alpha_INS_SUBSsSU = 142
Alpha_INS_SUBTsSU = 143
Alpha_INS_TRAPB = 144
Alpha_INS_UMULH = 145
Alpha_INS_WH64 = 146
Alpha_INS_WH64EN = 147
Alpha_INS_WMB = 148
Alpha_INS_XOR = 149
Alpha_INS_ZAPNOT = 150
ALPHA_INS_ENDING = 151

# Group of Alpha instructions

Alpha_GRP_INVALID = 0

# Generic groups
Alpha_GRP_CALL = 1
Alpha_GRP_JUMP = 2
Alpha_GRP_BRANCH_RELATIVE = 3
Alpha_GRP_ENDING = 4
