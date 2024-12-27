from langchain_s3_text_loaders import S3TextFileDirectoryLoader

def main():
    bucket = "my-bucket"
    prefix = "my_prefix"

    s3_dir = S3TextFileDirectoryLoader(bucket=bucket, prefix=prefix)
    docs = s3_dir.load()

    print(docs)


if __name__ == "__main__":
    main()