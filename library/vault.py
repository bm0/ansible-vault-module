#!/usr/bin/env python
# coding=utf-8

import os
import json
from urlparse import urljoin
from ansible.module_utils.basic import *
from ansible.module_utils import urls


def main():
    fields = {
        'vault_addr': {'required': False, 'type': 'str'},
        'path': {'required': True, 'type': 'str'},
    }
    module = AnsibleModule(argument_spec=fields)

    vault_token = os.getenv('VAULT_TOKEN')
    vault_addr = os.getenv('VAULT_ADDR', module.params.get('vault_addr'))

    if not vault_token:
        raise RuntimeError('You must provide environment variable VAULT_TOKEN!')
    if not vault_addr:
        raise RuntimeError('You must provide a address to Vault server'
                           ' via the VAULT_ADDR environment variable or as a module parameter')

    headers = {'X-Vault-Token': vault_token}
    url = urljoin(vault_addr, module.params['path'])
    response, info = urls.fetch_url(module, url, headers=headers)
    data = response.read()

    module.exit_json(response=json.loads(data))

if __name__ == '__main__':
    main()
