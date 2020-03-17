from pyknon.music import Note, NoteSeq
from pyknon.genmidi import Midi


def generate_patterns(pattern, n_rotations=12, repeat=4):
    result = NoteSeq()
    for n in range(0, n_rotations):
        rotation = pattern.rotate(n)
        result.extend(rotation * repeat)
    return result


def generate_phase(n_rotations=12, repeat=4):
    pattern = NoteSeq("E16 F# B C#'' D'' F#' E C#'' B' F# D'' C#")
    piano1 = pattern * (n_rotations + 1) * repeat
    piano2 = generate_patterns(pattern, n_rotations, repeat)
    return piano1, piano2


if __name__ == '__main__':
    repeat = 4
    piano1, piano2 = generate_phase(repeat=repeat)

    midi = Midi(2, tempo=108)
    midi.seq_notes(piano1)
    midi.seq_notes(piano2, track=1, time=3*repeat)
    midi.write("./_outputs/piano_phase.mid")
