# Hacking

## Install deps, dev-deps and run test.

```
git clone git@github.com:goombaio/orderedmap.git
cd dag
export GO111MODULE=on  # ref: https://dave.cheney.net/2018/07/16/using-go-modules-with-travis-ci
make deps
make dev-deps
make test
```
