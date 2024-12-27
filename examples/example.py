from langchain_s3_text_loaders import S3DirectoryLoader

bucket = "my-bucket"
prefix = "my_prefix"

s3_dir = S3DirectoryLoader(bucket=bucket, prefix=prefix)
docs = s3_dir.load()

print(docs)