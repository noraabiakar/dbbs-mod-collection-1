import os

__version__ = "0.0.0"

class Package:
  def __init__(self):
    self.mods = []

class Mod:
  pass

def package():
  pkg = Package()
  pkg.path = os.path.dirname(__file__)
  pkg.name = os.path.basename(pkg.path)
  pkg.astro_version = "0.0.4"
  pkg.glia_version = "0.1.1"

  return pkg
