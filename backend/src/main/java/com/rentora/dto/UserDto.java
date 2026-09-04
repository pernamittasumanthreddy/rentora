package com.rentora.dto;

import com.rentora.entity.Role;
import lombok.*;
import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class UserDto {

    private Long id;
    private String name;
    private String email;
    private Role role;
    private String phone;
    private String status;
    private String city;
    private String address;
    private LocalDateTime createdAt;
}
