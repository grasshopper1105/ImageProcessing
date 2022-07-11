from wand.image import Image

with Image(filename='1.png') as img:
    krnl="5x5: 0,0,0,0,0 1,1,1,1,1 1,1,1,1,1 1,1,1,1,1 0,0,0,0,0"
    img.threshold(threshold=0.75)
    img.morphology(method='close',kernel=krnl)
    img.connected_components(connectivity=4, area_threshold=100, mean_color=True)
    img.save(filename='curve_proc.bmp')