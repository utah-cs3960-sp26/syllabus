#include <stdint.h>
#include <string.h>

#include "fpmul.h"

float fpmul(float a, float b) {
  uint32_t ai, bi;
  memcpy(&ai, &a, sizeof(ai));
  memcpy(&bi, &b, sizeof(bi));

  uint32_t as = ai >> 31;
  uint32_t ae = (ai >> 23) & 0xFF;
  uint32_t am = ai & 0x7FFFFF;

  uint32_t bs = bi >> 31;
  uint32_t be = (bi >> 23) & 0xFF;
  uint32_t bm = bi & 0x7FFFFF;

  uint32_t afm = (1u << 23) | am;
  uint32_t bfm = (1u << 23) | bm;

  uint64_t fullm = (uint64_t)afm * bfm;
  uint32_t needs_shift = (fullm >> 47) & 1;
  uint64_t shiftm = needs_shift ? fullm : (fullm << 1);
  int32_t e = (int32_t)ae + (int32_t)be - 127 + (int32_t)needs_shift;

  uint32_t ye, ym;
  if (e > 0) {
    // Normal-result path: round to a 24-bit significand (hidden bit + 23 frac).
    uint32_t sig24 = (uint32_t)(shiftm >> 24);
    uint32_t guard = (shiftm >> 23) & 1;
    uint32_t sticky = (shiftm & 0x7FFFFF) ? 1 : 0;
    uint32_t lsb = sig24 & 1;
    if (guard && (sticky || lsb))
      ++sig24;
    if (sig24 == 0x1000000) {
      sig24 = 0x800000;
      ++e;
    }
    ye = (uint32_t)e;
    ym = sig24 & 0x7FFFFF;
  } else {
    // Subnormal path: round directly into the subnormal fraction field.
    uint32_t sub;
    uint32_t round_up = 0;
    int32_t k = 25 - e;
    if (k <= 0) {
      sub = (uint32_t)shiftm;
    } else if (k >= 64) {
      sub = 0;
    } else {
      sub = (uint32_t)(shiftm >> k);
      uint32_t guard = (uint32_t)((shiftm >> (k - 1)) & 1);
      uint64_t low_mask = (k == 1) ? 0 : ((1ULL << (k - 1)) - 1);
      uint32_t sticky = (shiftm & low_mask) ? 1 : 0;
      uint32_t lsb = sub & 1;
      round_up = guard && (sticky || lsb);
    }
    sub += round_up;
    if (sub >= 0x800000) {
      // Rounded up into the minimum normal.
      ye = 1;
      ym = 0;
    } else {
      ye = 0;
      ym = sub & 0x7FFFFF;
    }
  }

  uint32_t ys = as ^ bs;

  uint32_t yi = (ys << 31) | (ye << 23) | (ym & 0x7FFFFF);

  float y;
  memcpy(&y, &yi, sizeof(y));
  return y;
}
