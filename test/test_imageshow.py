from test.helper import unittest, PillowTestCase

from PIL import Image
from PIL import ImageShow


class TestImage(PillowTestCase):

    def test_sanity(self):
        dir(Image)
        dir(ImageShow)
        pass


if __name__ == '__main__':
    unittest.main()

# End of file