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