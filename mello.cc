#include "algos.h"
#include <iostream>

int main()
{
    for (const auto &e : melody("Eb", "natural minor", 16)) play_single_note(e, "play");
    return 0;
}
