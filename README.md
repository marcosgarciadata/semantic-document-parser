# *Prism Scaffold**

> *"transform ideas into working prototypes — zero configuration required."*

Prism Scaffold is a hybrid orchestrator that creates **instant service blueprints** from declarative YAML definitions.
Think *Docker Compose* meets *Snowpack*, optimized for rapid prototyping.

---

### Quickstart

```bash
npm i -g prism-scaffold
prism init ./project.yaml
```

Example:

```yaml
services:
  api:
    image: node:20
    command: npm start
    ports: [3000]
  db:
    image: postgres:15
```

### Key Features

* generates Dockerfiles automatically
* hot reload for services
* dependency visualization (`prism graph`)
* offline capable

> Built by [scaffold.systems](https://scaffold.systems) — for rapid iteration.

MIT © Prism Systems 2025
