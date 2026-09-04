package com.rentora.pricing;

import java.time.DayOfWeek;
import java.time.LocalDate;

public class SurgeMultiplierCalculator {

    public double calculateCompositeSurge(LocalDate start, LocalDate end, double fleetUtilizationRatio) {
        double multiplier = 1.0;

        // Weekend surge factor
        long weekendDays = 0;
        long totalDays = java.time.temporal.ChronoUnit.DAYS.between(start, end);
        if (totalDays <= 0) totalDays = 1;

        LocalDate curr = start;
        while (!curr.isAfter(end)) {
            if (curr.getDayOfWeek() == DayOfWeek.SATURDAY || curr.getDayOfWeek() == DayOfWeek.SUNDAY) {
                weekendDays++;
            }
            curr = curr.plusDays(1);
        }

        double weekendRatio = (double) weekendDays / totalDays;
        if (weekendRatio > 0.4) {
            multiplier += 0.12; // 12% weekend demand surge
        }

        // Fleet utilization surge factor
        if (fleetUtilizationRatio >= 0.90) {
            multiplier += 0.25; // 25% peak capacity surge
        } else if (fleetUtilizationRatio >= 0.75) {
            multiplier += 0.10; // 10% high demand surge
        }

        return Math.round(multiplier * 100.0) / 100.0;
    }
}
