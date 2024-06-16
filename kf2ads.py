import math

def normalize(x):
    if mode == 1:
        return math.tan(radialzooms[x]/2) / math.tan(radialfov/2) / zooms[x] / 0.01333 * coef
    return math.atan(coef*math.tan(radialzooms[x]/2)) / math.atan(coef*math.tan(radialfov/2)) / zooms[x] / 0.01333

fovMult = float(input("FOVOptionsPercentageValue="))
mode = int(input("Mode:\n1 for zoom ratio\n2 for monitor distance\n\t"))
coef = float(input("Coefficient="))
fov = 90 * fovMult
radialfov = math.radians(fov)
zooms = [80, 77, 75, 73, 70, 65, 50]
zooms = [fovMult*z for z in zooms]
radialzooms = [math.radians(z) for z in zooms]
scopes = [48, 27, 20.5]
radialscopes = [math.radians(s) for s in scopes]
scopes = [(70/12.5 * 8), (70/23 * 16), (70/18.5 * 12)]
zooms += scopes
radialzooms += radialscopes
normalizations = [normalize(x) for x in range(0,10)]
keys = ['NumpadZero', 'NumpadOne', 'NumpadTwo', 'NumpadThree', 'NumpadFour', 'NumpadFive', 'NumpadSix', 'NumpadSeven', 'NumpadEight', 'NumpadNine']
output = ''
for x in range(0,10):
    output += 'SetBind {} "SetZoomedSensitivity {}"|'.format(keys[x], round(normalizations[x],6))
print('Paste the following into console:', end='\n')
print(output[:-1])
