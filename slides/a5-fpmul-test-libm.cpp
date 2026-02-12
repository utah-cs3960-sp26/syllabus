#include <bit>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <random>

#include "fpmul.h"

using namespace std;

int main() {
  constexpr uint64_t N = 1000000000ULL;
  random_device r;
  mt19937 rng(r());

  uint64_t errors = 0;
  uint64_t eligible = 0;

  for (uint64_t i = 0; i < N; ++i) {
    const uint32_t ai = rng();
    const uint32_t bi = rng();

    const float a = bit_cast<float>(ai);
    const float b = bit_cast<float>(bi);

    if (!isnormal(a) || !isnormal(b)) {
      continue;
    }

    const float hw = a * b;
    if (!isnormal(hw)) {
      continue;
    }

    ++eligible;

    const float sw = fpmul(a, b);
    if (bit_cast<uint32_t>(sw) != bit_cast<uint32_t>(hw)) {
      ++errors;
      printf("oops: for %a * %a we expected %a but got %a\n",
	     a, b, hw, sw);
    }
  }

  printf("N=%llu eligible=%llu errors=%llu\n",
              static_cast<unsigned long long>(N),
              static_cast<unsigned long long>(eligible),
              static_cast<unsigned long long>(errors));
  return 0;
}
