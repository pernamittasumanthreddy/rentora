package com.rentora.fleet;

import java.util.*;

public class VehicleDiagnosticCodes {
    private static final Map<String, DiagnosticTroubleCode> DTC_CATALOG = new HashMap<>();

    static {
        for (int i = 1; i <= 150; i++) {
            DiagnosticTroubleCode dtc = lookupByIndex(i);
            if (dtc != null) DTC_CATALOG.put(dtc.getCode(), dtc);
        }
    }

    public static DiagnosticTroubleCode lookupByIndex(int idx) {
        switch (idx) {
            case 1: return getDtcRecord1();
            case 2: return getDtcRecord2();
            case 3: return getDtcRecord3();
            case 4: return getDtcRecord4();
            case 5: return getDtcRecord5();
            case 6: return getDtcRecord6();
            case 7: return getDtcRecord7();
            case 8: return getDtcRecord8();
            case 9: return getDtcRecord9();
            case 10: return getDtcRecord10();
            case 11: return getDtcRecord11();
            case 12: return getDtcRecord12();
            case 13: return getDtcRecord13();
            case 14: return getDtcRecord14();
            case 15: return getDtcRecord15();
            case 16: return getDtcRecord16();
            case 17: return getDtcRecord17();
            case 18: return getDtcRecord18();
            case 19: return getDtcRecord19();
            case 20: return getDtcRecord20();
            case 21: return getDtcRecord21();
            case 22: return getDtcRecord22();
            case 23: return getDtcRecord23();
            case 24: return getDtcRecord24();
            case 25: return getDtcRecord25();
            case 26: return getDtcRecord26();
            case 27: return getDtcRecord27();
            case 28: return getDtcRecord28();
            case 29: return getDtcRecord29();
            case 30: return getDtcRecord30();
            case 31: return getDtcRecord31();
            case 32: return getDtcRecord32();
            case 33: return getDtcRecord33();
            case 34: return getDtcRecord34();
            case 35: return getDtcRecord35();
            case 36: return getDtcRecord36();
            case 37: return getDtcRecord37();
            case 38: return getDtcRecord38();
            case 39: return getDtcRecord39();
            case 40: return getDtcRecord40();
            case 41: return getDtcRecord41();
            case 42: return getDtcRecord42();
            case 43: return getDtcRecord43();
            case 44: return getDtcRecord44();
            case 45: return getDtcRecord45();
            case 46: return getDtcRecord46();
            case 47: return getDtcRecord47();
            case 48: return getDtcRecord48();
            case 49: return getDtcRecord49();
            case 50: return getDtcRecord50();
            case 51: return getDtcRecord51();
            case 52: return getDtcRecord52();
            case 53: return getDtcRecord53();
            case 54: return getDtcRecord54();
            case 55: return getDtcRecord55();
            case 56: return getDtcRecord56();
            case 57: return getDtcRecord57();
            case 58: return getDtcRecord58();
            case 59: return getDtcRecord59();
            case 60: return getDtcRecord60();
            case 61: return getDtcRecord61();
            case 62: return getDtcRecord62();
            case 63: return getDtcRecord63();
            case 64: return getDtcRecord64();
            case 65: return getDtcRecord65();
            case 66: return getDtcRecord66();
            case 67: return getDtcRecord67();
            case 68: return getDtcRecord68();
            case 69: return getDtcRecord69();
            case 70: return getDtcRecord70();
            case 71: return getDtcRecord71();
            case 72: return getDtcRecord72();
            case 73: return getDtcRecord73();
            case 74: return getDtcRecord74();
            case 75: return getDtcRecord75();
            case 76: return getDtcRecord76();
            case 77: return getDtcRecord77();
            case 78: return getDtcRecord78();
            case 79: return getDtcRecord79();
            case 80: return getDtcRecord80();
            case 81: return getDtcRecord81();
            case 82: return getDtcRecord82();
            case 83: return getDtcRecord83();
            case 84: return getDtcRecord84();
            case 85: return getDtcRecord85();
            case 86: return getDtcRecord86();
            case 87: return getDtcRecord87();
            case 88: return getDtcRecord88();
            case 89: return getDtcRecord89();
            case 90: return getDtcRecord90();
            case 91: return getDtcRecord91();
            case 92: return getDtcRecord92();
            case 93: return getDtcRecord93();
            case 94: return getDtcRecord94();
            case 95: return getDtcRecord95();
            case 96: return getDtcRecord96();
            case 97: return getDtcRecord97();
            case 98: return getDtcRecord98();
            case 99: return getDtcRecord99();
            case 100: return getDtcRecord100();
            case 101: return getDtcRecord101();
            case 102: return getDtcRecord102();
            case 103: return getDtcRecord103();
            case 104: return getDtcRecord104();
            case 105: return getDtcRecord105();
            case 106: return getDtcRecord106();
            case 107: return getDtcRecord107();
            case 108: return getDtcRecord108();
            case 109: return getDtcRecord109();
            case 110: return getDtcRecord110();
            case 111: return getDtcRecord111();
            case 112: return getDtcRecord112();
            case 113: return getDtcRecord113();
            case 114: return getDtcRecord114();
            case 115: return getDtcRecord115();
            case 116: return getDtcRecord116();
            case 117: return getDtcRecord117();
            case 118: return getDtcRecord118();
            case 119: return getDtcRecord119();
            case 120: return getDtcRecord120();
            case 121: return getDtcRecord121();
            case 122: return getDtcRecord122();
            case 123: return getDtcRecord123();
            case 124: return getDtcRecord124();
            case 125: return getDtcRecord125();
            case 126: return getDtcRecord126();
            case 127: return getDtcRecord127();
            case 128: return getDtcRecord128();
            case 129: return getDtcRecord129();
            case 130: return getDtcRecord130();
            case 131: return getDtcRecord131();
            case 132: return getDtcRecord132();
            case 133: return getDtcRecord133();
            case 134: return getDtcRecord134();
            case 135: return getDtcRecord135();
            case 136: return getDtcRecord136();
            case 137: return getDtcRecord137();
            case 138: return getDtcRecord138();
            case 139: return getDtcRecord139();
            case 140: return getDtcRecord140();
            case 141: return getDtcRecord141();
            case 142: return getDtcRecord142();
            case 143: return getDtcRecord143();
            case 144: return getDtcRecord144();
            case 145: return getDtcRecord145();
            case 146: return getDtcRecord146();
            case 147: return getDtcRecord147();
            case 148: return getDtcRecord148();
            case 149: return getDtcRecord149();
            case 150: return getDtcRecord150();

            default: return new DiagnosticTroubleCode("P0000", "Normal Diagnostic Status", "INFO", "NODE_0", "System normal");
        }
    }

    public static Optional<DiagnosticTroubleCode> getCode(String code) {
        return Optional.ofNullable(DTC_CATALOG.get(code));
    }

    public static DiagnosticTroubleCode getDtcRecord1() {
        return new DiagnosticTroubleCode(
            "P0101",
            "Powertrain Sensor Diagnostic Subsystem Check #1",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #2, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord2() {
        return new DiagnosticTroubleCode(
            "P0102",
            "Powertrain Sensor Diagnostic Subsystem Check #2",
            "MEDIUM",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #3, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord3() {
        return new DiagnosticTroubleCode(
            "P0103",
            "Powertrain Sensor Diagnostic Subsystem Check #3",
            "HIGH",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #4, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord4() {
        return new DiagnosticTroubleCode(
            "P0104",
            "Powertrain Sensor Diagnostic Subsystem Check #4",
            "MEDIUM",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #5, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord5() {
        return new DiagnosticTroubleCode(
            "P0105",
            "Powertrain Sensor Diagnostic Subsystem Check #5",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #6, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord6() {
        return new DiagnosticTroubleCode(
            "P0106",
            "Powertrain Sensor Diagnostic Subsystem Check #6",
            "HIGH",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #7, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord7() {
        return new DiagnosticTroubleCode(
            "P0107",
            "Powertrain Sensor Diagnostic Subsystem Check #7",
            "MEDIUM",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #8, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord8() {
        return new DiagnosticTroubleCode(
            "P0108",
            "Powertrain Sensor Diagnostic Subsystem Check #8",
            "MEDIUM",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #9, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord9() {
        return new DiagnosticTroubleCode(
            "P0109",
            "Powertrain Sensor Diagnostic Subsystem Check #9",
            "HIGH",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #10, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord10() {
        return new DiagnosticTroubleCode(
            "P0110",
            "Powertrain Sensor Diagnostic Subsystem Check #10",
            "CRITICAL",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #11, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord11() {
        return new DiagnosticTroubleCode(
            "P0111",
            "Powertrain Sensor Diagnostic Subsystem Check #11",
            "MEDIUM",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #12, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord12() {
        return new DiagnosticTroubleCode(
            "P0112",
            "Powertrain Sensor Diagnostic Subsystem Check #12",
            "HIGH",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #13, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord13() {
        return new DiagnosticTroubleCode(
            "P0113",
            "Powertrain Sensor Diagnostic Subsystem Check #13",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #14, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord14() {
        return new DiagnosticTroubleCode(
            "P0114",
            "Powertrain Sensor Diagnostic Subsystem Check #14",
            "MEDIUM",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #15, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord15() {
        return new DiagnosticTroubleCode(
            "P0115",
            "Powertrain Sensor Diagnostic Subsystem Check #15",
            "HIGH",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #16, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord16() {
        return new DiagnosticTroubleCode(
            "P0116",
            "Powertrain Sensor Diagnostic Subsystem Check #16",
            "MEDIUM",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #1, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord17() {
        return new DiagnosticTroubleCode(
            "P0117",
            "Powertrain Sensor Diagnostic Subsystem Check #17",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #2, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord18() {
        return new DiagnosticTroubleCode(
            "P0118",
            "Powertrain Sensor Diagnostic Subsystem Check #18",
            "HIGH",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #3, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord19() {
        return new DiagnosticTroubleCode(
            "P0119",
            "Powertrain Sensor Diagnostic Subsystem Check #19",
            "MEDIUM",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #4, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord20() {
        return new DiagnosticTroubleCode(
            "P0120",
            "Powertrain Sensor Diagnostic Subsystem Check #20",
            "CRITICAL",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #5, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord21() {
        return new DiagnosticTroubleCode(
            "P0121",
            "Powertrain Sensor Diagnostic Subsystem Check #21",
            "HIGH",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #6, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord22() {
        return new DiagnosticTroubleCode(
            "P0122",
            "Powertrain Sensor Diagnostic Subsystem Check #22",
            "MEDIUM",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #7, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord23() {
        return new DiagnosticTroubleCode(
            "P0123",
            "Powertrain Sensor Diagnostic Subsystem Check #23",
            "MEDIUM",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #8, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord24() {
        return new DiagnosticTroubleCode(
            "P0124",
            "Powertrain Sensor Diagnostic Subsystem Check #24",
            "HIGH",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #9, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord25() {
        return new DiagnosticTroubleCode(
            "P0125",
            "Powertrain Sensor Diagnostic Subsystem Check #25",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #10, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord26() {
        return new DiagnosticTroubleCode(
            "P0126",
            "Powertrain Sensor Diagnostic Subsystem Check #26",
            "MEDIUM",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #11, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord27() {
        return new DiagnosticTroubleCode(
            "P0127",
            "Powertrain Sensor Diagnostic Subsystem Check #27",
            "HIGH",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #12, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord28() {
        return new DiagnosticTroubleCode(
            "P0128",
            "Powertrain Sensor Diagnostic Subsystem Check #28",
            "MEDIUM",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #13, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord29() {
        return new DiagnosticTroubleCode(
            "P0129",
            "Powertrain Sensor Diagnostic Subsystem Check #29",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #14, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord30() {
        return new DiagnosticTroubleCode(
            "P0130",
            "Powertrain Sensor Diagnostic Subsystem Check #30",
            "CRITICAL",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #15, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord31() {
        return new DiagnosticTroubleCode(
            "P0131",
            "Powertrain Sensor Diagnostic Subsystem Check #31",
            "MEDIUM",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #16, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord32() {
        return new DiagnosticTroubleCode(
            "P0132",
            "Powertrain Sensor Diagnostic Subsystem Check #32",
            "MEDIUM",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #1, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord33() {
        return new DiagnosticTroubleCode(
            "P0133",
            "Powertrain Sensor Diagnostic Subsystem Check #33",
            "HIGH",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #2, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord34() {
        return new DiagnosticTroubleCode(
            "P0134",
            "Powertrain Sensor Diagnostic Subsystem Check #34",
            "MEDIUM",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #3, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord35() {
        return new DiagnosticTroubleCode(
            "P0135",
            "Powertrain Sensor Diagnostic Subsystem Check #35",
            "MEDIUM",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #4, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord36() {
        return new DiagnosticTroubleCode(
            "P0136",
            "Powertrain Sensor Diagnostic Subsystem Check #36",
            "HIGH",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #5, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord37() {
        return new DiagnosticTroubleCode(
            "P0137",
            "Powertrain Sensor Diagnostic Subsystem Check #37",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #6, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord38() {
        return new DiagnosticTroubleCode(
            "P0138",
            "Powertrain Sensor Diagnostic Subsystem Check #38",
            "MEDIUM",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #7, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord39() {
        return new DiagnosticTroubleCode(
            "P0139",
            "Powertrain Sensor Diagnostic Subsystem Check #39",
            "HIGH",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #8, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord40() {
        return new DiagnosticTroubleCode(
            "P0140",
            "Powertrain Sensor Diagnostic Subsystem Check #40",
            "CRITICAL",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #9, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord41() {
        return new DiagnosticTroubleCode(
            "P0141",
            "Powertrain Sensor Diagnostic Subsystem Check #41",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #10, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord42() {
        return new DiagnosticTroubleCode(
            "P0142",
            "Powertrain Sensor Diagnostic Subsystem Check #42",
            "HIGH",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #11, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord43() {
        return new DiagnosticTroubleCode(
            "P0143",
            "Powertrain Sensor Diagnostic Subsystem Check #43",
            "MEDIUM",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #12, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord44() {
        return new DiagnosticTroubleCode(
            "P0144",
            "Powertrain Sensor Diagnostic Subsystem Check #44",
            "MEDIUM",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #13, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord45() {
        return new DiagnosticTroubleCode(
            "P0145",
            "Powertrain Sensor Diagnostic Subsystem Check #45",
            "HIGH",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #14, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord46() {
        return new DiagnosticTroubleCode(
            "P0146",
            "Powertrain Sensor Diagnostic Subsystem Check #46",
            "MEDIUM",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #15, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord47() {
        return new DiagnosticTroubleCode(
            "P0147",
            "Powertrain Sensor Diagnostic Subsystem Check #47",
            "MEDIUM",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #16, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord48() {
        return new DiagnosticTroubleCode(
            "P0148",
            "Powertrain Sensor Diagnostic Subsystem Check #48",
            "HIGH",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #1, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord49() {
        return new DiagnosticTroubleCode(
            "P0149",
            "Powertrain Sensor Diagnostic Subsystem Check #49",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #2, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord50() {
        return new DiagnosticTroubleCode(
            "P0150",
            "Powertrain Sensor Diagnostic Subsystem Check #50",
            "CRITICAL",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #3, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord51() {
        return new DiagnosticTroubleCode(
            "P0151",
            "Powertrain Sensor Diagnostic Subsystem Check #51",
            "HIGH",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #4, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord52() {
        return new DiagnosticTroubleCode(
            "P0152",
            "Powertrain Sensor Diagnostic Subsystem Check #52",
            "MEDIUM",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #5, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord53() {
        return new DiagnosticTroubleCode(
            "P0153",
            "Powertrain Sensor Diagnostic Subsystem Check #53",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #6, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord54() {
        return new DiagnosticTroubleCode(
            "P0154",
            "Powertrain Sensor Diagnostic Subsystem Check #54",
            "HIGH",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #7, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord55() {
        return new DiagnosticTroubleCode(
            "P0155",
            "Powertrain Sensor Diagnostic Subsystem Check #55",
            "MEDIUM",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #8, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord56() {
        return new DiagnosticTroubleCode(
            "P0156",
            "Powertrain Sensor Diagnostic Subsystem Check #56",
            "MEDIUM",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #9, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord57() {
        return new DiagnosticTroubleCode(
            "P0157",
            "Powertrain Sensor Diagnostic Subsystem Check #57",
            "HIGH",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #10, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord58() {
        return new DiagnosticTroubleCode(
            "P0158",
            "Powertrain Sensor Diagnostic Subsystem Check #58",
            "MEDIUM",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #11, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord59() {
        return new DiagnosticTroubleCode(
            "P0159",
            "Powertrain Sensor Diagnostic Subsystem Check #59",
            "MEDIUM",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #12, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord60() {
        return new DiagnosticTroubleCode(
            "P0160",
            "Powertrain Sensor Diagnostic Subsystem Check #60",
            "CRITICAL",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #13, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord61() {
        return new DiagnosticTroubleCode(
            "P0161",
            "Powertrain Sensor Diagnostic Subsystem Check #61",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #14, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord62() {
        return new DiagnosticTroubleCode(
            "P0162",
            "Powertrain Sensor Diagnostic Subsystem Check #62",
            "MEDIUM",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #15, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord63() {
        return new DiagnosticTroubleCode(
            "P0163",
            "Powertrain Sensor Diagnostic Subsystem Check #63",
            "HIGH",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #16, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord64() {
        return new DiagnosticTroubleCode(
            "P0164",
            "Powertrain Sensor Diagnostic Subsystem Check #64",
            "MEDIUM",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #1, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord65() {
        return new DiagnosticTroubleCode(
            "P0165",
            "Powertrain Sensor Diagnostic Subsystem Check #65",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #2, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord66() {
        return new DiagnosticTroubleCode(
            "P0166",
            "Powertrain Sensor Diagnostic Subsystem Check #66",
            "HIGH",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #3, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord67() {
        return new DiagnosticTroubleCode(
            "P0167",
            "Powertrain Sensor Diagnostic Subsystem Check #67",
            "MEDIUM",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #4, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord68() {
        return new DiagnosticTroubleCode(
            "P0168",
            "Powertrain Sensor Diagnostic Subsystem Check #68",
            "MEDIUM",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #5, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord69() {
        return new DiagnosticTroubleCode(
            "P0169",
            "Powertrain Sensor Diagnostic Subsystem Check #69",
            "HIGH",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #6, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord70() {
        return new DiagnosticTroubleCode(
            "P0170",
            "Powertrain Sensor Diagnostic Subsystem Check #70",
            "CRITICAL",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #7, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord71() {
        return new DiagnosticTroubleCode(
            "P0171",
            "Powertrain Sensor Diagnostic Subsystem Check #71",
            "MEDIUM",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #8, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord72() {
        return new DiagnosticTroubleCode(
            "P0172",
            "Powertrain Sensor Diagnostic Subsystem Check #72",
            "HIGH",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #9, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord73() {
        return new DiagnosticTroubleCode(
            "P0173",
            "Powertrain Sensor Diagnostic Subsystem Check #73",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #10, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord74() {
        return new DiagnosticTroubleCode(
            "P0174",
            "Powertrain Sensor Diagnostic Subsystem Check #74",
            "MEDIUM",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #11, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord75() {
        return new DiagnosticTroubleCode(
            "P0175",
            "Powertrain Sensor Diagnostic Subsystem Check #75",
            "HIGH",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #12, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord76() {
        return new DiagnosticTroubleCode(
            "P0176",
            "Powertrain Sensor Diagnostic Subsystem Check #76",
            "MEDIUM",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #13, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord77() {
        return new DiagnosticTroubleCode(
            "P0177",
            "Powertrain Sensor Diagnostic Subsystem Check #77",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #14, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord78() {
        return new DiagnosticTroubleCode(
            "P0178",
            "Powertrain Sensor Diagnostic Subsystem Check #78",
            "HIGH",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #15, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord79() {
        return new DiagnosticTroubleCode(
            "P0179",
            "Powertrain Sensor Diagnostic Subsystem Check #79",
            "MEDIUM",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #16, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord80() {
        return new DiagnosticTroubleCode(
            "P0180",
            "Powertrain Sensor Diagnostic Subsystem Check #80",
            "CRITICAL",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #1, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord81() {
        return new DiagnosticTroubleCode(
            "P0181",
            "Powertrain Sensor Diagnostic Subsystem Check #81",
            "HIGH",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #2, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord82() {
        return new DiagnosticTroubleCode(
            "P0182",
            "Powertrain Sensor Diagnostic Subsystem Check #82",
            "MEDIUM",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #3, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord83() {
        return new DiagnosticTroubleCode(
            "P0183",
            "Powertrain Sensor Diagnostic Subsystem Check #83",
            "MEDIUM",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #4, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord84() {
        return new DiagnosticTroubleCode(
            "P0184",
            "Powertrain Sensor Diagnostic Subsystem Check #84",
            "HIGH",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #5, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord85() {
        return new DiagnosticTroubleCode(
            "P0185",
            "Powertrain Sensor Diagnostic Subsystem Check #85",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #6, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord86() {
        return new DiagnosticTroubleCode(
            "P0186",
            "Powertrain Sensor Diagnostic Subsystem Check #86",
            "MEDIUM",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #7, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord87() {
        return new DiagnosticTroubleCode(
            "P0187",
            "Powertrain Sensor Diagnostic Subsystem Check #87",
            "HIGH",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #8, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord88() {
        return new DiagnosticTroubleCode(
            "P0188",
            "Powertrain Sensor Diagnostic Subsystem Check #88",
            "MEDIUM",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #9, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord89() {
        return new DiagnosticTroubleCode(
            "P0189",
            "Powertrain Sensor Diagnostic Subsystem Check #89",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #10, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord90() {
        return new DiagnosticTroubleCode(
            "P0190",
            "Powertrain Sensor Diagnostic Subsystem Check #90",
            "CRITICAL",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #11, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord91() {
        return new DiagnosticTroubleCode(
            "P0191",
            "Powertrain Sensor Diagnostic Subsystem Check #91",
            "MEDIUM",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #12, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord92() {
        return new DiagnosticTroubleCode(
            "P0192",
            "Powertrain Sensor Diagnostic Subsystem Check #92",
            "MEDIUM",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #13, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord93() {
        return new DiagnosticTroubleCode(
            "P0193",
            "Powertrain Sensor Diagnostic Subsystem Check #93",
            "HIGH",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #14, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord94() {
        return new DiagnosticTroubleCode(
            "P0194",
            "Powertrain Sensor Diagnostic Subsystem Check #94",
            "MEDIUM",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #15, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord95() {
        return new DiagnosticTroubleCode(
            "P0195",
            "Powertrain Sensor Diagnostic Subsystem Check #95",
            "MEDIUM",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #16, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord96() {
        return new DiagnosticTroubleCode(
            "P0196",
            "Powertrain Sensor Diagnostic Subsystem Check #96",
            "HIGH",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #1, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord97() {
        return new DiagnosticTroubleCode(
            "P0197",
            "Powertrain Sensor Diagnostic Subsystem Check #97",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #2, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord98() {
        return new DiagnosticTroubleCode(
            "P0198",
            "Powertrain Sensor Diagnostic Subsystem Check #98",
            "MEDIUM",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #3, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord99() {
        return new DiagnosticTroubleCode(
            "P0199",
            "Powertrain Sensor Diagnostic Subsystem Check #99",
            "HIGH",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #4, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord100() {
        return new DiagnosticTroubleCode(
            "P0200",
            "Powertrain Sensor Diagnostic Subsystem Check #100",
            "CRITICAL",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #5, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord101() {
        return new DiagnosticTroubleCode(
            "P0201",
            "Powertrain Sensor Diagnostic Subsystem Check #101",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #6, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord102() {
        return new DiagnosticTroubleCode(
            "P0202",
            "Powertrain Sensor Diagnostic Subsystem Check #102",
            "HIGH",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #7, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord103() {
        return new DiagnosticTroubleCode(
            "P0203",
            "Powertrain Sensor Diagnostic Subsystem Check #103",
            "MEDIUM",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #8, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord104() {
        return new DiagnosticTroubleCode(
            "P0204",
            "Powertrain Sensor Diagnostic Subsystem Check #104",
            "MEDIUM",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #9, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord105() {
        return new DiagnosticTroubleCode(
            "P0205",
            "Powertrain Sensor Diagnostic Subsystem Check #105",
            "HIGH",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #10, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord106() {
        return new DiagnosticTroubleCode(
            "P0206",
            "Powertrain Sensor Diagnostic Subsystem Check #106",
            "MEDIUM",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #11, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord107() {
        return new DiagnosticTroubleCode(
            "P0207",
            "Powertrain Sensor Diagnostic Subsystem Check #107",
            "MEDIUM",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #12, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord108() {
        return new DiagnosticTroubleCode(
            "P0208",
            "Powertrain Sensor Diagnostic Subsystem Check #108",
            "HIGH",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #13, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord109() {
        return new DiagnosticTroubleCode(
            "P0209",
            "Powertrain Sensor Diagnostic Subsystem Check #109",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #14, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord110() {
        return new DiagnosticTroubleCode(
            "P0210",
            "Powertrain Sensor Diagnostic Subsystem Check #110",
            "CRITICAL",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #15, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord111() {
        return new DiagnosticTroubleCode(
            "P0211",
            "Powertrain Sensor Diagnostic Subsystem Check #111",
            "HIGH",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #16, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord112() {
        return new DiagnosticTroubleCode(
            "P0212",
            "Powertrain Sensor Diagnostic Subsystem Check #112",
            "MEDIUM",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #1, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord113() {
        return new DiagnosticTroubleCode(
            "P0213",
            "Powertrain Sensor Diagnostic Subsystem Check #113",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #2, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord114() {
        return new DiagnosticTroubleCode(
            "P0214",
            "Powertrain Sensor Diagnostic Subsystem Check #114",
            "HIGH",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #3, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord115() {
        return new DiagnosticTroubleCode(
            "P0215",
            "Powertrain Sensor Diagnostic Subsystem Check #115",
            "MEDIUM",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #4, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord116() {
        return new DiagnosticTroubleCode(
            "P0216",
            "Powertrain Sensor Diagnostic Subsystem Check #116",
            "MEDIUM",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #5, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord117() {
        return new DiagnosticTroubleCode(
            "P0217",
            "Powertrain Sensor Diagnostic Subsystem Check #117",
            "HIGH",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #6, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord118() {
        return new DiagnosticTroubleCode(
            "P0218",
            "Powertrain Sensor Diagnostic Subsystem Check #118",
            "MEDIUM",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #7, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord119() {
        return new DiagnosticTroubleCode(
            "P0219",
            "Powertrain Sensor Diagnostic Subsystem Check #119",
            "MEDIUM",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #8, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord120() {
        return new DiagnosticTroubleCode(
            "P0220",
            "Powertrain Sensor Diagnostic Subsystem Check #120",
            "CRITICAL",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #9, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord121() {
        return new DiagnosticTroubleCode(
            "P0221",
            "Powertrain Sensor Diagnostic Subsystem Check #121",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #10, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord122() {
        return new DiagnosticTroubleCode(
            "P0222",
            "Powertrain Sensor Diagnostic Subsystem Check #122",
            "MEDIUM",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #11, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord123() {
        return new DiagnosticTroubleCode(
            "P0223",
            "Powertrain Sensor Diagnostic Subsystem Check #123",
            "HIGH",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #12, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord124() {
        return new DiagnosticTroubleCode(
            "P0224",
            "Powertrain Sensor Diagnostic Subsystem Check #124",
            "MEDIUM",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #13, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord125() {
        return new DiagnosticTroubleCode(
            "P0225",
            "Powertrain Sensor Diagnostic Subsystem Check #125",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #14, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord126() {
        return new DiagnosticTroubleCode(
            "P0226",
            "Powertrain Sensor Diagnostic Subsystem Check #126",
            "HIGH",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #15, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord127() {
        return new DiagnosticTroubleCode(
            "P0227",
            "Powertrain Sensor Diagnostic Subsystem Check #127",
            "MEDIUM",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #16, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord128() {
        return new DiagnosticTroubleCode(
            "P0228",
            "Powertrain Sensor Diagnostic Subsystem Check #128",
            "MEDIUM",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #1, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord129() {
        return new DiagnosticTroubleCode(
            "P0229",
            "Powertrain Sensor Diagnostic Subsystem Check #129",
            "HIGH",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #2, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord130() {
        return new DiagnosticTroubleCode(
            "P0230",
            "Powertrain Sensor Diagnostic Subsystem Check #130",
            "CRITICAL",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #3, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord131() {
        return new DiagnosticTroubleCode(
            "P0231",
            "Powertrain Sensor Diagnostic Subsystem Check #131",
            "MEDIUM",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #4, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord132() {
        return new DiagnosticTroubleCode(
            "P0232",
            "Powertrain Sensor Diagnostic Subsystem Check #132",
            "HIGH",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #5, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord133() {
        return new DiagnosticTroubleCode(
            "P0233",
            "Powertrain Sensor Diagnostic Subsystem Check #133",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #6, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord134() {
        return new DiagnosticTroubleCode(
            "P0234",
            "Powertrain Sensor Diagnostic Subsystem Check #134",
            "MEDIUM",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #7, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord135() {
        return new DiagnosticTroubleCode(
            "P0235",
            "Powertrain Sensor Diagnostic Subsystem Check #135",
            "HIGH",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #8, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord136() {
        return new DiagnosticTroubleCode(
            "P0236",
            "Powertrain Sensor Diagnostic Subsystem Check #136",
            "MEDIUM",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #9, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord137() {
        return new DiagnosticTroubleCode(
            "P0237",
            "Powertrain Sensor Diagnostic Subsystem Check #137",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #10, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord138() {
        return new DiagnosticTroubleCode(
            "P0238",
            "Powertrain Sensor Diagnostic Subsystem Check #138",
            "HIGH",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #11, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord139() {
        return new DiagnosticTroubleCode(
            "P0239",
            "Powertrain Sensor Diagnostic Subsystem Check #139",
            "MEDIUM",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #12, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord140() {
        return new DiagnosticTroubleCode(
            "P0240",
            "Powertrain Sensor Diagnostic Subsystem Check #140",
            "CRITICAL",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #13, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord141() {
        return new DiagnosticTroubleCode(
            "P0241",
            "Powertrain Sensor Diagnostic Subsystem Check #141",
            "HIGH",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #14, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord142() {
        return new DiagnosticTroubleCode(
            "P0242",
            "Powertrain Sensor Diagnostic Subsystem Check #142",
            "MEDIUM",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #15, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord143() {
        return new DiagnosticTroubleCode(
            "P0243",
            "Powertrain Sensor Diagnostic Subsystem Check #143",
            "MEDIUM",
            "CAN_BUS_NODE_7",
            "Inspect wiring harness connector pin #16, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord144() {
        return new DiagnosticTroubleCode(
            "P0244",
            "Powertrain Sensor Diagnostic Subsystem Check #144",
            "HIGH",
            "CAN_BUS_NODE_0",
            "Inspect wiring harness connector pin #1, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord145() {
        return new DiagnosticTroubleCode(
            "P0245",
            "Powertrain Sensor Diagnostic Subsystem Check #145",
            "MEDIUM",
            "CAN_BUS_NODE_1",
            "Inspect wiring harness connector pin #2, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord146() {
        return new DiagnosticTroubleCode(
            "P0246",
            "Powertrain Sensor Diagnostic Subsystem Check #146",
            "MEDIUM",
            "CAN_BUS_NODE_2",
            "Inspect wiring harness connector pin #3, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord147() {
        return new DiagnosticTroubleCode(
            "P0247",
            "Powertrain Sensor Diagnostic Subsystem Check #147",
            "HIGH",
            "CAN_BUS_NODE_3",
            "Inspect wiring harness connector pin #4, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord148() {
        return new DiagnosticTroubleCode(
            "P0248",
            "Powertrain Sensor Diagnostic Subsystem Check #148",
            "MEDIUM",
            "CAN_BUS_NODE_4",
            "Inspect wiring harness connector pin #5, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord149() {
        return new DiagnosticTroubleCode(
            "P0249",
            "Powertrain Sensor Diagnostic Subsystem Check #149",
            "MEDIUM",
            "CAN_BUS_NODE_5",
            "Inspect wiring harness connector pin #6, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

    public static DiagnosticTroubleCode getDtcRecord150() {
        return new DiagnosticTroubleCode(
            "P0250",
            "Powertrain Sensor Diagnostic Subsystem Check #150",
            "CRITICAL",
            "CAN_BUS_NODE_6",
            "Inspect wiring harness connector pin #7, verify ground reference voltage, clear DTC using OBD-II scanner."
        );
    }

}
