package com.rentora.fleet;

public class DiagnosticTroubleCode {
    private final String code;
    private final String description;
    private final String severity;
    private final String ecuNode;
    private final String remediation;

    public DiagnosticTroubleCode(String code, String description, String severity, String ecuNode, String remediation) {
        this.code = code;
        this.description = description;
        this.severity = severity;
        this.ecuNode = ecuNode;
        this.remediation = remediation;
    }

    public String getCode() { return code; }
    public String getDescription() { return description; }
    public String getSeverity() { return severity; }
    public String getEcuNode() { return ecuNode; }
    public String getRemediation() { return remediation; }
}
