# FT_OTP
ft_otp allows you to store an initial password in file, and can generate a new one time password every time it is requested.

## Setup

`make` Create environment and executable

`make clean` stop environment and delete exec

## Usage
    ./ft_otp [options]

  - Option -g [64_HEXA_KEY] : store the encrypted key in ft_otp.key 
  - Option -k [FILE / KEY] : generates a new temporary password based on the key given

## Test

`openssl rand -hex 32` Generate a random 32 bytes hexadecimal key (1 bytes = 2 characters)

`oathtool –totp $(cat key.txt)` Generate code based on the given key (not encrypted)