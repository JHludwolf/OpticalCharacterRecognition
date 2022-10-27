#
# ./ocr.py : Perform optical character recognition, usage:
#     ./ocr.py train-image-file.png train-text.txt test-image-file.png
#    test-0-0.png test-0-0.txt test-1-0.png
# 
# Authors: (insert names here)
# (based on skeleton code by D. Crandall, Oct 2017)
#

from PIL import Image
from ocr_solver import OCRSolver


CHARACTER_WIDTH = 14
CHARACTER_HEIGHT = 25


def load_letters(fname):
    im = Image.open(fname)
    px = im.load()
    (x_size, y_size) = im.size
    print(im.size)
    print(int(x_size / CHARACTER_WIDTH) * CHARACTER_WIDTH)
    result = []
    for x_beg in range(0, int(x_size / CHARACTER_WIDTH) * CHARACTER_WIDTH, CHARACTER_WIDTH):
        result += [["".join(['*' if type(px[x, y]) is not tuple and px[x, y] < 1 else ' ' for x in range(x_beg, x_beg + CHARACTER_WIDTH)]) for y in range(0, CHARACTER_HEIGHT)], ]
    return result

def load_training_letters(fname):
    TRAIN_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(),.-!?\"' "
    letter_images = load_letters(fname) 
    return {TRAIN_LETTERS[i]: letter_images[i] for i in range(0, len(TRAIN_LETTERS))}


#####
# main program
#(train_img_fname, train_txt_fname, test_img_fname) = sys.argv[1:]
#train_img_fname = 'TestFiles/Optical-Character-Recognition-using-Hidden-Markov-Models-master/courier-train.png'
#train_txt_fname = 'TestFiles/Optical-Character-Recognition-using-Hidden-Markov-Models-master/test-0-0.txt'
#test_img_fname = 'TestFiles/Optical-Character-Recognition-using-Hidden-Markov-Models-master/test-15-0.png'

train_img_fname = 'tests/train2.png'
train_txt_fname = 'TestFiles/Optical-Character-Recognition-using-Hidden-Markov-Models-master/test-0-0.txt'
test_img_fname = 'tests/test182.png'

train_letters = load_training_letters(train_img_fname)
test_letters = load_letters(test_img_fname)

# Below is just some sample code to show you how the functions above work.
# You can delete them and put your own code here!
solver = OCRSolver(train_letters, test_letters, train_txt_fname)
solver.simplified()
solver.hmm_ve()
solver.hmm_viterbi()
# Each training letter is now stored as a list of characters, where black
#  dots are represented by *'s and white dots are spaces. For example,
#  here's what "a" looks like:

# print "\n".join([r for r in train_letters['a']])

# Same with test letters. Here's what the third letter of the test data
#  looks like:
# print "\n".join([r for r in test_letters[2]])
