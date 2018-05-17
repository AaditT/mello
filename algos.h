/* Header file for Mello algorithms - Written by Srihari Nanniyur */
#ifndef __mello_algos_h__
#define __mello_algos_h__
#include <vector>
#include <string>

// Uses intervals to derive the notes of a given scale
class Generator {
public:
    Generator(std::string);
    std::vector<std::string> notes(std::vector<int>);
private:
    std::string key;
    std::vector<std::string> flat_octave = {
        "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"
    };
    std::vector<std::string> sharp_octave = {
        "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"
    };
    std::vector<std::string> octave;
};

void play_single_note(std::string, std::string);
std::vector<std::string> melody(std::string, std::string, int);

#endif
