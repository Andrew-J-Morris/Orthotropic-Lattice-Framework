# Orthotropic Lattice Enumeration Framework

Official source code and benchmark scripts accompanying the research paper:

> **Morris, A. J. (2026).** *An Integer-Only Orthotropic Lattice Enumeration Framework and Asymptotic Convergence of Discrete Rational π.* Zenodo. [DOI: 10.5281/zenodo.22282210](https://doi.org/10.5281/zenodo.22282210)

## Overview
This repository contains the pure integer-ALU Python and C++ implementations demonstrating $\mathcal{O}(r^2)$ spatial enumeration and scale-dependent rational fraction convergence for discrete geometry.

## Contents
- `2D_discrete_pi.py`: Two-dimensional discrete $\pi$ convergence and row-collapse logic.
- `3D_discrete_pi.py`: Three-dimensional volume evaluation via integer square roots.
- `complexity_reduction_benchmark.cpp`: Hardware benchmarking script evaluating execution time scaling from $\mathcal{O}(r^3)$ down to $\mathcal{O}(r^2)$.
