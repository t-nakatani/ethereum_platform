

```
curl 127.0.0.1:8545 -X POST \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_syncing","params": [],"id":1}'
```

geth logs
```.out
geth-execution-node  | INFO [11-04|01:30:47.073] Syncing: state download in progress      synced=5.17%  state=15.94GiB  accounts=13,765,962@2.76GiB   slots=60,103,221@12.64GiB  codes=101,077@546.40MiB eta=6h5m48.140s
geth-execution-node  | INFO [11-04|01:30:48.726] Syncing: chain download in progress      synced=19.75% chain=9.49GiB    headers=4,208,640@1.32GiB    bodies=4,169,757@5.29GiB    receipts=4,169,757@2.88GiB    eta=1h22m8.227s
```


### kill geth (in restart)
https://github.com/celo-org/celo-blockchain/issues/857
docker update && kill -s INT PID (less convenient than pkill geth) && docker logs (to see how it gracefully shuts down) && do what i need (for example snapshot db to startup new machine) && docker update &&docker start && docker logs
