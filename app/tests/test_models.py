from django.test import TestCase
from PIL import Image
import os

from app.models import Photo


# Create your tests here.


class PhotoModelTest(TestCase):
    def setUp(self) -> None:
        self.image_local_url = "images/test.png"
        self.img_width = 50
        self.img_height = 75
        img = Image.new("RGB", (self.img_width, self.img_height), "#11814B")
        img2 = Image.new("RGB", (10, 10), "#f1c232")
        img.paste(img2, (0, 0))
        img.save(self.image_local_url)
        self.new_photo = Photo.objects.create(
            title="test", album_id=1, local_url=self.image_local_url
        )

    def tearDown(self) -> None:
        os.remove(self.image_local_url)

    def testShouldReturnCorrectImageSizeWhenCreatingPhotoInstance(self):
        self.assertEqual(self.new_photo.width, self.img_width)
        self.assertEqual(self.new_photo.height, self.img_height)

    def testShouldReturnProperHexCodeOfDominantColorWhenCreatingPhotoInstance(self):
        self.assertRegex(self.new_photo.dominant_color, r"^#\S{6}$")
