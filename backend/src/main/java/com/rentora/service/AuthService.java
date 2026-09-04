package com.rentora.service;

import com.rentora.dto.AuthRequest;
import com.rentora.dto.AuthResponse;
import com.rentora.dto.RegisterRequest;
import com.rentora.entity.Role;
import com.rentora.entity.User;
import com.rentora.entity.Vendor;
import com.rentora.exception.BadRequestException;
import com.rentora.repository.UserRepository;
import com.rentora.repository.VendorRepository;
import com.rentora.security.JwtTokenProvider;
import lombok.RequiredArgsConstructor;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class AuthService {

    private final AuthenticationManager authenticationManager;
    private final UserRepository userRepository;
    private final VendorRepository vendorRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtTokenProvider tokenProvider;

    public AuthResponse login(AuthRequest authRequest) {
        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(authRequest.getEmail(), authRequest.getPassword())
        );

        SecurityContextHolder.getContext().setAuthentication(authentication);
        String jwt = tokenProvider.generateToken(authentication);

        User user = userRepository.findByEmail(authRequest.getEmail())
                .orElseThrow(() -> new BadRequestException("User not found"));

        String businessName = null;
        if (user.getRole() == Role.ROLE_VENDOR) {
            businessName = vendorRepository.findByUserId(user.getId())
                    .map(Vendor::getBusinessName)
                    .orElse(null);
        }

        return AuthResponse.builder()
                .token(jwt)
                .tokenType("Bearer")
                .userId(user.getId())
                .name(user.getName())
                .email(user.getEmail())
                .role(user.getRole().name())
                .businessName(businessName)
                .build();
    }

    @Transactional
    public AuthResponse register(RegisterRequest registerRequest) {
        if (userRepository.existsByEmail(registerRequest.getEmail())) {
            throw new BadRequestException("Email is already registered on Rentora!");
        }

        Role role = registerRequest.getRole() != null ? registerRequest.getRole() : Role.ROLE_CUSTOMER;

        User user = User.builder()
                .name(registerRequest.getName())
                .email(registerRequest.getEmail())
                .password(passwordEncoder.encode(registerRequest.getPassword()))
                .role(role)
                .phone(registerRequest.getPhone())
                .city(registerRequest.getCity())
                .status("ACTIVE")
                .build();

        User savedUser = userRepository.save(user);

        String businessName = null;
        if (role == Role.ROLE_VENDOR) {
            businessName = registerRequest.getBusinessName() != null ?
                    registerRequest.getBusinessName() : savedUser.getName() + " Fleet";

            Vendor vendor = Vendor.builder()
                    .user(savedUser)
                    .businessName(businessName)
                    .city(savedUser.getCity())
                    .rating(5.0)
                    .trustScore(95)
                    .build();

            vendorRepository.save(vendor);
        }

        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(registerRequest.getEmail(), registerRequest.getPassword())
        );

        String jwt = tokenProvider.generateToken(authentication);

        return AuthResponse.builder()
                .token(jwt)
                .tokenType("Bearer")
                .userId(savedUser.getId())
                .name(savedUser.getName())
                .email(savedUser.getEmail())
                .role(savedUser.getRole().name())
                .businessName(businessName)
                .build();
    }
}
