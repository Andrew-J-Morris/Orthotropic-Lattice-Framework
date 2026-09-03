#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

// ============================================================================
// COMPONENT 1: HARDWARE-LEVEL INTEGER SQUARE ROOT
// Bypasses the FPU entirely. Runs strictly on ALU bitwise shifts.
// ============================================================================
uint64_t pure_isqrt(uint64_t value) {
	uint64_t res = 0;
	uint64_t bit = 1ULL << 62; // Top usable bit for 64-bit unsigned systems

	while (bit > value) {
		bit >>= 2;
	}

	while (bit != 0) {
		if (value >= res + bit) {
			value -= res + bit;
			res = (res >> 1) + bit;
		}
		else {
			res >>= 1;
		}
		bit >>= 2;
	}
	return res;
}

// ============================================================================
// COMPONENT 2: TRADITIONAL BRUTE-FORCE SWEEPER - O(r^3)
// Evaluates exact orthotropic constraints using pure integer math.
// ============================================================================
long long traditional_pure_integer_ellipsoid(long long r) {
	long long count = 0;
	long long A = 4 * r - 1;
	long long B = 4 * r + 1;
	long long AB_sq = (A * B) * (A * B);

	long long max_z = B / 2;

	for (long long z = -max_z; z <= max_z; ++z) {
		long long z_term = (2 * z * A) * (2 * z * A);
		for (long long y = -max_z; y <= max_z; ++y) {
			long long y_term = (2 * y * A) * (2 * y * A);
			for (long long x = -max_z; x <= max_z; ++x) {
				long long x_term = (2 * x * B) * (2 * x * B);

				if (x_term + y_term + z_term <= AB_sq) {
					count++;
				}
			}
		}
	}
	return count;
}

// ============================================================================
// COMPONENT 3: ROW-COLLAPSE ARCHITECTURE - O(r^2)
// Exact C++ structural mirror of the engine published in this paper.
// ============================================================================
long long discrete_pi_3d(long long r) {
	long long A = 4 * r - 1;
	long long B = 4 * r + 1;
	long long AB_sq = (A * B) * (A * B);
	long long total_lattice_points = 0;
	long long max_z = B / 2;

	for (long long z = -max_z; z <= max_z; ++z) {
		long long z_term = (2 * z * A) * (2 * z * A);
		long long rem_z0 = AB_sq - z_term;
		if (rem_z0 < 0) continue;

		long long max_x_y0 = pure_isqrt(rem_z0) / (2 * B);
		long long planar_lattice_count = (2 * max_x_y0) + 1;

		long long max_y = B / 2;
		long long count_y = 0;
		for (long long y = 1; y <= max_y; ++y) {
			long long y_term = (2 * y * A) * (2 * y * A);
			long long rem = AB_sq - y_term - z_term;
			if (rem >= 0) {
				long long max_x = pure_isqrt(rem) / (2 * B);
				count_y += (2 * max_x) + 1;
			}
		}
		planar_lattice_count += 2 * count_y;
		total_lattice_points += planar_lattice_count;
	}
	return total_lattice_points;
}

// ============================================================================
// MASTER EXECUTION COORDINATOR
// ============================================================================
int main() {
	// Radius value set to 2000 for massive volumetric profiling
	long long r = 2000;

	cout << "Starting Comprehensive FPU-Free Benchmark (r = " << r << ")..." << endl;
	cout << "--------------------------------------------------------" << endl;

	// --- Execution 1: Traditional Brute-Force ---
	auto start_trad = high_resolution_clock::now();
	long long trad_points = traditional_pure_integer_ellipsoid(r);
	auto stop_trad = high_resolution_clock::now();
	auto duration_trad = duration_cast<milliseconds>(stop_trad - start_trad);

	cout << "Traditional Pure Integer O(r^3) Sweeper:" << endl;
	cout << "Lattice Points : " << trad_points << endl;
	cout << "Clock Time     : " << duration_trad.count() << " ms" << endl << endl;

	// --- Execution 2: Row-Collapse Engine ---
	auto start_your = high_resolution_clock::now();
	long long your_points = discrete_pi_3d(r);
	auto stop_your = high_resolution_clock::now();
	auto duration_your = duration_cast<milliseconds>(stop_your - start_your);

	cout << "Row-Collapse O(r^2) Framework:" << endl;
	cout << "Lattice Points : " << your_points << endl;
	cout << "Clock Time     : " << duration_your.count() << " ms" << endl << endl;

	// --- Verification & Data Analytics ---
	if (trad_points == your_points) {
		cout << "VERIFICATION VERDICT: SUCCESS. Both methods evaluated identical domains." << endl;
		if (duration_your.count() > 0) {
			double multiplier = (double)duration_trad.count() / duration_your.count();
			cout << "RESULT: Your framework ran " << multiplier << "x faster." << endl;
		}
	}
	else {
		cout << "VERIFICATION VERDICT: FAILURE. Check mathematical limits." << endl;
	}

	return 0;
}