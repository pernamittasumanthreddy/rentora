package com.rentora.tax;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.UUID;

public class CommercialInvoiceGenerator {

    public CommercialInvoice generateInvoice(
            long rentalId,
            String customerName,
            String customerGstin,
            String vendorBusinessName,
            String vendorGstin,
            BigDecimal rentAmount,
            GstTaxBreakdown tax
    ) {
        String invoiceNumber = "INV-RENT-" + LocalDate.now().getYear() + "-" + (10000 + (rentalId % 90000));
        BigDecimal totalPayable = rentAmount.add(tax.getTotalTax());

        return new CommercialInvoice(
            invoiceNumber,
            rentalId,
            LocalDate.now(),
            customerName,
            customerGstin,
            vendorBusinessName,
            vendorGstin,
            rentAmount,
            tax.getCgst(),
            tax.getSgst(),
            tax.getIgst(),
            tax.getTotalTax(),
            totalPayable
        );
    }
}
