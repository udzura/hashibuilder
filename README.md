# hashibuilder

Hashicorp tools off-hand builder

## How to build

Install:

* docker
* docker-machine(on OSX)
* docker-compose

Then run:

```bash
$ docker-compose build --no-cache consul-rpm
```

Want to get rpm, running below copies rpms to ./pkg

```
$ docker-compose run consul-rpm
```

## Available

* consul-rpm
* vault-rpm

Best match for `systemd` installed system. *TODO: add sysvinit script...*
