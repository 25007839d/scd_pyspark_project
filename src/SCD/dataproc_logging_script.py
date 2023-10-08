import logging
from google.cloud import storage

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler(r"/home/g25007839d/log1.txt")
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s-%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.warning('sale upload hoja')

# Imports the Google Cloud client library
storage_client = storage.Client()
bucket = storage_client.get_bucket('rahul-01')
filename = "%s/%s" % ('log', 'log1.txt')
blob = bucket.blob(filename)
blob.upload_from_filename('/home/g25007839d/log1.txt')

# Uploading string of text
# blob.upload_from_string('this is test content!')

# Uploading from a local file using open()
# with open('photo.jpg', 'rb') as photo:
#     blob.upload_from_file(photo)

# Uploading from local file without open()

lis=bucket.list_blobs('hgfhfh')
print(lis.item_to_value)


