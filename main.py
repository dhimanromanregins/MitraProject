import boto3

# Vultr Object Storage credentials
endpoint_url = 'https://blr1.vultrobjects.com'
access_key_id = 'RPXXFVF2T8NYMS0HU92G'
secret_access_key = 'nU3jO0rP7pCGKFmab3vUuSDacaaN4jvKlOlFCMHM'

# Create an S3 client for Vultr Object Storage
s3 = boto3.client(
    's3',
    endpoint_url=endpoint_url,
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key
)

# Specify the desired bucket name
bucket_name = 'mitra-bucket'

# Create the Vultr Object Storage bucket
s3.create_bucket(Bucket=bucket_name)

print(f"Bucket '{bucket_name}' created successfully.")
