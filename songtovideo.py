import os
import glob
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--input", required=True, help="Input folder directory")
arg_parser.add_argument("-o", "--output", required=False, help="Output folder directory, default location is inside the input folder under /videos")
arg_parser.add_argument("-f", "--format", required=False, default='flac', help="Input music file type")
arg_parser.add_argument("-a", "--art", required=False, help="Album art location, in case you don't want to extract the album art on a song-by-song basis")
args = vars(arg_parser.parse_args())

src = args['input']
output = args['output']
filetype = args['format']
art = args['art']

if output is None:
    output = os.path.join(src, 'videos')
if not os.path.exists(output):
    os.mkdir(output)

print("Source directory set to: " + src + ", all files ending in " + filetype)
print("Output directory set to: " + output)

filenames = (f for f in os.listdir(src) if f.endswith('.' + filetype))
total_songs = sum(1 for _ in (f for f in os.listdir(src) if f.endswith('.' + filetype)))

for pos, song in enumerate(filenames):
    song_path = os.path.join(src, song)
    video_output_path = os.path.join(output, os.path.splitext(song)[0] + '.mp4')

    if art is None:     # No specified album art, we are going to extract our current song's art instead
        cover_path = os.path.join(src,'extracted_cover.png')
        extract_cover = f"ffmpeg -hide_banner -loglevel warning -i \"{song_path}\" \"{cover_path}\""
        os.system(extract_cover)
    else:
        cover_path = art

    print("Processing: " + song + " (#" + str(pos + 1) + "/" + str(total_songs) + ")...")
    if filetype == 'flac':
        render_video = f"ffmpeg -hide_banner -loglevel warning -loop 1 -i \"{cover_path}\" -i \"{song_path}\" -vf \"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1\" -c:a aac -ab 320k -c:v libx264 -shortest -strict -2 \"{video_output_path}\""
    else:
        render_video = f"ffmpeg -hide_banner -loglevel warning -loop 1 -i \"{cover_path}\" -i \"{song_path}\" -vf \"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1\" -c:a copy -c:v libx264 -shortest \"{video_output_path}\""
    os.system(render_video)

    if art is None:
        os.remove(cover_path)   # Delete our current extracted cover