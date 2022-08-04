# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import httpx


def download_file(path, *args, **kwargs):
    with path.open(mode='wb', buffering=0) as f:
        with httpx.stream('GET', *args, **kwargs) as response:
            for chunk in response.iter_bytes(16384):
                f.write(chunk)
