from PIL import Image

black_to_white = [(0, 0, 0), (28, 28, 28), (56, 56, 56), (85, 85, 85), (113, 113, 113), (141, 141, 141), (170, 170, 170), (198, 198, 198), (226, 226, 226), (255, 255, 255)]
ocean_beach_forest = [(5, 6, 27), (11, 15, 134), (25, 68, 178), (60, 143, 215), (60, 208, 215), (237, 255, 68), (79, 255, 0), (70, 200, 11), (29, 145, 32), (9, 110, 12)]
black_orange_yellow_white = [(0, 0, 0, 255), (63, 27, 0, 255), (127, 54, 0, 255), (191, 81, 0, 255), (255, 108, 0, 255), (255, 157, 0, 255), (255, 206, 0, 255), (255, 255, 0, 255), (255, 255, 127, 255), (255, 255, 255, 255)]
dark_grey_brown = [(42, 39, 30), (48, 46, 39), (55, 53, 48), (67, 65, 59), (79, 77, 71), (91, 89, 83), (103, 101, 95), (116, 113, 107), (91, 89, 83), (55, 53, 48)]
grass = [(21, 21, 21), (23, 27, 24), (26, 33, 27), (28, 40, 31), (31, 46, 34), (34, 53, 38), (42, 69, 47), (50, 85, 57), (59, 102, 67), (69, 119, 77)]

def ReadGradient(path):
    to_read = Image.open(path)
    gradient = [to_read.getpixel((x, 0)) for x in range(0, 10)]
    return gradient

def SaveGradient(gradient, name):
    to_save = Image.new('RGBA', (10, 1))
    to_save.putdata(gradient)
    to_save.save(f'gradients/{name}')

# print(ReadGradient("gradients/black_orange_yellow_white.png"))
# SaveGradient(grass, "grass.png")
