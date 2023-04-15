# Compilation instruction:
c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` primes.cpp -o primes`python3-config --extension-suffix`