#!/usr/bin/env python3
"""
fabric script to generate zip file
of the web static
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    function to create zip
    """
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    
    # Run the tar command and check the exit code
    result = local('tar -cvzf versions/{} web_static'.format(archive), capture=True)
    
    if result.succeeded:
        return 'versions/{}'.format(archive)
    else:
        return None
