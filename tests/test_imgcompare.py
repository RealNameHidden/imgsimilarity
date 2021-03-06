import csv
import dhash
from PIL import Image
from imgsimilarity import diff
dictHash = dict()
results = [
    ['tests/resources/img1.gif', 'tests/resources/img2.jpg', 0.0, 0.125],
    ['tests/resources/img1.gif', 'tests/resources/img3.jpg', 0.19, 0.078],
    ['tests/resources/img2.jpg', 'tests/resources/img3.jpg', 0.19, 0.0],
    ['tests/resources/img1.gif', 'tests/resources/img5.jpg', 0.53, 0.0],
    ['tests/resources/img2.jpg', 'tests/resources/img5.jpg', 0.53, 0.0],
    ['tests/resources/img4.jpg', 'tests/resources/img1.gif', 0.34, 0.031]]
csvfile = None
row1 = None
row2 = None

# class TestClass:
def setup_module(module):
    global dictHash, results, csvfile, row1, row2
    with open("tests/resources/Image_Loc.csv", encoding='utf-8-sig') as file:
        csvfile = csv.reader(file)
        for i, row in enumerate(csvfile):
            if i == 0:
                row1 = row
            if i == 1:
                row2 = row
    file.close()


def test_computeScore():
    assert 0.0 == diff.computeScore(dictHash, row1)
    assert 0.19 == diff.computeScore(dictHash, row2)


def test_diff():
    h1 = dhash.dhash_int(Image.open(row1[0]))
    h2 = dhash.dhash_int(Image.open(row1[1]))
    print(0, diff.diff(h1, h2))


def test_computeScore():
    assert results.__eq__(diff.computeScore(dictHash, row1))
