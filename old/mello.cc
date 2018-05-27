/* mello.cc - mello main file.
 * Written by Srihari Nanniyur.
 */
#include "algos.h"
#include <iostream>

int main()
{
    for (const auto &e : melody("C", "pentatonic major", 16)) play_single_note(e, "play");
    return 0;
}
