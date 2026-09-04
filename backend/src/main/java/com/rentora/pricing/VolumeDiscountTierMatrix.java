package com.rentora.pricing;

public class VolumeDiscountTierMatrix {

    public double getDiscountFactor(int days) {
        if (days >= 30) {
            return 0.30; // 30% monthly volume discount
        } else if (days >= 14) {
            return 0.20; // 20% bi-weekly volume discount
        } else if (days >= 7) {
            return 0.15; // 15% weekly discount
        } else if (days >= 3) {
            return 0.05; // 5% extended weekend discount
        }
        return 0.0;
    }
}
