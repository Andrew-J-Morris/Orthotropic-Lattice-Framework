# orthotropic parity and discrete pi

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22282210.svg)](https://doi.org/10.5281/zenodo.22282210)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Quickstart Compilation
Compile and run the C++ benchmark demonstrating the O(r^3) to O(r^2) volumetric collapse via 4r ± 1 orthotropic bounds:
```bash
g++ -O3 -std=c++20 O_r3_to_O_r2_benchmark.cpp -o benchmark && ./benchmark
```

**Discrete Geometry First: Collapsing High-Dimensional Lattice Enumeration from O(r^N) to Quasi-Quadratic O(r^2 log_2 N log r)**

For over two centuries, the standard approach to discrete lattice point enumeration has relied on continuous Euclidean tools—transcendental functions, Bessel expansions, modular forms, and floating-point approximations—projected onto integer grids[cite: 4, 15]. This approach frequently runs into boundary-vertex collisions, floating-point precision drift, and the classical exponential coordinate bottleneck[cite: 4, 17].

Instead of forcing continuous calculus onto discrete space, I developed an integer-native geometric framework that treats discrete grids on their own native algebraic terms[cite: 4, 15]. By recognizing that squared Euclidean distance is additively separable across orthogonal submanifolds, high-dimensional boundaries can be decoupled and evaluated via single-pass integer dot products and discrete cross-convolutions[cite: 8, 10].

The complete research suite consists of four preprints establishing the theoretical derivations, asymptotic complexity proofs, and hardware-native C++ reference implementations:

*   **Paper I: An Integer-Only Orthotropic Lattice Enumeration Framework and Asymptotic Convergence of Discrete Rational π**
    *   *Core Premise:* Couples orthotropic boundaries 4r ± 1 to construct Diophantine parity constraints that mathematically prohibit boundary-vertex collisions[cite: 6, 15].
    *   *Result:* Resolves boundary discrepancy and derives a deterministic, rational convergence envelope for discrete π_d ∈ ℚ[cite: 6, 15].
    *   *Zenodo DOI:* [10.5281/zenodo.22282210](https://doi.org/10.5281/zenodo.22282210)[cite: 4, 6] | *GitHub:* [Orthotropic-Lattice-Framework](https://github.com/Andrew-J-Morris/Orthotropic-Lattice-Framework)[cite: 6]

*   **Paper II: A Dimension-Paired Combinatorial Framework: Asymptotic O(r^2) Reduction and O(r^2 log_2 N log r) Generalized Convolution for High-Dimensional Discrete Lattice Enumeration**
    *   *Core Premise:* Decomposes 4D space as orthogonal planes (Z^4 ≅ Z^2 × Z^2), reducing 4-space enumeration from O(r^4) to a single-pass 1D dot product in strict O(r^2) without floating-point operations[cite: 5, 8].
    *   *Generalization:* Applies recursive bisection via Number Theoretic Transforms (NTT) in finite fields Z_p[t], collapsing N-dimensional ball enumeration to O(r^2 log_2 N log r)[cite: 5, 8].
    *   *Zenodo DOI:* [10.5281/zenodo.22509388](https://doi.org/10.5281/zenodo.22509388)[cite: 5] | *GitHub:* [dimension-paired-lattice-framework](https://github.com/Andrew-J-Morris/dimension-paired-lattice-framework)[cite: 5]

*   **Paper III: Hierarchical Dimension-Pairing: Hardware-Native O(r^2) Enumeration of 5D through 8D Spherical Lattices and High-Dimensional Capacity Limits**
    *   *Core Premise:* Neutralizes the historical odd-dimension class-number barrier for Z^5 and Z^7 by slicing 1D axial profiles against precomputed even-dimensional hyperdisk profiles[cite: 9, 10].
    *   *Empirical Scaling:* Verifies sequences against OEIS baselines (A000333–A000336), and benchmarks a 1024-dimensional R = 2896 hyperball (output = 831168560 (mod 998244353)) in 1561.833 ms on a single desktop core[cite: 9, 10].
    *   *Zenodo DOI:* [10.5281/zenodo.22691273](https://doi.org/10.5281/zenodo.22691273)[cite: 9] | *GitHub:* [Hierarchical-Dimension-Pairing-Framework](https://github.com/Andrew-J-Morris/Hierarchical-Dimension-Pairing-Framework)

*   **Paper IV: Parity-Filtered Bisection: Hardware-Native O(r^2) Enumeration of Optimal D_N Lattices**
    *   *Core Premise:* Extends the bisection architecture beyond primitive grids to dense, non-orthogonal kissing-number lattices[cite: 3, 14]. By redefining geometries as parity-constrained sublattices of Z^N (∑ x_i ≡ 0 (mod 2)), internal coordinate staggering is fully absorbed into pre-filtered arrays[cite: 3, 14].
    *   *Result:* Achieves hardware-native O(r^2) exact enumeration for Face-Centered Cubic (D_3), the 24-cell honeycomb (D_4), and the D_8 root lattice, verified bit-for-bit against OEIS A005875, A004011, and A004013[cite: 3].
    *   *Zenodo DOI:* [10.5281/zenodo.22824219](https://doi.org/10.5281/zenodo.22824219) | *GitHub:* [Parity-Filtered-Bisection-DN-Lattices](https://github.com/Andrew-J-Morris/Parity-Filtered-Bisection-DN-Lattices)

**The Empirical Validation**

The C++ implementations are designed as self-contained, reproducible test benches running exclusively on 64-bit integer ALUs with zero floating-point emulation:
*   Resolving 246+ million points in the 4D 24-cell honeycomb at R=100 in 2 ms on consumer hardware.
*   Pushing the finite-field Number Theoretic Transform (NTT) bisection tree to its theoretical single-prime 2-adic ceiling (R = 2896, transform size M = 2^23), evaluating a 1024-dimensional hyperball across an 8.38-million-element ring in 1,561 ms on a single desktop core.
*   Evaluating 7-dimensional bounding hyperballs from R = 0..5000, culminating in a bit-perfect 27-digit lattice point count, thereby extending OEIS A055413 from R = 0..500 to R = 0..5000.

All four preprints, source code, and benchmark suites are open-access. Feedback on the combinatorial proofs, algorithmic bounds, and hardware pipelining is welcome.

---

### The Discrete Lattice Research Suite
This repository is part of a 4-paper research program establishing hardware-native, integer-only lattice enumeration:

1. **[orthotropic-parity-and-discrete-pi](https://github.com/Andrew-J-Morris/orthotropic-parity-and-discrete-pi):** 3D row-collapse, 4r ± 1 parity bounds, and rational π_d ∈ ℚ convergence. [[Zenodo DOI: 10.5281/zenodo.22282210](https://doi.org/10.5281/zenodo.22282210)]
2. **[dimension-paired-cross-convolution](https://github.com/Andrew-J-Morris/dimension-paired-cross-convolution):** 4D orthogonal plane bisection (O(r^2)) and generalized NTT convolution (O(r^2 log_2 N log r)). [[Zenodo DOI: 10.5281/zenodo.22509388](https://doi.org/10.5281/zenodo.22509388)]
3. **[hierarchical-ntt-bisection](https://github.com/Andrew-J-Morris/hierarchical-ntt-bisection):** 5D–8D odd-dimension slicing, OEIS A000333–A000336 verification, and N=1024 NTT scaling. [[Zenodo DOI: 10.5281/zenodo.22691273](https://doi.org/10.5281/zenodo.22691273)]
4. **[parity-filtered-kissing-lattices](https://github.com/Andrew-J-Morris/parity-filtered-kissing-lattices):** Exact O(r^2) kissing-number root lattices (D_3 FCC, D_4 24-cell, and D_8). [[Zenodo DOI: 10.5281/zenodo.22824219](https://doi.org/10.5281/zenodo.22824219)]

---

## ⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details.
