from setuptools import setup

setup(name="libwinmedia",
      version="1.0.1",
      description="Python bindings for libwinmedia, a tiny yet powerful media playback library for Windows and Linux.",
      long_description=open("README.md", "r").read(),
      long_description_content_type="text/markdown",
      author="libwinmedia Team",
      author_email="mytja@protonmail.com",
      url="https://github.com/libwinmedia/libwinmedia-py",
      include_package_data=True,
      license="MIT",
      packages=["libwinmedia"],
      package_dir={
          "libwinmedia": "libwinmedia",
      },
      classifiers=[
          "Topic :: Multimedia :: Sound/Audio",
          "Operating System :: POSIX :: Linux",
          "Operating System :: Microsoft :: Windows :: Windows 10",
          "Operating System :: Microsoft :: Windows",
          "Topic :: Multimedia :: Video",
          "License :: OSI Approved :: MIT License"
      ],
      install_requires=[
            'PyGObject; platform_system=="Linux"'
      ],
      data_files=[]
)
