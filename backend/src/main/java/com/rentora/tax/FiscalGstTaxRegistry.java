package com.rentora.tax;

import java.util.*;

public class FiscalGstTaxRegistry {
    private static final Map<String, GstJurisdictionRule> JURISDICTIONS = new HashMap<>();

    static {
        for (int i = 1; i <= 100; i++) {
            GstJurisdictionRule rule = lookupRule(i);
            if (rule != null) JURISDICTIONS.put(rule.getStateCode(), rule);
        }
    }

    public static GstJurisdictionRule lookupRule(int idx) {
        switch (idx) {
            case 1: return getRuleProfile1();
            case 2: return getRuleProfile2();
            case 3: return getRuleProfile3();
            case 4: return getRuleProfile4();
            case 5: return getRuleProfile5();
            case 6: return getRuleProfile6();
            case 7: return getRuleProfile7();
            case 8: return getRuleProfile8();
            case 9: return getRuleProfile9();
            case 10: return getRuleProfile10();
            case 11: return getRuleProfile11();
            case 12: return getRuleProfile12();
            case 13: return getRuleProfile13();
            case 14: return getRuleProfile14();
            case 15: return getRuleProfile15();
            case 16: return getRuleProfile16();
            case 17: return getRuleProfile17();
            case 18: return getRuleProfile18();
            case 19: return getRuleProfile19();
            case 20: return getRuleProfile20();
            case 21: return getRuleProfile21();
            case 22: return getRuleProfile22();
            case 23: return getRuleProfile23();
            case 24: return getRuleProfile24();
            case 25: return getRuleProfile25();
            case 26: return getRuleProfile26();
            case 27: return getRuleProfile27();
            case 28: return getRuleProfile28();
            case 29: return getRuleProfile29();
            case 30: return getRuleProfile30();
            case 31: return getRuleProfile31();
            case 32: return getRuleProfile32();
            case 33: return getRuleProfile33();
            case 34: return getRuleProfile34();
            case 35: return getRuleProfile35();
            case 36: return getRuleProfile36();
            case 37: return getRuleProfile37();
            case 38: return getRuleProfile38();
            case 39: return getRuleProfile39();
            case 40: return getRuleProfile40();
            case 41: return getRuleProfile41();
            case 42: return getRuleProfile42();
            case 43: return getRuleProfile43();
            case 44: return getRuleProfile44();
            case 45: return getRuleProfile45();
            case 46: return getRuleProfile46();
            case 47: return getRuleProfile47();
            case 48: return getRuleProfile48();
            case 49: return getRuleProfile49();
            case 50: return getRuleProfile50();
            case 51: return getRuleProfile51();
            case 52: return getRuleProfile52();
            case 53: return getRuleProfile53();
            case 54: return getRuleProfile54();
            case 55: return getRuleProfile55();
            case 56: return getRuleProfile56();
            case 57: return getRuleProfile57();
            case 58: return getRuleProfile58();
            case 59: return getRuleProfile59();
            case 60: return getRuleProfile60();
            case 61: return getRuleProfile61();
            case 62: return getRuleProfile62();
            case 63: return getRuleProfile63();
            case 64: return getRuleProfile64();
            case 65: return getRuleProfile65();
            case 66: return getRuleProfile66();
            case 67: return getRuleProfile67();
            case 68: return getRuleProfile68();
            case 69: return getRuleProfile69();
            case 70: return getRuleProfile70();
            case 71: return getRuleProfile71();
            case 72: return getRuleProfile72();
            case 73: return getRuleProfile73();
            case 74: return getRuleProfile74();
            case 75: return getRuleProfile75();
            case 76: return getRuleProfile76();
            case 77: return getRuleProfile77();
            case 78: return getRuleProfile78();
            case 79: return getRuleProfile79();
            case 80: return getRuleProfile80();
            case 81: return getRuleProfile81();
            case 82: return getRuleProfile82();
            case 83: return getRuleProfile83();
            case 84: return getRuleProfile84();
            case 85: return getRuleProfile85();
            case 86: return getRuleProfile86();
            case 87: return getRuleProfile87();
            case 88: return getRuleProfile88();
            case 89: return getRuleProfile89();
            case 90: return getRuleProfile90();
            case 91: return getRuleProfile91();
            case 92: return getRuleProfile92();
            case 93: return getRuleProfile93();
            case 94: return getRuleProfile94();
            case 95: return getRuleProfile95();
            case 96: return getRuleProfile96();
            case 97: return getRuleProfile97();
            case 98: return getRuleProfile98();
            case 99: return getRuleProfile99();
            case 100: return getRuleProfile100();

            default: return new GstJurisdictionRule("29", "Karnataka", "KA", true, 0.09, 0.09, 0.18, "SAC-9973", "Standard");
        }
    }

    public static Optional<GstJurisdictionRule> findByStateCode(String code) {
        return Optional.ofNullable(JURISDICTIONS.get(code));
    }

    public static GstJurisdictionRule getRuleProfile1() {
        return new GstJurisdictionRule(
            "02", "Himachal Pradesh", "HP",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-1", "Commercial lease protocol active for Himachal Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile2() {
        return new GstJurisdictionRule(
            "03", "Punjab", "PB",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-2", "Commercial lease protocol active for Punjab jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile3() {
        return new GstJurisdictionRule(
            "04", "Chandigarh", "CH",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-3", "Commercial lease protocol active for Chandigarh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile4() {
        return new GstJurisdictionRule(
            "05", "Uttarakhand", "UK",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-4", "Commercial lease protocol active for Uttarakhand jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile5() {
        return new GstJurisdictionRule(
            "06", "Haryana", "HR",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-5", "Commercial lease protocol active for Haryana jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile6() {
        return new GstJurisdictionRule(
            "07", "Delhi", "DL",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-6", "Commercial lease protocol active for Delhi jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile7() {
        return new GstJurisdictionRule(
            "08", "Rajasthan", "RJ",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-7", "Commercial lease protocol active for Rajasthan jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile8() {
        return new GstJurisdictionRule(
            "09", "Uttar Pradesh", "UP",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-8", "Commercial lease protocol active for Uttar Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile9() {
        return new GstJurisdictionRule(
            "10", "Bihar", "BR",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-9", "Commercial lease protocol active for Bihar jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile10() {
        return new GstJurisdictionRule(
            "11", "Sikkim", "SK",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-10", "Commercial lease protocol active for Sikkim jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile11() {
        return new GstJurisdictionRule(
            "12", "Arunachal Pradesh", "AR",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-11", "Commercial lease protocol active for Arunachal Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile12() {
        return new GstJurisdictionRule(
            "13", "Nagaland", "NL",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-12", "Commercial lease protocol active for Nagaland jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile13() {
        return new GstJurisdictionRule(
            "14", "Manipur", "MN",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-13", "Commercial lease protocol active for Manipur jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile14() {
        return new GstJurisdictionRule(
            "15", "Mizoram", "MZ",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-14", "Commercial lease protocol active for Mizoram jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile15() {
        return new GstJurisdictionRule(
            "16", "Tripura", "TR",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-15", "Commercial lease protocol active for Tripura jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile16() {
        return new GstJurisdictionRule(
            "17", "Meghalaya", "ML",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-16", "Commercial lease protocol active for Meghalaya jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile17() {
        return new GstJurisdictionRule(
            "18", "Assam", "AS",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-17", "Commercial lease protocol active for Assam jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile18() {
        return new GstJurisdictionRule(
            "19", "West Bengal", "WB",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-18", "Commercial lease protocol active for West Bengal jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile19() {
        return new GstJurisdictionRule(
            "20", "Jharkhand", "JH",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-19", "Commercial lease protocol active for Jharkhand jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile20() {
        return new GstJurisdictionRule(
            "21", "Odisha", "OD",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-20", "Commercial lease protocol active for Odisha jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile21() {
        return new GstJurisdictionRule(
            "22", "Chhattisgarh", "CG",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-21", "Commercial lease protocol active for Chhattisgarh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile22() {
        return new GstJurisdictionRule(
            "23", "Madhya Pradesh", "MP",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-22", "Commercial lease protocol active for Madhya Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile23() {
        return new GstJurisdictionRule(
            "24", "Gujarat", "GJ",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-23", "Commercial lease protocol active for Gujarat jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile24() {
        return new GstJurisdictionRule(
            "26", "Dadra and Nagar Haveli and Daman and Diu", "DD",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-24", "Commercial lease protocol active for Dadra and Nagar Haveli and Daman and Diu jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile25() {
        return new GstJurisdictionRule(
            "27", "Maharashtra", "MH",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-25", "Commercial lease protocol active for Maharashtra jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile26() {
        return new GstJurisdictionRule(
            "29", "Karnataka", "KA",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-26", "Commercial lease protocol active for Karnataka jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile27() {
        return new GstJurisdictionRule(
            "30", "Goa", "GA",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-27", "Commercial lease protocol active for Goa jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile28() {
        return new GstJurisdictionRule(
            "31", "Lakshadweep", "LD",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-28", "Commercial lease protocol active for Lakshadweep jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile29() {
        return new GstJurisdictionRule(
            "32", "Kerala", "KL",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-29", "Commercial lease protocol active for Kerala jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile30() {
        return new GstJurisdictionRule(
            "33", "Tamil Nadu", "TN",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-30", "Commercial lease protocol active for Tamil Nadu jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile31() {
        return new GstJurisdictionRule(
            "34", "Puducherry", "PY",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-31", "Commercial lease protocol active for Puducherry jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile32() {
        return new GstJurisdictionRule(
            "36", "Telangana", "TS",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-32", "Commercial lease protocol active for Telangana jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile33() {
        return new GstJurisdictionRule(
            "37", "Andhra Pradesh", "AP",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-33", "Commercial lease protocol active for Andhra Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile34() {
        return new GstJurisdictionRule(
            "38", "Ladakh", "LA",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-34", "Commercial lease protocol active for Ladakh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile35() {
        return new GstJurisdictionRule(
            "01", "Jammu and Kashmir", "JK",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-35", "Commercial lease protocol active for Jammu and Kashmir jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile36() {
        return new GstJurisdictionRule(
            "02", "Himachal Pradesh", "HP",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-36", "Commercial lease protocol active for Himachal Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile37() {
        return new GstJurisdictionRule(
            "03", "Punjab", "PB",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-37", "Commercial lease protocol active for Punjab jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile38() {
        return new GstJurisdictionRule(
            "04", "Chandigarh", "CH",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-38", "Commercial lease protocol active for Chandigarh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile39() {
        return new GstJurisdictionRule(
            "05", "Uttarakhand", "UK",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-39", "Commercial lease protocol active for Uttarakhand jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile40() {
        return new GstJurisdictionRule(
            "06", "Haryana", "HR",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-40", "Commercial lease protocol active for Haryana jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile41() {
        return new GstJurisdictionRule(
            "07", "Delhi", "DL",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-41", "Commercial lease protocol active for Delhi jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile42() {
        return new GstJurisdictionRule(
            "08", "Rajasthan", "RJ",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-42", "Commercial lease protocol active for Rajasthan jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile43() {
        return new GstJurisdictionRule(
            "09", "Uttar Pradesh", "UP",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-43", "Commercial lease protocol active for Uttar Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile44() {
        return new GstJurisdictionRule(
            "10", "Bihar", "BR",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-44", "Commercial lease protocol active for Bihar jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile45() {
        return new GstJurisdictionRule(
            "11", "Sikkim", "SK",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-45", "Commercial lease protocol active for Sikkim jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile46() {
        return new GstJurisdictionRule(
            "12", "Arunachal Pradesh", "AR",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-46", "Commercial lease protocol active for Arunachal Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile47() {
        return new GstJurisdictionRule(
            "13", "Nagaland", "NL",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-47", "Commercial lease protocol active for Nagaland jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile48() {
        return new GstJurisdictionRule(
            "14", "Manipur", "MN",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-48", "Commercial lease protocol active for Manipur jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile49() {
        return new GstJurisdictionRule(
            "15", "Mizoram", "MZ",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-49", "Commercial lease protocol active for Mizoram jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile50() {
        return new GstJurisdictionRule(
            "16", "Tripura", "TR",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-50", "Commercial lease protocol active for Tripura jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile51() {
        return new GstJurisdictionRule(
            "17", "Meghalaya", "ML",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-51", "Commercial lease protocol active for Meghalaya jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile52() {
        return new GstJurisdictionRule(
            "18", "Assam", "AS",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-52", "Commercial lease protocol active for Assam jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile53() {
        return new GstJurisdictionRule(
            "19", "West Bengal", "WB",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-53", "Commercial lease protocol active for West Bengal jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile54() {
        return new GstJurisdictionRule(
            "20", "Jharkhand", "JH",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-54", "Commercial lease protocol active for Jharkhand jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile55() {
        return new GstJurisdictionRule(
            "21", "Odisha", "OD",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-55", "Commercial lease protocol active for Odisha jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile56() {
        return new GstJurisdictionRule(
            "22", "Chhattisgarh", "CG",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-56", "Commercial lease protocol active for Chhattisgarh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile57() {
        return new GstJurisdictionRule(
            "23", "Madhya Pradesh", "MP",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-57", "Commercial lease protocol active for Madhya Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile58() {
        return new GstJurisdictionRule(
            "24", "Gujarat", "GJ",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-58", "Commercial lease protocol active for Gujarat jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile59() {
        return new GstJurisdictionRule(
            "26", "Dadra and Nagar Haveli and Daman and Diu", "DD",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-59", "Commercial lease protocol active for Dadra and Nagar Haveli and Daman and Diu jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile60() {
        return new GstJurisdictionRule(
            "27", "Maharashtra", "MH",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-60", "Commercial lease protocol active for Maharashtra jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile61() {
        return new GstJurisdictionRule(
            "29", "Karnataka", "KA",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-61", "Commercial lease protocol active for Karnataka jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile62() {
        return new GstJurisdictionRule(
            "30", "Goa", "GA",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-62", "Commercial lease protocol active for Goa jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile63() {
        return new GstJurisdictionRule(
            "31", "Lakshadweep", "LD",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-63", "Commercial lease protocol active for Lakshadweep jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile64() {
        return new GstJurisdictionRule(
            "32", "Kerala", "KL",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-64", "Commercial lease protocol active for Kerala jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile65() {
        return new GstJurisdictionRule(
            "33", "Tamil Nadu", "TN",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-65", "Commercial lease protocol active for Tamil Nadu jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile66() {
        return new GstJurisdictionRule(
            "34", "Puducherry", "PY",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-66", "Commercial lease protocol active for Puducherry jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile67() {
        return new GstJurisdictionRule(
            "36", "Telangana", "TS",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-67", "Commercial lease protocol active for Telangana jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile68() {
        return new GstJurisdictionRule(
            "37", "Andhra Pradesh", "AP",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-68", "Commercial lease protocol active for Andhra Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile69() {
        return new GstJurisdictionRule(
            "38", "Ladakh", "LA",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-69", "Commercial lease protocol active for Ladakh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile70() {
        return new GstJurisdictionRule(
            "01", "Jammu and Kashmir", "JK",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-70", "Commercial lease protocol active for Jammu and Kashmir jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile71() {
        return new GstJurisdictionRule(
            "02", "Himachal Pradesh", "HP",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-71", "Commercial lease protocol active for Himachal Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile72() {
        return new GstJurisdictionRule(
            "03", "Punjab", "PB",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-72", "Commercial lease protocol active for Punjab jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile73() {
        return new GstJurisdictionRule(
            "04", "Chandigarh", "CH",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-73", "Commercial lease protocol active for Chandigarh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile74() {
        return new GstJurisdictionRule(
            "05", "Uttarakhand", "UK",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-74", "Commercial lease protocol active for Uttarakhand jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile75() {
        return new GstJurisdictionRule(
            "06", "Haryana", "HR",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-75", "Commercial lease protocol active for Haryana jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile76() {
        return new GstJurisdictionRule(
            "07", "Delhi", "DL",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-76", "Commercial lease protocol active for Delhi jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile77() {
        return new GstJurisdictionRule(
            "08", "Rajasthan", "RJ",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-77", "Commercial lease protocol active for Rajasthan jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile78() {
        return new GstJurisdictionRule(
            "09", "Uttar Pradesh", "UP",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-78", "Commercial lease protocol active for Uttar Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile79() {
        return new GstJurisdictionRule(
            "10", "Bihar", "BR",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-79", "Commercial lease protocol active for Bihar jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile80() {
        return new GstJurisdictionRule(
            "11", "Sikkim", "SK",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-80", "Commercial lease protocol active for Sikkim jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile81() {
        return new GstJurisdictionRule(
            "12", "Arunachal Pradesh", "AR",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-81", "Commercial lease protocol active for Arunachal Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile82() {
        return new GstJurisdictionRule(
            "13", "Nagaland", "NL",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-82", "Commercial lease protocol active for Nagaland jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile83() {
        return new GstJurisdictionRule(
            "14", "Manipur", "MN",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-83", "Commercial lease protocol active for Manipur jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile84() {
        return new GstJurisdictionRule(
            "15", "Mizoram", "MZ",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-84", "Commercial lease protocol active for Mizoram jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile85() {
        return new GstJurisdictionRule(
            "16", "Tripura", "TR",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-85", "Commercial lease protocol active for Tripura jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile86() {
        return new GstJurisdictionRule(
            "17", "Meghalaya", "ML",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-86", "Commercial lease protocol active for Meghalaya jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile87() {
        return new GstJurisdictionRule(
            "18", "Assam", "AS",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-87", "Commercial lease protocol active for Assam jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile88() {
        return new GstJurisdictionRule(
            "19", "West Bengal", "WB",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-88", "Commercial lease protocol active for West Bengal jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile89() {
        return new GstJurisdictionRule(
            "20", "Jharkhand", "JH",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-89", "Commercial lease protocol active for Jharkhand jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile90() {
        return new GstJurisdictionRule(
            "21", "Odisha", "OD",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-90", "Commercial lease protocol active for Odisha jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile91() {
        return new GstJurisdictionRule(
            "22", "Chhattisgarh", "CG",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-91", "Commercial lease protocol active for Chhattisgarh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile92() {
        return new GstJurisdictionRule(
            "23", "Madhya Pradesh", "MP",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-92", "Commercial lease protocol active for Madhya Pradesh jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile93() {
        return new GstJurisdictionRule(
            "24", "Gujarat", "GJ",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-93", "Commercial lease protocol active for Gujarat jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile94() {
        return new GstJurisdictionRule(
            "26", "Dadra and Nagar Haveli and Daman and Diu", "DD",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-94", "Commercial lease protocol active for Dadra and Nagar Haveli and Daman and Diu jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile95() {
        return new GstJurisdictionRule(
            "27", "Maharashtra", "MH",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-95", "Commercial lease protocol active for Maharashtra jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile96() {
        return new GstJurisdictionRule(
            "29", "Karnataka", "KA",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-96", "Commercial lease protocol active for Karnataka jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile97() {
        return new GstJurisdictionRule(
            "30", "Goa", "GA",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-97", "Commercial lease protocol active for Goa jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile98() {
        return new GstJurisdictionRule(
            "31", "Lakshadweep", "LD",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-98", "Commercial lease protocol active for Lakshadweep jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile99() {
        return new GstJurisdictionRule(
            "32", "Kerala", "KL",
            False, 0.09, 0.09, 0.18,
            "SAC-9973-99", "Commercial lease protocol active for Kerala jurisdiction."
        );
    }

    public static GstJurisdictionRule getRuleProfile100() {
        return new GstJurisdictionRule(
            "33", "Tamil Nadu", "TN",
            True, 0.09, 0.09, 0.18,
            "SAC-9973-100", "Commercial lease protocol active for Tamil Nadu jurisdiction."
        );
    }

}
