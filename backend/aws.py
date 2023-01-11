from typing import Optional, List

import boto3
from asgiref.sync import sync_to_async
from cachetools import cached, TTLCache
from django.conf import settings
from strawberry_django_plus import gql

from backend.types2 import Location

location_client = boto3.client('location',
                               region_name="us-west-2",
                               aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                               aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)


@cached(cache=TTLCache(maxsize=4096, ttl=86400))
def get_suggestion(text, top_n):
    result: dict = location_client.search_place_index_for_suggestions(
        IndexName='PhotoShareApp',
        MaxResults=top_n,
        Text=text
    )
    return [place['Text'] for place in result["Results"]]


def parse_address(address: str) -> Location:
    parts = address.split(',', maxsplit=1)
    main = parts[0]
    secondary = parts[1].strip() if len(parts) == 2 else ""
    return Location(main=main, secondary=secondary, full_address=address)


@gql.type
class AWSQuery:

    @gql.field
    @sync_to_async
    def location_suggestions(self, text: str, top_n: Optional[int] = 5) -> List[Location]:
        addresses = get_suggestion(text, top_n)
        return [parse_address(a) for a in addresses]
