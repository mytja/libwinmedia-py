from setuptools import setup

setup(name="libwinmedia",
      version="1.0.0",
      description="Python bindings for libwinmedia, a tiny yet powerful media playback library for Windows.",
      long_description=open("README.md", "r").read(),
      long_description_content_type="text/markdown",
      author="libwinmedia Team",
      author_email="mytja@protonmail.com",
      url="https://github.com/libwinmedia/libwinmedia",
      include_package_data=True,
      license="MIT",
      packages=["libwinmedia"],
      package_dir={
          "libwinmedia": "libwinmedia",
      },
      classifiers=[
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License"
      ],
      data_files=[]
)
