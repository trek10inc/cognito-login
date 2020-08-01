# Changelog

## 0.0.0 - 2020-08-01 Initial release

- initial release
- implements
  - plugin management system
  - core logic through default plugins
  - custom exception classes for application error handling
  - arguments can be sourced through config files (`./.cognito-login.yaml` then `~/.cognito-login.yaml`) or environment variables (shown in the `cognito-login --help` output)
  - core functionality to use the warrant library to authenticate against a given user pool/app client with username and password and return the jwt. Catches when the user is in a `ForceChangePassword` state and will prompt for a new password. Also catches if the user is in a `PasswordResetRequired` state and prompts for both the new password and the password reset code
