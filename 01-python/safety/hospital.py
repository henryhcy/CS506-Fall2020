def draw_hospital(width = 4, height = 3):

    if width < 4 or height < 3:
        raise Exception("width >= 4, height >= 3")
    
    indent = width - 4
    indent = indent // 2
    
    print("-"*width)
    print(" "*indent + " || ")
    print(" "*indent + "=  =")
    print(" "*indent + " || ")
    for h in range(height - 3):
        print()
    print("-"*width)
