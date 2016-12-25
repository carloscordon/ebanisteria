
from uuid import uuid1
import boto3

session = boto3.Session(profile_name='carlos')

client = session.client('cloudfront')
response = client.create_invalidation(
        DistributionId='E3POJ2XS0DE4TL',
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [
                    '/*',
                    ]
                },
            'CallerReference': str(uuid1())
            }
        )
