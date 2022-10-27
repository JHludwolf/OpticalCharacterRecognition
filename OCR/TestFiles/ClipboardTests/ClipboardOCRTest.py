from PIL import ImageGrab
import pytesseract
from pytesseract import Output
import numpy as np
import cv2
import pyperclip
import time
import AppKit


def getTextFromClipboard(noiseReduction=False):
    image = ImageGrab.grabclipboard()
    img = np.array(image)

    if noiseReduction:
        norm_img = np.zeros((img.shape[0], img.shape[1]))
        img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
        img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
        img = cv2.GaussianBlur(img, (1, 1), 0)

    results = pytesseract.image_to_data(img, lang="eng+spa", output_type=Output.DICT)
    return ' '.join([r for r in results['text'] if r != ''])


'''
def main():
    try:
        pyperclip.copy(getTextFromClipboard(noiseReduction=True))
        AppKit.NSSound.soundNamed_('Glass').play()
    except:
        pyperclip.copy('')
        AppKit.NSSound.soundNamed_('Funk').play()

    time.sleep(1)


if __name__ == '__main__':
    main()
'''

