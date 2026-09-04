import React, { useEffect, useRef, useState } from 'react';
import { motion } from 'framer-motion';
import { Sparkles, RefreshCw } from 'lucide-react';

export default function CinematicLogoReveal({ onAnimationComplete }) {
  const canvasRef = useRef(null);
  const [phase, setPhase] = useState('converging'); // 'converging', 'locked', 'sheen'
  const [blurLevel, setBlurLevel] = useState(14);
  const [logoOpacity, setLogoOpacity] = useState(0);
  const [showSheen, setShowSheen] = useState(false);
  const [replayKey, setReplayKey] = useState(0);

  // Trigger convergence animation
  const triggerReveal = () => {
    setPhase('converging');
    setBlurLevel(14);
    setLogoOpacity(0);
    setShowSheen(false);
    setReplayKey((prev) => prev + 1);
  };

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let animationFrameId;

    // Handle high DPI
    const resizeCanvas = () => {
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = rect.width * dpr;
      canvas.height = rect.height * dpr;
      ctx.scale(dpr, dpr);
    };
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    const width = canvas.getBoundingClientRect().width;
    const height = canvas.getBoundingClientRect().height;

    // Target letter coordinate clusters for R-E-N-T-O-R-A across the canvas
    const centerX = width / 2;
    const centerY = height / 2;
    const letterSpacing = Math.min(width * 0.11, 72);
    const startX = centerX - (letterSpacing * 3);

    // Letter target anchors for 7 letters: R E N T O R A
    const targetPoints = [];
    const letters = ['R', 'E', 'N', 'T', 'O', 'R', 'A'];
    letters.forEach((char, idx) => {
      const lx = startX + idx * letterSpacing;
      // Define 7-8 points per letter shape
      for (let i = 0; i < 8; i++) {
        const angle = (i / 8) * Math.PI * 2;
        const radius = 18 + (i % 3) * 6;
        targetPoints.push({
          x: lx + Math.cos(angle) * radius,
          y: centerY + Math.sin(angle) * radius,
          char,
        });
      }
    });

    // Initialize organic particles
    const particleCount = targetPoints.length + 24; // converged + floating ambient
    const particles = [];

    for (let i = 0; i < particleCount; i++) {
      const hasTarget = i < targetPoints.length;
      const target = hasTarget ? targetPoints[i] : null;

      // Start from scattered perimeter or outer areas
      const startAngle = Math.random() * Math.PI * 2;
      const startDist = Math.random() * (width * 0.45) + 120;

      particles.push({
        x: centerX + Math.cos(startAngle) * startDist,
        y: centerY + Math.sin(startAngle) * startDist,
        vx: (Math.random() - 0.5) * 1.5,
        vy: (Math.random() - 0.5) * 1.5,
        targetX: target ? target.x : null,
        targetY: target ? target.y : null,
        radius: Math.random() * 2.2 + 1.2,
        color: i % 3 === 0 ? '#C99700' : i % 3 === 1 ? '#2D6A4F' : '#52B788',
        alpha: Math.random() * 0.6 + 0.4,
        settled: false,
      });
    }

    let startTime = performance.now();
    let lineOpacity = 0.45;

    const render = (now) => {
      const elapsed = (now - startTime) / 1000;
      ctx.clearRect(0, 0, width, height);

      // Convergence progress from 0.0 to 1.0 over 1.8 seconds
      const progress = Math.min(elapsed / 1.8, 1);
      const ease = 1 - Math.pow(1 - progress, 3); // cubic easeOut

      // Fade connecting lines as convergence nears completion
      if (progress > 0.4) {
        lineOpacity = Math.max(0, 0.45 * (1 - (progress - 0.4) / 0.6));
      }

      // Draw faint constellation network lines between nearby particles
      if (lineOpacity > 0.01) {
        ctx.lineWidth = 0.75;
        for (let i = 0; i < particles.length; i++) {
          for (let j = i + 1; j < particles.length; j++) {
            const dx = particles[i].x - particles[j].x;
            const dy = particles[i].y - particles[j].y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 65) {
              const alpha = (1 - dist / 65) * lineOpacity;
              ctx.strokeStyle = `rgba(45, 106, 79, ${alpha})`;
              ctx.beginPath();
              ctx.moveTo(particles[i].x, particles[i].y);
              ctx.lineTo(particles[j].x, particles[j].y);
              ctx.stroke();
            }
          }
        }
      }

      // Update and draw particles
      particles.forEach((p) => {
        if (p.targetX !== null) {
          // Organic homing interpolation
          const curTargetX = p.targetX;
          const curTargetY = p.targetY;
          p.x += (curTargetX - p.x) * (0.05 + ease * 0.05);
          p.y += (curTargetY - p.y) * (0.05 + ease * 0.05);

          // Add slight organic harmonic vibration
          p.x += Math.sin(now * 0.003 + p.y) * 0.35;
          p.y += Math.cos(now * 0.003 + p.x) * 0.35;
        } else {
          // Floating background ambient particle
          p.x += p.vx;
          p.y += p.vy;
          if (p.x < 0 || p.x > width) p.vx *= -1;
          if (p.y < 0 || p.y > height) p.vy *= -1;
        }

        // Draw glowing particle
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.globalAlpha = p.alpha;
        ctx.shadowBlur = 6;
        ctx.shadowColor = p.color;
        ctx.fill();
        ctx.shadowBlur = 0;
      });

      ctx.globalAlpha = 1;

      // Sequential state triggers
      if (progress >= 0.75 && blurLevel > 0) {
        const remaining = (1 - progress) / 0.25;
        setBlurLevel(Math.max(0, 14 * remaining));
        setLogoOpacity(Math.min(1, (progress - 0.75) / 0.25));
      }

      if (progress >= 1.0) {
        setPhase('locked');
        setBlurLevel(0);
        setLogoOpacity(1);
        setShowSheen(true);
        if (onAnimationComplete) {
          onAnimationComplete();
        }
      }

      animationFrameId = requestAnimationFrame(render);
    };

    animationFrameId = requestAnimationFrame(render);

    return () => {
      cancelAnimationFrame(animationFrameId);
      window.removeEventListener('resize', resizeCanvas);
    };
  }, [replayKey]);

  return (
    <div className="relative w-full py-10 flex flex-col items-center justify-center select-none overflow-hidden">
      {/* Canvas for dynamic particles & connecting network lines */}
      <canvas
        ref={canvasRef}
        className="absolute inset-0 w-full h-full pointer-events-none z-0"
        style={{ minHeight: '220px' }}
      />

      {/* Atmospheric Ambient Glow Behind Logo */}
      <div className="absolute w-72 h-36 bg-gradient-to-r from-hunter-600/20 via-gold-500/25 to-hunter-500/20 rounded-full blur-3xl pointer-events-none animate-pulse-subtle" />

      {/* The Revealed Brand Logo Container */}
      <div className="relative z-10 flex flex-col items-center justify-center">
        {/* Sub-Brand Monogram Badge */}
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.8, delay: 0.3 }}
          className="inline-flex items-center space-x-2 px-3.5 py-1 rounded-full bg-white/70 backdrop-blur-md border border-hunter-700/15 shadow-elevation-1 mb-3"
        >
          <span className="w-2 h-2 rounded-full bg-hunter-600 animate-ping" />
          <span className="text-[11px] font-semibold tracking-widest uppercase text-hunter-900">
            CINEMATIC REVEAL
          </span>
          <span className="text-bungalow-400">•</span>
          <span className="text-[11px] font-bold text-hunter-700">VERIFIED ESCROW FLEET</span>
        </motion.div>

        {/* Sharpening & Sheen-swept RENTORA Brand Wordmark */}
        <div
          className="relative px-6 py-2 transition-all duration-700"
          style={{
            filter: `blur(${blurLevel}px)`,
            opacity: logoOpacity,
            transform: `scale(${0.92 + (1 - blurLevel / 14) * 0.08})`,
          }}
        >
          <h1 className="text-5xl sm:text-7xl lg:text-8xl font-black font-display tracking-tight text-hunter-900 drop-shadow-sm flex items-center">
            <span className="bg-clip-text text-transparent bg-gradient-to-br from-hunter-950 via-hunter-800 to-hunter-700">
              RENT
            </span>
            <span className="text-gold-600 mx-0.5 font-light">·</span>
            <span className="bg-clip-text text-transparent bg-gradient-to-br from-hunter-800 via-hunter-700 to-hunter-600">
              ORA
            </span>
          </h1>

          {/* Luxury Sheen Light Sweep Reflection */}
          {showSheen && (
            <div className="absolute inset-0 pointer-events-none sheen-sweep" />
          )}
        </div>

        {/* Brand Tagline */}
        <motion.p
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: logoOpacity > 0.6 ? 1 : 0, y: logoOpacity > 0.6 ? 0 : 8 }}
          transition={{ duration: 0.5 }}
          className="mt-2 text-xs sm:text-sm font-semibold tracking-[0.25em] uppercase text-hunter-700/90 text-center"
        >
          Smart Product, Vehicle &amp; Bungalow Platform
        </motion.p>
      </div>

      {/* Subtle Replay Reveal Action Pill */}
      <button
        onClick={triggerReveal}
        type="button"
        title="Replay Logo Reveal Animation"
        className="absolute right-4 bottom-2 z-20 inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-full text-[11px] font-medium text-hunter-800/70 hover:text-hunter-950 bg-white/60 hover:bg-white/90 border border-bungalow-300/80 shadow-sm backdrop-blur-sm transition-all duration-200"
      >
        <RefreshCw className="w-3 h-3 text-hunter-600" />
        <span className="hidden sm:inline">Replay Reveal</span>
      </button>
    </div>
  );
}
