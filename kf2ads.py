import math

def normalize(x):
    if mode == 1:
        return math.tan(radialzooms[x]/2) / math.tan(radialfov/2) / zooms[x] / 0.01333 * coef
    return math.atan(coef*math.tan(radialzooms[x]/2)) / math.atan(coef*math.tan(radialfov/2)) / zooms[x] / 0.01333

fovMult = float(input("FOVOptionsPercentageValue="))
mode = input("Mode:\n1 for zoom ratio\n2 for monitor distance\n")
coef = float(input("Coefficient="))
fov = 90 * fovMult
radialfov = math.radians(fov)
zooms = [80, 77, 75, 73, 70, 65, 50]
zooms = [fovMult*z for z in zooms]
radialzooms = [math.radians(z) for z in zooms]
normalizations = [normalize(x) for x in range(0,7)]
keys = ['NumpadOne', 'NumpadTwo', 'NumpadThree', 'NumpadFour', 'NumpadFive', 'NumpadSix', 'NumpadSeven']
output = ''
for x in range(0,7):
    output += 'SetBind {} "SetZoomedSensitivity {}"|'.format(keys[x], round(normalizations[x],6))
print('Paste the following into console:', end='\n')
print(output[:-1])
