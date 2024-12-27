# langchain-s3-text-loaders

AWS S3 directory and file loaders for **text files**, for instance text, html, xml, json, etc.

Inspired by `langchain-community`'s `S3FileLoader` and `S3DirectoryLoader`, `langchain_s3_text_loaders` provides loaders optimized for text e.g. plain text, html, xml, json, etc. 

## Install

```bash
pip install langchain-s3-text-loaders
```

## Usage

```python
from langchain_s3_text_loaders import S3DirectoryLoader
s3_dir = S3DirectoryLoader(bucket="my-bucket", prefix="my_prefix")
docs = s3_dir.load()
```

## Advanced Usage

```python
from langchain_s3_text_loaders import S3DirectoryLoader
s3_dir = S3DirectoryLoader(
    bucket: str,
    prefix: str = "",
    batch_size=50, # number of concurrent s3 downloads
    region_name: Optional[str] = None,
    api_version: Optional[str] = None,
    use_ssl: Optional[bool] = True,
    verify: Union[str, bool, None] = None,
    endpoint_url: Optional[str] = None,
    aws_access_key_id: Optional[str] = None,
    aws_secret_access_key: Optional[str] = None,
    aws_session_token: Optional[str] = None,
    boto_config: Optional[botocore.client.Config] = None,
    )
docs = s3_dir.load()
```

## License
MIT
