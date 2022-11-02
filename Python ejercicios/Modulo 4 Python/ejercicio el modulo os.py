import os

class FindDir:
  def find(self, path, dir):
    try:
      os.chdir(path)
    except OSError:
      return

    current_dir = os.getcwd()
    for x in os.listdir('.'):
      if x == dir:
        print(os.getcwd() + '/' + dir)
      self.find(current_dir + '/' + x, dir)


dir_obj = FindDir()
dir_obj.find(path=".\OneDrive", dir="Documentos")