ansible-consul
=========

[![asciicast](https://asciinema.org/a/14ffwrvdqgzt47utdckyw314y.png)](https://asciinema.org/a/14ffwrvdqgzt47utdckyw314y)

A very simple ansible role that installs consul and sets it up as a service. Used strictly for demonstration purposes on how to develop ansible roles with [molecule](https://molecule.readthedocs.io/en/stable-1.24/) and is not recommended for production usage. 

Requirements
------------

This role has no pre-requisites.

Role Variables
--------------

Dependencies
------------

This role has no dependencies.

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
         - role: jamescarr.consul

```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
