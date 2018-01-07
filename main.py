from pydub import AudioSegment
from os import listdir, stat, mkdir, getcwd
from os.path import isfile, join


def is_wav_file(cwd, fname):
    if len(fname) < 4:
        return False
    else:
        return isfile(join(cwd, fname)) and fname[-3:] == 'wav'


def main():
    op = 'output'
    try:
        stat(op)
    except:
        mkdir(op)

    cwd = getcwd()
    wavfiles = [f for f in listdir(cwd) if is_wav_file(cwd, f)]
    for fname in wavfiles:
        wav = AudioSegment.from_wav(fname)
        wav.export('{0}/{1}/{2}mp3'.format(cwd, op, fname[:-3]), format="mp3", bitrate='320k')


main()
