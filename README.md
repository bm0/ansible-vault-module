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
      no_log: yes   # Set if you want to hide the module output

    - debug: var=foo.top_secret
```