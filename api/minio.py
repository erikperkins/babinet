import duckdb


class MinioClientException(Exception):
  def __init__(self, message = None):
    super().__init__(message)


class MinioQueryException(Exception):
  def __init__(self, message = None):
    super().__init__(message)


class MinioClient:
  """Connect to MinIO."""
  def __init__(self, endpoint = None, access_key = None, secret_key = None):
    self.endpoint = endpoint
    self.access_key = access_key
    self.secret_key = secret_key

    try:
      self.client = duckdb.connect(database = ':memory:', read_only = False)
      self.client.execute(f"""
      INSTALL httpfs;
      LOAD httpfs;
      SET s3_endpoint='{self.endpoint}';
      SET s3_access_key_id='{self.access_key}';
      SET s3_secret_access_key='{self.secret_key}';
      SET s3_use_ssl=false;
      """)
    except Exception as e:
      raise MinioClientException(e)

  def query_parquet(self, bucket = None, file = None, query = None):
    """
    Query Parquet file in bucket.
    FROM clause should say only PARQUET, to be replaced by the
    specified bucket and object name.
    """
    parquet = f"read_parquet('s3://minio/{bucket}/{file}.parquet')"
    sql = query.replace('PARQUET', parquet)

    try:
      results = self.client.sql(sql).df()
    except Exception as e:
      raise MinioQueryException(e)

    return results
