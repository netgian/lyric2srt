
# lyric2srt

`lyric2srt` is a Python script that converts synchronized lyrics (in timestamp format) to SRT files, the standard format used for subtitles. 
This project was made possible thanks to the [lrclib.net](https://lrclib.net) API.

## Requirements

- Python 3.7 or higher.
- Required libraries:
  - `requests`

Install requests by running:
```bash
pip install requests
```

## Usage

The script can be run from the command line with the following arguments:

```bash
python lyric2srt.py <track> <artist> [--album <album>] [--duration <duration>]
```

### Example:

```bash
python lyric2srt.py "Shape of You" "Ed Sheeran" --album "Divide" --duration 233
```

This command will fetch the synchronized lyrics of the song and save them in a `lyrics.srt` file.

## Output

The output file (`lyrics.srt`) contains the synchronized lyrics in SRT format, ready to be used as subtitles in compatible media players.

### Example SRT output:

```
1
00:00:00,000 --> 00:00:10,500
The club isn't the best place to find a lover

2
00:00:10,500 --> 00:00:15,200
So the bar is where I go
```

## Contribution

If you'd like to contribute, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
