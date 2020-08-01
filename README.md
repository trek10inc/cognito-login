# Cognito Login: A CLI to get a jwt from cognito login credentials

Makes heavy use of the [warrant](https://github.com/capless/warrant) library to make it easy to get a jwt from a cognito userpool.

## Configuration

Configuration for this project is sourced from your current working directory `./.cognito-login.yaml`, your home directory `~/.cognito-login.yaml`, or environment variables showin in the `cognito-login --help` output.

Configuration file properties look similar to the command-line arguments, except without the `--`.

The following command

```sh
$ cognito-login --user-pool-id us-east-1_ABCABCABC --app-client-id abcabcabcabcabcabcabcabcab -u ... -p ...
```

can be made easier by defining the following config:

```yaml
user-pool-id: us-east-1_ABCABCABC
app-client-id: abcabcabcabcabcabcabcabcab
```

so you just have to execute this command:

```sh
$ cognito-login -u ... -p ...
```

## Usage

### -h, --help

Get more information on how to use the command

### -v, --version

Display the current version of cognito-login

### --user-pool-id

The ID of the user pool you want to authenticate with

### --app-client-id

The ID of the user pool's app client you want to authenticate with

### -u, --username

The username of the user you want to authenticate

### -p, --password

The password of the user you want to authenticate
