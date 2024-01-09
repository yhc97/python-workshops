import os
from pathlib import Path


SOME_CONSTANT = 1_000.00


def find_image_files(folder: os.path = os.path.join(os.path.split(__file__)[0], "..", "images")) -> None:
    """find_image_files
    Simple function that utilises glob for finding image files in
    the folder specified

    Parameters
    ----------
    folder : os.path, optional
        folder to find the image files from,
        by default os.path.join(os.path.split(__file__)[0], "..", "images")
    """

    image_files = Path(folder).glob(os.path.join("*", "*.??g"))

    for image in image_files:
        print(image)


def private_func1():
    print("This should not be exposed")
    return None


def __private_func2():
    print("This should not be exposed either")
    return None
