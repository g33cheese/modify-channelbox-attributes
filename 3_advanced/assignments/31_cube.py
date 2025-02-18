#*********************************************************************
# content   = Cube Class assignment
# version   = 0.1.0
# date      = 2025-02-16
# 
# author   = Garvey Chi - garveychi@gmail.com
#*********************************************************************
"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

"""

import maya.cmds as cmds

# Parent Class
class Object:
   def __init__(self, name):
      self.name = name
      self.translate_value = [0.0, 0.0, 0.0]
      self.rotate_value = [0.0, 0.0, 0.0]
      self.scale_value = [1.0, 1.0, 1.0]

   def translate(self, x, y, z):
      self.translate_value = [x, y, z]
      print('{0} translated: {1}, {2}. {3}'.format(self.name, x, y, z))

   def rotate(self, x, y, z):
      self.rotate_value = [x, y, z]
      print('{0} rotated: {1}, {2}, {3}'.format(self.name, x, y, z))

   def scale(self, x, y, z):
      self.scale_value = [x, y, z]
      print('{0} scaled: {1}, {2}, {3}'.format(self.name, x, y, z))

# Child Class
class Cube(Object):
   def __init__(self, name):
      super().__init__(name)
      self.color_value = [1.0, 1.0, 1.0]
      self.cube = cmds.polyCube(name=self.name)

   def color(self, R, G, B): 
      self.color_value = [R, G, B]
      print('{0} set RGB: {1}, {2}, {3}'.format(self.name, R, G, B))

   def print_status(self):
      print('Transform Status for {0}:'.format(self.name))
      print('{0}'.format(self.translate_value))
      print('{0}'.format(self.rotate_value))
      print('{0}'.format(self.scale_value))
      print('{0}'.format(self.color_value))

   def update_transform(self, ttype, value):
      transforms = {'translation': self.translate, 
                       'rotation': self.rotate,
                          'scale': self.scale,
                    }
      transforms[ttype](*value)


cube1 = Cube('cube_001')
cube2 = Cube('cube_002')
cube3 = Cube('cube_003')

cube1.translate(10, 10, 10)
cube1.rotate(90, -45, 90)
cube1.scale(2, 1.5, 1.85)
cube1.color(255, 192, 203)
cube1.print_status()

cube1.update_transform('rotation', [30, 180, -45])