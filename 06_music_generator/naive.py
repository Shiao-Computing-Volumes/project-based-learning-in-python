from pyknon.music import Note, NoteSeq
from pyknon.genmidi import Midi

def generate_phrase():
    patterns = []
    # patterns.extend(NoteSeq("C4 D E F G A B"))
    patterns.extend(NoteSeq("E5 D#5 E5 D#5 E5 B4 D5 C5"))
    return patterns


if __name__ == '__main__':
    piece = generate_phrase()

    midi = Midi(2, tempo=108)
    midi.seq_notes(piece)
    midi.write("./_outputs/naive.mid")
