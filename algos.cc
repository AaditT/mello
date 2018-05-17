#include <iostream>
#include <stdexcept>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <random>
#include "algos.h"

Generator::Generator(std::string k): key(k)
{
    if (k.size() < 1) throw std::runtime_error("Invalid key signature.");
    if (k.size() == 1) octave = sharp_octave;
    else if (k[1] == 'b') octave = flat_octave;
    else if (k[1] == '#') octave = sharp_octave;
    else throw std::runtime_error("Invalid key signature.");
}

std::vector<std::string> Generator::notes(std::vector<int> intervals)
{
    std::vector<std::string> order;
    std::vector<std::string> result;
    std::for_each(std::find(octave.begin(), octave.end(), key), octave.end(), [&order](std::string& s) {
        order.push_back(s);
    });
    std::for_each(octave.begin(), std::find(octave.begin(), octave.end(), key), [&order](std::string& s) {
        order.push_back(s);
    });
    auto it = order.begin();
    std::for_each(intervals.begin(), intervals.end(), [&order, &result, &it](int& n) {
        if (it >= order.end()) return;
        result.push_back(*it);
        it += n;
    });
    result.push_back(*it);
    return result;
}

void play_single_note(std::string s, std::string c)
{
    std::string cmd = "";
    cmd += c + " ";
    if (s == "A")
        cmd += " WAV/A.wav ";
    else if (s ==  "A#" || s == "Bb")
        cmd += " WAV/Bflat.wav ";
    else if (s ==  "B")
        cmd += " WAV/B.wav ";
    else if (s == "B#" || s == "C")
        cmd += " WAV/C.wav ";
    else if (s == "C#" || s == "Db")
        cmd += " WAV/Csharp.wav ";
    else if (s == "D")
        cmd += " WAV/D.wav ";
    else if (s == "D#" || s == "Eb")
        cmd += " WAV/Eflat.wav ";
    else if (s == "E")
        cmd += " WAV/E.wav ";
    else if (s == "E#" || s ==  "F")
        cmd += " WAV/F.wav ";
    else if (s ==  "F#" || s == "Gb")
        cmd += " WAV/Fsharp.wav ";
    else if (s == "G")
        cmd += " WAV/G.wav ";
    else if (s == "G#" || s == "Ab")
        cmd += " WAV/Gsharp.wav ";
    std::cout << cmd << std::endl;
    std::system(cmd.c_str());
}

std::vector<std::string> melody(std::string key, std::string scale, int num)
{
    Generator gen(key);
    std::vector<std::string> notes, result;
    int i, index;
    if      (scale == "whole tone")     notes = gen.notes({2, 2, 2, 2, 2});
    else if (scale == "natural major")  notes = gen.notes({2, 2, 1, 2, 2, 2});
    else if (scale == "natural minor")  notes = gen.notes({2, 1, 2, 2, 1, 2});
    else if (scale == "harmonic minor") notes = gen.notes({2, 1, 2, 2, 1, 3});
    else throw std::runtime_error("Invalid key signature.");
    for (i = 0; i < num; i++) {
        std::srand(std::time(nullptr));
        std::random_shuffle(notes.begin(), notes.end());
        result.push_back(notes[(int) notes.size() / 2]);
    }
    return result;
}
