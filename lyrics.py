import requests
import argparse


def convert_to_srt(synced_lyrics):
    lines = synced_lyrics.strip().split("\n")
    srt_output = []

    for i in range(len(lines) - 1):  # Exclude the last timestamp without text
        current_timestamp, text = lines[i].split("]", 1)
        current_timestamp = current_timestamp.strip("[")
        text = text.strip()
        next_timestamp = lines[i + 1].split("]", 1)[0].strip("[")
        srt_output.append(f"{i + 1}\n{format_srt(current_timestamp)} --> {format_srt(next_timestamp)}\n{text}\n\n")

    return "".join(srt_output)


def format_srt(timestamp):
    minutes, seconds = map(float, timestamp.split(":"))
    hours, minutes = divmod(int(minutes), 60)
    seconds, milliseconds = divmod(seconds, 1)
    return f"{hours:02}:{minutes:02}:{int(seconds):02},{int(milliseconds * 1000):03}"


def get_lyrics(track, artist, album=None, duration=None):
    url = "https://lrclib.net/api/get"
    params = {"artist_name": artist, "track_name": track, "album_name": album, "duration": duration}

    response = requests.get(url, params=params)
    data = response.json()

    if "syncedLyrics" in data:
        return data["syncedLyrics"]
    exit(f"No lyrics found for {artist} - {track}")


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("track", help="Track name")
    args.add_argument("artist", help="Artist name")
    args.add_argument("--album", help="Album name")
    args.add_argument("--duration", help="Duration of the track in seconds", type=int)

    lyrics = get_lyrics(**vars(args.parse_args()))
    srt = convert_to_srt(lyrics)
    with open("lyrics.srt", "w") as file:
        file.write(srt)
    print("Lyrics saved to lyrics.srt")
