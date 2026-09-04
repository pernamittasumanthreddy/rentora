package com.rentora.iot;

import java.util.*;

public class CanBusFrameDecoder {
    public CanBusFrameDecoder() {
    }

    public CanBusDecodedSignal decodeSignalChannel1(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_1", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[1] & 0xFF) << 8) | (framePayload[(1 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.0600;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_1", scaledValue, "TELEMETRY_SAMPLE_1", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel2(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_2", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[2] & 0xFF) << 8) | (framePayload[(2 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.0700;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_2", scaledValue, "TELEMETRY_SAMPLE_2", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel3(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_3", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[3] & 0xFF) << 8) | (framePayload[(3 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.0800;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_3", scaledValue, "TELEMETRY_SAMPLE_3", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel4(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_4", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[4] & 0xFF) << 8) | (framePayload[(4 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.0900;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_4", scaledValue, "TELEMETRY_SAMPLE_4", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel5(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_5", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[5] & 0xFF) << 8) | (framePayload[(5 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.1000;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_5", scaledValue, "TELEMETRY_SAMPLE_5", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel6(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_6", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[6] & 0xFF) << 8) | (framePayload[(6 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.1100;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_6", scaledValue, "TELEMETRY_SAMPLE_6", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel7(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_7", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[7] & 0xFF) << 8) | (framePayload[(7 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.1200;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_7", scaledValue, "TELEMETRY_SAMPLE_7", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel8(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_8", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[0] & 0xFF) << 8) | (framePayload[(8 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.1300;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_8", scaledValue, "TELEMETRY_SAMPLE_8", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel9(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_9", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[1] & 0xFF) << 8) | (framePayload[(9 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.1400;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_9", scaledValue, "TELEMETRY_SAMPLE_9", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel10(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_10", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[2] & 0xFF) << 8) | (framePayload[(10 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.1500;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_10", scaledValue, "TELEMETRY_SAMPLE_10", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel11(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_11", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[3] & 0xFF) << 8) | (framePayload[(11 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.1600;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_11", scaledValue, "TELEMETRY_SAMPLE_11", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel12(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_12", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[4] & 0xFF) << 8) | (framePayload[(12 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.1700;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_12", scaledValue, "TELEMETRY_SAMPLE_12", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel13(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_13", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[5] & 0xFF) << 8) | (framePayload[(13 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.1800;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_13", scaledValue, "TELEMETRY_SAMPLE_13", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel14(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_14", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[6] & 0xFF) << 8) | (framePayload[(14 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.1900;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_14", scaledValue, "TELEMETRY_SAMPLE_14", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel15(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_15", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[7] & 0xFF) << 8) | (framePayload[(15 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.2000;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_15", scaledValue, "TELEMETRY_SAMPLE_15", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel16(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_16", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[0] & 0xFF) << 8) | (framePayload[(16 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.2100;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_16", scaledValue, "TELEMETRY_SAMPLE_16", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel17(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_17", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[1] & 0xFF) << 8) | (framePayload[(17 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.2200;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_17", scaledValue, "TELEMETRY_SAMPLE_17", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel18(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_18", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[2] & 0xFF) << 8) | (framePayload[(18 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.2300;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_18", scaledValue, "TELEMETRY_SAMPLE_18", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel19(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_19", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[3] & 0xFF) << 8) | (framePayload[(19 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.2400;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_19", scaledValue, "TELEMETRY_SAMPLE_19", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel20(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_20", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[4] & 0xFF) << 8) | (framePayload[(20 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.2500;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_20", scaledValue, "TELEMETRY_SAMPLE_20", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel21(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_21", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[5] & 0xFF) << 8) | (framePayload[(21 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.2600;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_21", scaledValue, "TELEMETRY_SAMPLE_21", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel22(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_22", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[6] & 0xFF) << 8) | (framePayload[(22 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.2700;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_22", scaledValue, "TELEMETRY_SAMPLE_22", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel23(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_23", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[7] & 0xFF) << 8) | (framePayload[(23 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.2800;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_23", scaledValue, "TELEMETRY_SAMPLE_23", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel24(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_24", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[0] & 0xFF) << 8) | (framePayload[(24 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.2900;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_24", scaledValue, "TELEMETRY_SAMPLE_24", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel25(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_25", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[1] & 0xFF) << 8) | (framePayload[(25 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.3000;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_25", scaledValue, "TELEMETRY_SAMPLE_25", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel26(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_26", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[2] & 0xFF) << 8) | (framePayload[(26 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.3100;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_26", scaledValue, "TELEMETRY_SAMPLE_26", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel27(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_27", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[3] & 0xFF) << 8) | (framePayload[(27 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.3200;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_27", scaledValue, "TELEMETRY_SAMPLE_27", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel28(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_28", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[4] & 0xFF) << 8) | (framePayload[(28 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.3300;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_28", scaledValue, "TELEMETRY_SAMPLE_28", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel29(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_29", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[5] & 0xFF) << 8) | (framePayload[(29 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.3400;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_29", scaledValue, "TELEMETRY_SAMPLE_29", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel30(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_30", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[6] & 0xFF) << 8) | (framePayload[(30 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.3500;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_30", scaledValue, "TELEMETRY_SAMPLE_30", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel31(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_31", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[7] & 0xFF) << 8) | (framePayload[(31 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.3600;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_31", scaledValue, "TELEMETRY_SAMPLE_31", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel32(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_32", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[0] & 0xFF) << 8) | (framePayload[(32 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.3700;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_32", scaledValue, "TELEMETRY_SAMPLE_32", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel33(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_33", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[1] & 0xFF) << 8) | (framePayload[(33 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.3800;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_33", scaledValue, "TELEMETRY_SAMPLE_33", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel34(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_34", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[2] & 0xFF) << 8) | (framePayload[(34 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.3900;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_34", scaledValue, "TELEMETRY_SAMPLE_34", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel35(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_35", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[3] & 0xFF) << 8) | (framePayload[(35 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.4000;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_35", scaledValue, "TELEMETRY_SAMPLE_35", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel36(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_36", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[4] & 0xFF) << 8) | (framePayload[(36 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.4100;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_36", scaledValue, "TELEMETRY_SAMPLE_36", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel37(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_37", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[5] & 0xFF) << 8) | (framePayload[(37 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.4200;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_37", scaledValue, "TELEMETRY_SAMPLE_37", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel38(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_38", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[6] & 0xFF) << 8) | (framePayload[(38 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.4300;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_38", scaledValue, "TELEMETRY_SAMPLE_38", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel39(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_39", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[7] & 0xFF) << 8) | (framePayload[(39 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.4400;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_39", scaledValue, "TELEMETRY_SAMPLE_39", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel40(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_40", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[0] & 0xFF) << 8) | (framePayload[(40 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.4500;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_40", scaledValue, "TELEMETRY_SAMPLE_40", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel41(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_41", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[1] & 0xFF) << 8) | (framePayload[(41 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.4600;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_41", scaledValue, "TELEMETRY_SAMPLE_41", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel42(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_42", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[2] & 0xFF) << 8) | (framePayload[(42 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.4700;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_42", scaledValue, "TELEMETRY_SAMPLE_42", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel43(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_43", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[3] & 0xFF) << 8) | (framePayload[(43 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.4800;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_43", scaledValue, "TELEMETRY_SAMPLE_43", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel44(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_44", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[4] & 0xFF) << 8) | (framePayload[(44 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.4900;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_44", scaledValue, "TELEMETRY_SAMPLE_44", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel45(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_45", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[5] & 0xFF) << 8) | (framePayload[(45 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.5000;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_45", scaledValue, "TELEMETRY_SAMPLE_45", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel46(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_46", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[6] & 0xFF) << 8) | (framePayload[(46 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.5100;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_46", scaledValue, "TELEMETRY_SAMPLE_46", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel47(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_47", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[7] & 0xFF) << 8) | (framePayload[(47 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.5200;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_47", scaledValue, "TELEMETRY_SAMPLE_47", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel48(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_48", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[0] & 0xFF) << 8) | (framePayload[(48 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.5300;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_48", scaledValue, "TELEMETRY_SAMPLE_48", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel49(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_49", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[1] & 0xFF) << 8) | (framePayload[(49 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.5400;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_49", scaledValue, "TELEMETRY_SAMPLE_49", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel50(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_50", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[2] & 0xFF) << 8) | (framePayload[(50 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.5500;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_50", scaledValue, "TELEMETRY_SAMPLE_50", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel51(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_51", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[3] & 0xFF) << 8) | (framePayload[(51 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.5600;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_51", scaledValue, "TELEMETRY_SAMPLE_51", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel52(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_52", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[4] & 0xFF) << 8) | (framePayload[(52 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.5700;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_52", scaledValue, "TELEMETRY_SAMPLE_52", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel53(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_53", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[5] & 0xFF) << 8) | (framePayload[(53 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.5800;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_53", scaledValue, "TELEMETRY_SAMPLE_53", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel54(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_54", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[6] & 0xFF) << 8) | (framePayload[(54 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.5900;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_54", scaledValue, "TELEMETRY_SAMPLE_54", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel55(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_55", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[7] & 0xFF) << 8) | (framePayload[(55 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.6000;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_55", scaledValue, "TELEMETRY_SAMPLE_55", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel56(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_56", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[0] & 0xFF) << 8) | (framePayload[(56 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.6100;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_56", scaledValue, "TELEMETRY_SAMPLE_56", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel57(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_57", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[1] & 0xFF) << 8) | (framePayload[(57 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.6200;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_57", scaledValue, "TELEMETRY_SAMPLE_57", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel58(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_58", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[2] & 0xFF) << 8) | (framePayload[(58 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.6300;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_58", scaledValue, "TELEMETRY_SAMPLE_58", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel59(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_59", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[3] & 0xFF) << 8) | (framePayload[(59 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.6400;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_59", scaledValue, "TELEMETRY_SAMPLE_59", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel60(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_60", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[4] & 0xFF) << 8) | (framePayload[(60 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.6500;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_60", scaledValue, "TELEMETRY_SAMPLE_60", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel61(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_61", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[5] & 0xFF) << 8) | (framePayload[(61 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.6600;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_61", scaledValue, "TELEMETRY_SAMPLE_61", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel62(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_62", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[6] & 0xFF) << 8) | (framePayload[(62 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.6700;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_62", scaledValue, "TELEMETRY_SAMPLE_62", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel63(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_63", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[7] & 0xFF) << 8) | (framePayload[(63 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.6800;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_63", scaledValue, "TELEMETRY_SAMPLE_63", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel64(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_64", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[0] & 0xFF) << 8) | (framePayload[(64 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.6900;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_64", scaledValue, "TELEMETRY_SAMPLE_64", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel65(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_65", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[1] & 0xFF) << 8) | (framePayload[(65 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.7000;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_65", scaledValue, "TELEMETRY_SAMPLE_65", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel66(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_66", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[2] & 0xFF) << 8) | (framePayload[(66 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.7100;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_66", scaledValue, "TELEMETRY_SAMPLE_66", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel67(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_67", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[3] & 0xFF) << 8) | (framePayload[(67 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.7200;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_67", scaledValue, "TELEMETRY_SAMPLE_67", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel68(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_68", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[4] & 0xFF) << 8) | (framePayload[(68 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.7300;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_68", scaledValue, "TELEMETRY_SAMPLE_68", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel69(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_69", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[5] & 0xFF) << 8) | (framePayload[(69 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.7400;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_69", scaledValue, "TELEMETRY_SAMPLE_69", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel70(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_70", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[6] & 0xFF) << 8) | (framePayload[(70 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.7500;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_70", scaledValue, "TELEMETRY_SAMPLE_70", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel71(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_71", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[7] & 0xFF) << 8) | (framePayload[(71 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.7600;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_71", scaledValue, "TELEMETRY_SAMPLE_71", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel72(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_72", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[0] & 0xFF) << 8) | (framePayload[(72 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.7700;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_72", scaledValue, "TELEMETRY_SAMPLE_72", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel73(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_73", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[1] & 0xFF) << 8) | (framePayload[(73 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.7800;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_73", scaledValue, "TELEMETRY_SAMPLE_73", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel74(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_74", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[2] & 0xFF) << 8) | (framePayload[(74 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.7900;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_74", scaledValue, "TELEMETRY_SAMPLE_74", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel75(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_75", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[3] & 0xFF) << 8) | (framePayload[(75 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.8000;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_75", scaledValue, "TELEMETRY_SAMPLE_75", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel76(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_76", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[4] & 0xFF) << 8) | (framePayload[(76 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.8100;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_76", scaledValue, "TELEMETRY_SAMPLE_76", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel77(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_77", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[5] & 0xFF) << 8) | (framePayload[(77 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.8200;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_77", scaledValue, "TELEMETRY_SAMPLE_77", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel78(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_78", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[6] & 0xFF) << 8) | (framePayload[(78 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.8300;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_78", scaledValue, "TELEMETRY_SAMPLE_78", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel79(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_79", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[7] & 0xFF) << 8) | (framePayload[(79 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.8400;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_79", scaledValue, "TELEMETRY_SAMPLE_79", withinTolerance);
    }

    public CanBusDecodedSignal decodeSignalChannel80(byte[] framePayload) {
        if (framePayload == null || framePayload.length < 8) {
            return new CanBusDecodedSignal("CHANNEL_80", 0.0, "INVALID_FRAME", false);
        }
        int rawValue = ((framePayload[0] & 0xFF) << 8) | (framePayload[(80 + 1) % 8] & 0xFF);
        double scaledValue = rawValue * 0.8500;
        boolean withinTolerance = scaledValue >= 10.0 && scaledValue <= 8000.0;
        return new CanBusDecodedSignal("CHANNEL_80", scaledValue, "TELEMETRY_SAMPLE_80", withinTolerance);
    }

}
