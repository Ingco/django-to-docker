from django.db import models
from django.utils import timezone


class FileParent(models.Model):
    """Parent for File model"""

    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "File parent"
        verbose_name_plural = "File parents"

    def __str__(self):
        return self.title


def get_file_name() -> str:
    """Make and get name for file"""
    return timezone.now().isoformat().replace(":", "_").replace(".", "_")


class MyImage(models.Model):
    """Images"""

    img_name = models.CharField(
        max_length=255, verbose_name="Image name", default=get_file_name
    )
    img = models.ImageField(upload_to="upload/images/%Y/%m/%d/", verbose_name="Image")
    parent = models.ForeignKey(
        FileParent,
        on_delete=models.CASCADE,
        verbose_name="Parent",
        related_name="myimage_parent"
    )

    class Meta:
        verbose_name = "My image"
        verbose_name_plural = "My images"

    def __str__(self):
        return self.img_name


class MyFile(models.Model):
    """Files"""

    file_name = models.CharField(
        max_length=255, verbose_name="File name", default=get_file_name
    )
    my_file = models.ImageField(upload_to="upload/files/%Y/%m/%d/", verbose_name="File")
    parent = models.ForeignKey(
        FileParent,
        on_delete=models.CASCADE,
        verbose_name="Parent",
        related_name="myfile_myfile"
    )

    class Meta:
        verbose_name = "My file"
        verbose_name_plural = "My files"

    def __str__(self):
        return self.file_name
