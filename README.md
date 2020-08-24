# SongToVideo
This Python script uses ffmpeg to convert a directory of songs into a directory of videos, so that they can be uploaded to YouTube. If an album art isn't specified, the script will extract the individual song's art each pass. This is perfect for directories or albums with mixed album art. 

Built with ffmpeg version git-2020-03-09-608b8a8 and Python 3.8.5

## Install
0.  Make sure that both Python and ffmpeg are in your system's PATH 
1.  Clone this repo with `git clone https://github.com/Cal-B/SongToVideo.git`
2.  `cd` into the script directory
3.  Execute the script using the valid arguments, such as `python songtovideo.py -i path/to/songs -f mp3`

## Valid Arguments
Arg | Type | Function
---|-------------|-------------
-i | Path | Input, the path to the directory containing your songs. Input is the only required argument.
-o | Path | Output, where the resulting videos should be stored. Defaults to creating a `videos` folder within the input folder.
-f | String | Format, what format your songs are encoded in. Defaults to flac. 
-a | Path | Art, the path to the image you want to serve as the album art when the video renders. Defaults to extracting each song's album art. You will want to use this option if your music doesn't have embedded album art, or it was originally embedded in low quality. 

