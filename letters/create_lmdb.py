import numpy as np
import lmdb
import caffe
import glob
import Image
import os

env = lmdb.open('mylmdb')

#transformer = caffe.io.Transformer({'data': (1,3,100,100)})
#transformer.set_transpose('data', (2,0,1))
#transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
#transformer.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB


with env.begin(write=True) as txn:
	data = glob.glob('data/*.jpg')
	for key, item in enumerate(data):
		#img = transformer.preprocess('data', caffe.io.load_image(item))
		file_name = os.path.split(item)
		img = np.array(Image.open(item)) #caffe.io.load_image(item)
		datum = caffe.proto.caffe_pb2.Datum()
		datum.channels = img.shape[2]
		datum.height = img.shape[0]
		datum.width = img.shape[1]
		datum.data = img.tobytes()
		datum.label = ord(file_name[1][0])-97
		str_id = '{:08}'.format(key)
		txn.put(str_id,datum.SerializeToString())

# with env.begin() as txn:
#     print txn.get(b"00000000")

# with env.begin() as txn:
# 	for i in txn.cursor():
# 		print i
