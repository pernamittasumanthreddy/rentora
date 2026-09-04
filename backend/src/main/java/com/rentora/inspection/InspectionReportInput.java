package com.rentora.inspection;

import java.math.BigDecimal;
import java.util.List;

public class InspectionReportInput {
    private long rentalId;
    private String inspectorName;
    private boolean chassisClean = true;
    private String chassisNotes = "No scratches or dents";
    private BigDecimal chassisDamageFee = BigDecimal.ZERO;

    private boolean opticsFlawless = true;
    private String opticsNotes = "Optics & glass spotless";
    private BigDecimal opticsDamageFee = BigDecimal.ZERO;

    private boolean electronicsSound = true;
    private String electronicsNotes = "No error codes";
    private BigDecimal electronicsDamageFee = BigDecimal.ZERO;

    private boolean allAccessoriesPresent = true;
    private String accessoriesNotes = "All chargers and cases present";
    private BigDecimal accessoriesMissingFee = BigDecimal.ZERO;

    private boolean operationalPass = true;
    private String operationalNotes = "Field tested 100% operational";
    private BigDecimal operationalDamageFee = BigDecimal.ZERO;

    private List<String> photographicProofs;

    public long getRentalId() { return rentalId; }
    public void setRentalId(long rentalId) { this.rentalId = rentalId; }
    public String getInspectorName() { return inspectorName; }
    public void setInspectorName(String n) { this.inspectorName = n; }
    public boolean isChassisClean() { return chassisClean; }
    public void setChassisClean(boolean b) { this.chassisClean = b; }
    public String getChassisNotes() { return chassisNotes; }
    public void setChassisNotes(String s) { this.chassisNotes = s; }
    public BigDecimal getChassisDamageFee() { return chassisDamageFee; }
    public void setChassisDamageFee(BigDecimal f) { this.chassisDamageFee = f; }
    public boolean isOpticsFlawless() { return opticsFlawless; }
    public void setOpticsFlawless(boolean b) { this.opticsFlawless = b; }
    public String getOpticsNotes() { return opticsNotes; }
    public void setOpticsNotes(String s) { this.opticsNotes = s; }
    public BigDecimal getOpticsDamageFee() { return opticsDamageFee; }
    public void setOpticsDamageFee(BigDecimal f) { this.opticsDamageFee = f; }
    public boolean isElectronicsSound() { return electronicsSound; }
    public void setElectronicsSound(boolean b) { this.electronicsSound = b; }
    public String getElectronicsNotes() { return electronicsNotes; }
    public void setElectronicsNotes(String s) { this.electronicsNotes = s; }
    public BigDecimal getElectronicsDamageFee() { return electronicsDamageFee; }
    public void setElectronicsDamageFee(BigDecimal f) { this.electronicsDamageFee = f; }
    public boolean isAllAccessoriesPresent() { return allAccessoriesPresent; }
    public void setAllAccessoriesPresent(boolean b) { this.allAccessoriesPresent = b; }
    public String getAccessoriesNotes() { return accessoriesNotes; }
    public void setAccessoriesNotes(String s) { this.accessoriesNotes = s; }
    public BigDecimal getAccessoriesMissingFee() { return accessoriesMissingFee; }
    public void setAccessoriesMissingFee(BigDecimal f) { this.accessoriesMissingFee = f; }
    public boolean isOperationalPass() { return operationalPass; }
    public void setOperationalPass(boolean b) { this.operationalPass = b; }
    public String getOperationalNotes() { return operationalNotes; }
    public void setOperationalNotes(String s) { this.operationalNotes = s; }
    public BigDecimal getOperationalDamageFee() { return operationalDamageFee; }
    public void setOperationalDamageFee(BigDecimal f) { this.operationalDamageFee = f; }
    public List<String> getPhotographicProofs() { return photographicProofs; }
    public void setPhotographicProofs(List<String> proofs) { this.photographicProofs = proofs; }
}
