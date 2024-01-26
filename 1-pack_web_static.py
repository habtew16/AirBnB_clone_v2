#!/usr/bin/env python3
"""
fabric script to generate zip file
of the web static
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    function to create zip
    """
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
