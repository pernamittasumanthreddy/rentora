package com.rentora.iot;

public class CanBusDecodedSignal {
    private final String channelName;
    private final double decodedValue;
    private final String unitLabel;
    private final boolean withinTolerance;

    public CanBusDecodedSignal(String channelName, double decodedValue, String unitLabel, boolean withinTolerance) {
        this.channelName = channelName;
        this.decodedValue = decodedValue;
        this.unitLabel = unitLabel;
        this.withinTolerance = withinTolerance;
    }

    public String getChannelName() { return channelName; }
    public double getDecodedValue() { return decodedValue; }
    public String getUnitLabel() { return unitLabel; }
    public boolean isWithinTolerance() { return withinTolerance; }
}
