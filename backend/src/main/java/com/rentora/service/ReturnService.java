package com.rentora.service;

import com.rentora.dto.ReturnDto;
import com.rentora.entity.Rental;
import com.rentora.entity.RentalStatus;
import com.rentora.entity.ReturnRecord;
import com.rentora.entity.ReturnStatus;
import com.rentora.exception.ResourceNotFoundException;
import com.rentora.repository.RentalRepository;
import com.rentora.repository.ReturnRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class ReturnService {

    private final ReturnRepository returnRepository;
    private final RentalRepository rentalRepository;

    public List<ReturnDto> getAllReturns() {
        return returnRepository.findAll().stream()
                .map(this::mapToDto)
                .collect(Collectors.toList());
    }

    public ReturnDto getReturnById(Long id) {
        ReturnRecord record = returnRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("ReturnRecord", "id", id));
        return mapToDto(record);
    }

    @Transactional
    public ReturnDto initiateReturn(Long rentalId, String damageReport) {
        Rental rental = rentalRepository.findById(rentalId)
                .orElseThrow(() -> new ResourceNotFoundException("Rental", "id", rentalId));

        rental.setStatus(RentalStatus.RETURNED);
        rentalRepository.save(rental);

        ReturnRecord record = ReturnRecord.builder()
                .rental(rental)
                .status(ReturnStatus.PENDING)
                .damageReport(damageReport)
                .damageFee(BigDecimal.ZERO)
                .depositRefunded(BigDecimal.ZERO)
                .returnDate(LocalDate.now())
                .build();

        return mapToDto(returnRepository.save(record));
    }

    @Transactional
    public ReturnDto settleReturn(Long returnId, BigDecimal damageFee, String remarks) {
        ReturnRecord record = returnRepository.findById(returnId)
                .orElseThrow(() -> new ResourceNotFoundException("ReturnRecord", "id", returnId));

        Rental rental = record.getRental();
        BigDecimal heldDeposit = rental.getDeposit();
        BigDecimal fee = damageFee != null ? damageFee : BigDecimal.ZERO;
        BigDecimal refund = heldDeposit.subtract(fee).max(BigDecimal.ZERO);

        record.setDamageFee(fee);
        record.setDepositRefunded(refund);
        record.setStatus(ReturnStatus.SETTLED);
        if (remarks != null) {
            record.setDamageReport(remarks);
        }

        rental.setStatus(RentalStatus.COMPLETED);
        rentalRepository.save(rental);

        return mapToDto(returnRepository.save(record));
    }

    private ReturnDto mapToDto(ReturnRecord r) {
        return ReturnDto.builder()
                .id(r.getId())
                .rentalId(r.getRental().getId())
                .productName(r.getRental().getProduct().getName())
                .customerName(r.getRental().getCustomer().getName())
                .vendorName(r.getRental().getProduct().getVendor().getBusinessName())
                .status(r.getStatus())
                .damageReport(r.getDamageReport())
                .damageFee(r.getDamageFee())
                .depositRefunded(r.getDepositRefunded())
                .returnDate(r.getReturnDate())
                .build();
    }
}
