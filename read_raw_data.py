import numpy as np 

def read_raw_data(filename, height, width):
    # black level compensation value for ov10640: 125
    blc = 125
    #filename = './frame.bin'
    #raw_image = Raw(filename)
    fid = open(filename, "rb")
    raw = fid.read()

    img = np.frombuffer(raw, dtype=np.int16)
    img = np.reshape(img, (height,width))
    #shape(nimg)
    print img.size
    print img.shape
    img = img - blc

    return img