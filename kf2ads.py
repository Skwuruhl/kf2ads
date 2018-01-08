import math

def normalize(x):
    if coef > 0:
        return math.atan(coef*math.tan(radialzooms[x]/2)) / math.atan(coef*math.tan(radialfov/2)) / zooms[x] / 0.013330
    return math.tan(radialzooms[x]/2) / math.tan(radialfov/2) / zooms[x] / 0.013330

fovMult = float(input("FOVOptionsPercentageValue="))
coef = float(input("Coefficient="))
fov = 90 * fovMult
radialfov = math.radians(fov)
zooms = [80, 77, 75, 73, 70, 65]
zooms = [fovMult*z for z in zooms]
radialzooms = [math.radians(z) for z in zooms]
normalizations = [normalize(x) for x in range(0,6)]
keys = ['NumpadOne', 'NumpadTwo', 'NumpadThree', 'NumpadFour', 'NumpadFive', 'NumpadSix']
output = ''
for x in range(0,6):
    output += 'SetBind {} "fov {}|SetZoomedSensitivity {}"|'.format(keys[x], zooms[x], round(normalizations[x],6))
print('Paste the following into console:', end='\n')
print(output[:-1])
