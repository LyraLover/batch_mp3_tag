from eyed3   import load
from os.path import basename, isdir, join
from os      import walk
from sys     import argv

def tagify(fname):
    bname = basename(fname)
    artist = bname.split(' - ')[0]
    title = ' - '.join(bname.split(' - ')[1:])
    title = '.'.join(title.split('.')[:-1])
    print(f'Artist: {artist}\nTitle: {title}\n')
    f = load(fname, (2,))
    try:
        f.tag.artist = artist
        f.tag.title = title
        f.tag.save()
    except:
        print('Failed to modify tags')

def find_files(dname):
    for root, dirs, files in walk(dname):
        for file in files:
            yield join(root, file)
        for dir in dirs:
            for file in find_files(join(root,dir)):
                yield file


def main(dnames):
    for dname in dnames:
        for fname in find_files(dname):
            tagify(fname)


if __name__ == '__main__':
    main(argv[1:])
