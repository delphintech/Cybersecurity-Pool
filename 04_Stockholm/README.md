# STOCKHOLM
Stockholm is a ransomware that only affects files whose extensions have been affected by **Wannacry**, inside a folder named **infection** inside **HOME** directory.

## Create the key encryption

`make` Create environment and executable

`make clean` Stop environment and delete exec

## Program usage

    ./stockholm [options] KEY
				[-h|-help]
			    [-v|-version]
			    [-r|-reverse]
			    [-s|-silent] 
				[-k|-key] PRIVATE_KEY
			    
 - **-h, -help** : display the help
 - **-v, -version**: Display program's version
 - **-r, -reverse=key**: reverse the infection using the given key
 - **-s, -silent**: Do not display the encrypted files
 - **-k, -key**: Given the private key as argument, it decrypt the key to use for reverse.\
 	Without argument, it generate the private and public key:\
 		=> The private key is to save and be kept secret.\
 		=> The public key is to put inside the class variable pub_key, in stockolm.py.

## Current private key
```
"-----BEGIN RSA PRIVATE KEY-----
MIICWQIBAAKBgQCljHKZhJcMzJQSsfQvuDmF0ewrf8oF3F2Pd5QSNulv8oyJtfUK
MD4O4xVjbZKPnU1SxQ3EB7F1JgzB7h+PiIlwDLbo/sKQ6FouX/UwjqXh9drBxCqh
DQvn2BSuj3dgnctiw1NJNPvRl45stdkHVhvMVh7fGU9ACfOMVgzdb6v0RQIDAQAB
An8sS+heK5w/UH5Ogk9UdXbu17zZ5tenuc9PFDAKr6bGzZ/NOWLX1xDD6v9OG4Ob
6ftGqnOEgIp7TjMbsRvAzEf5xOLgo/2EnJXtGhg4iwWClLS0PPyR0xRU3RTfXire
rZIiT0mhO3M6LjbSM6OBHAz3vSA4p4f7L2VRrhjNFHKnAkEAvap082cXRIbDttLV
pkR9T1pFooqDYpmGR/G4LU7v8VaqkTCU1FhEglwwzqb2BMymQjnAvu4z8oapsAQb
oRgP0wJBAN9yrd8BMGIJdwo5cNENG2RLGU3CeBCp2zxfvoOkv7ugZmxa/S3jPD6G
UMW1+BkLlvtA1G39gQF2NnPlUuXwdIcCQBWRtf0cQzQi000OSwe+kDWfAX5LnEdx
SCkUXyqf6H+cqIccbEB9zUS58T7/E8lV8K5lXPsZocS59cAzp2S5lMsCQFe1jzRz
JgfFiVmVFIiqqW7j36nbRP/dfLYlKwZHnA9NNgcgbDMf+FzeokQJWrqSBxDW8Mu/
72ygd11kzfZ+PW8CQHaDusEPx/U7kS4eoGe5m79ydIn6ySIdXYua+A2CdvcwQF2D
HzCEB3Sakvz1YeEIkXxNcMWZfJFMyQ/fUiOiGz8=
-----END RSA PRIVATE KEY-----"
```