# ansible-vault-module

Example
```yaml
---
- hosts: localhost
  tasks:
    - name : run custom module
      vault:
        vault_addr: http://127.0.0.1:8200/v1/
        path: secret/foo
      register: foo

    - debug: var=foo.top_secret
```

Enviroment variables:
```bash
export VAULT_ADDR='http://127.0.0.1:8200/v1/' # optional
export VAULT_TOKEN='f2b36cf6-f9c6-3062-be9b-797041b174ff'
```
