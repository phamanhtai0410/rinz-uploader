# -*- coding: utf-8 -*-
import boto3
from .config import DefaultConfig

# Redis cache
# redis_cache = Redis()
# Redis user info, will initialized in app
# redis_cluster = RedisCluster(startup_nodes=DefaultConfig.REDIS_USERS_STARTUP_NODES,
#                              decode_responses=True)  # print('Init Redis user info successfully')
# redis_user_info=None


# db = SQLAlchemy()
s3 = boto3.client(
    "s3",
    aws_access_key_id=DefaultConfig.S3_KEY,
    aws_secret_access_key=DefaultConfig.S3_SECRET,
    endpoint_url=DefaultConfig.S3_ENDPOINT,
    use_ssl=False,
)
