#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <cmath>

namespace py = pybind11;

std::vector<int> getPrimes(int start, int end) {
    std::vector<int> primes;
    for (int i = start; i <= end; i++) {
        bool isPrime = true;
        for (int j = 2; j <= std::sqrt(i); j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime && i > 1) {
            primes.push_back(i);
        }
    }
    return primes;
}

PYBIND11_MODULE(primes, m) {
    m.doc() = "Python wrapper for the getPrimes C++ function";
    m.def("get_primes", &getPrimes, "Calculate prime numbers within a specific range");
}