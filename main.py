"""
MusicForge
Main Program
"""

from song import Song


def divider(title):

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# --------------------------------------------------
# Create Song
# --------------------------------------------------

song = Song(
    key="E",
    scale="minor",
    bpm=140,
    style="rock"
)

# --------------------------------------------------
# Generate Song
# --------------------------------------------------

song.generate()

# --------------------------------------------------
# Song Information
# --------------------------------------------------

divider("Song Information")

print(f"Key          : {song.key}")
print(f"Scale        : {song.scale_name}")
print(f"BPM          : {song.bpm}")
print(f"Style        : {song.style}")

# --------------------------------------------------
# Song Structure
# --------------------------------------------------

divider("Song Structure")

song.show_structure()

# --------------------------------------------------
# Musical Data
# --------------------------------------------------

divider("Scale")
print(" -> ".join(song.scale))

divider("Chords")
print(" | ".join(song.chords))

divider("Chord Progression")
print(" -> ".join(song.progression))

divider("Melody")
print(" ".join(song.melody))

divider("Bass (MIDI Notes)")
print(song.bass)

divider("Kick Pattern")
print(song.kick)

divider("Snare Pattern")
print(song.snare)

divider("Hi-Hat Pattern")
print(song.hats)

# --------------------------------------------------
# Export
# --------------------------------------------------

divider("Exporting MIDI")

song.export()

print("\n✔ Song exported successfully!")
print("📁 Output: output/song.mid")