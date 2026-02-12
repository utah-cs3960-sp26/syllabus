#include <stdint.h>
#include <string.h>

#include "fpmul.h"

float fpmul(float a, float b) {
  uint32_t ai, bi;
  memcpy(&ai, &a, 4);
  memcpy(&bi, &b, 4);

  uint32_t as = ai >> 31;
  uint32_t ae = (ai >> 23) & 0xFF;
  uint32_t am = ai & 0x7FFFFF;

  uint32_t bs = bi >> 31;
  uint32_t be = (bi >> 23) & 0xFF;
  uint32_t bm = bi & 0x7FFFFF;

  uint32_t afm = (1 << 23) | am;
  uint32_t bfm = (1 << 23) | bm;

  uint64_t fullm = (uint64_t)afm * bfm;
  uint32_t needs_shift = (fullm >> 47) & 1;
  uint64_t shiftm = needs_shift ? fullm : (fullm << 1);

  uint32_t guard = (shiftm >> 23) & 1;
  uint32_t sticky = (shiftm & 0x7FFFFF) ? 1 : 0;
  uint32_t lsb = (shiftm >> 24) & 1;
  uint32_t round_up = (guard & sticky) | (guard & ~sticky & lsb);

  uint32_t ym = ((shiftm >> 24) & 0x7FFFFF) + round_up;
  uint32_t fulle = ae + be - 127 + needs_shift;
  uint32_t ye = fulle & 0xFF;

  uint32_t ys = as ^ bs;

  uint32_t yi = (ys << 31) | (ye << 23) | (ym & 0x7FFFFF);

  float y;
  memcpy(&y, &yi, 4);
  return y;
}
