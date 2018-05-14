/* mello.cc - Mello application for melody creation.
 * Written by Srihari Nanniyur. */
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <ctime>

static std::vector<std::string> accidentals;
static std::vector<std::string> flats( {"Bb", "Eb", "Ab", "Db", "Gb", "Cb", "Fb"} );
static std::vector<std::string> sharps( {"F#", "C#", "G#", "D#", "A#", "E#", "B#"} );
static std::vector<std::string> reg_notes( {"F", "C", "G", "D", "A", "E", "B"} );

void fill_sharps(int count)
{
    int i = 0;
    for (auto it = sharps.begin(); it != sharps.end() && i < count; it++, i++) {
        accidentals.push_back(*it);
        std::cout << *it << std::endl;
    }
}

void fill_flats(int count)
{
    int i = 0;
    for (auto it = flats.begin(); it != flats.end() && i < count; it++, i++) {
        accidentals.push_back(*it);
        std::cout << *it << std::endl;
    }
}

void mello_gen(int count, char *key)
{
    std::vector<std::string> notes;

    accidentals = std::vector<std::string>();

    if      (strcmp(key, "A") == 0)   fill_sharps(3);
    else if (strcmp(key, "Am") == 0)  ;
    else if (strcmp(key, "B") == 0)   fill_sharps(5);
    else if (strcmp(key, "Bm") == 0)  fill_sharps(2);
    else if (strcmp(key, "C") == 0)   ;
    else if (strcmp(key, "Cm") == 0)  fill_flats(3);
    else if (strcmp(key, "D") == 0)   fill_sharps(2);
    else if (strcmp(key, "Dm") == 0)  fill_flats(1);
    else if (strcmp(key, "E") == 0)   fill_sharps(4);
    else if (strcmp(key, "Em") == 0)  fill_sharps(1);
    else if (strcmp(key, "F") == 0)   fill_flats(1);
    else if (strcmp(key, "Fm") == 0)  fill_flats(4);
    else if (strcmp(key, "G") == 0)   fill_sharps(1);
    else if (strcmp(key, "Gm") == 0)  fill_flats(2);
    else if (strcmp(key, "F#") == 0)  fill_sharps(6);
    else if (strcmp(key, "F#m") == 0) fill_sharps(3);
    else if (strcmp(key, "C#") == 0)  fill_sharps(7);
    else if (strcmp(key, "C#m") == 0) fill_sharps(4);
    else if (strcmp(key, "G#m") == 0) fill_sharps(5);
    else if (strcmp(key, "D#m") == 0) fill_sharps(6);
    else if (strcmp(key, "A#m") == 0) fill_sharps(7);
    else if (strcmp(key, "Bb") == 0)  fill_flats(2);
    else if (strcmp(key, "Eb") == 0)  fill_flats(3);
    else if (strcmp(key, "Ab") == 0)  fill_flats(4);
    else if (strcmp(key, "Db") == 0)  fill_flats(5);
    else if (strcmp(key, "Gb") == 0)  fill_flats(6);
    else if (strcmp(key, "Cb") == 0)  fill_flats(7);
    else if (strcmp(key, "Bbm") == 0) fill_flats(5);
    else if (strcmp(key, "Ebm") == 0) fill_flats(6);
    else if (strcmp(key, "Abm") == 0) fill_flats(7);
    else return;

    int i, j, index;
    bool found;
    srand(time(0));
    for (i = 0; i < count; i++) {
        found = false;
        index = rand() % reg_notes.size();
        std::string note_with_accidental = reg_notes[index];
        for (auto it = accidentals.begin(); it != accidentals.end(); it++) {
            if ((*it)[0] == reg_notes[index][0]) {
                note_with_accidental = *it;
                found = true;
            }
        }
        notes.push_back(note_with_accidental);
    }
    std::string cmd = "";
    cmd += "play ";
    for (auto it = notes.begin(); it != notes.end(); it++) {
        if (*it == "A")
            cmd += " WAV/A.wav ";
        else if (*it ==  "A#" || *it == "Bb")
            cmd += " WAV/Bflat.wav ";
        else if (*it ==  "B")
            cmd += " WAV/B.wav ";
        else if (*it == "B#" || *it == "C")
            cmd += " WAV/C.wav ";
        else if (*it == "C#" || *it == "Db")
            cmd += " WAV/Csharp.wav ";
        else if (*it == "D")
            cmd += " WAV/D.wav ";
        else if (*it == "D#" || *it == "Eb")
            cmd += " WAV/Eflat.wav ";
        else if (*it == "E")
            cmd += " WAV/E.wav ";
        else if (*it == "E#" || *it ==  "F")
            cmd += " WAV/F.wav ";
        else if (*it ==  "F#" || *it == "Gb")
            cmd += " WAV/Fsharp.wav ";
        else if (*it == "G")
            cmd += " WAV/G.wav ";
        else if (*it == "G#" || *it == "Ab")
            cmd += " WAV/Gsharp.wav ";
    }
    std::cout << cmd << std::endl;
    system(cmd.c_str());
}

int main(int argc, char *argv[])
{
    if (argc != 3) {
        std::cerr << "Mello usage: mello <number of notes> <key signature>" << std::endl;
        return -1;
    }
    mello_gen(std::atoi(argv[1]), argv[2]);
    return 0;
}
