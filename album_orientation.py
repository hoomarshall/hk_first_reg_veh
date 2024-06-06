import os
import sys
import shutil
import argparse
from PIL import Image
from glob import glob

# pip3 install -r requirements.txt
# python -m album_orientation --walk_album
# python3 -m album_orientation --walk_album

def walk_album(album=None):

    if not album: raise ValueError('Please enter album Name')
    if not os.path.exists( f'{os.getcwd()}\\{album}\\' ): raise ValueError(f'PATH: "{os.getcwd()}\\{album}\\" DO NOT EXIST' )
    a_h, a_v, a_s = ( f'{os.getcwd()}\\{album}_horizontal\\', f'{os.getcwd()}\\{album}_vertical\\', f'{os.getcwd()}\\{album}_square\\' )
    orientation_map = { 'horizontal':a_h, 'vertical':a_v, 'square':a_s }
    for p_ in orientation_map.values():
        if not os.path.exists( p_ ): os.makedirs( p_ )
    for f_ in glob(f'{os.getcwd()}\\{album}\\*'):
        if not f_.endswith(('.jpg','.png')): continue
        im = Image.open( f_ )
        width, height = im.size
        orientation = 'horizontal' if width > height else 'vertical'
        orientation = 'square' if width == height else orientation
        if orientation in orientation_map: shutil.copy( f_ , orientation_map[orientation])
    for p_ in orientation_map.values():
        print( f"{p_} : {sum(len(f_) for _, _, f_ in os.walk( p_ ))}" )
        if sum(len(f_) for _, _, f_ in os.walk( p_ )) == 0: os.rmdir(p_)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--walk_album", help="walk album in the path", type=str)
    args = parser.parse_args()

    if args.walk_album:
        walk_album(album=args.walk_album)
    sys.exit(0)
