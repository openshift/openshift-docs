# Logging

The kuadrant operator outputs 3 levels of log messages: (from lowest to highest level)

1. `debug`
2. `info` (default)
3. `error`

`info` logging is restricted to high-level information. Actions like creating, deleteing or updating kubernetes resources will be logged with reduced details about the corresponding objects, and without any further detailed logs of the steps in between, except for errors.

Only `debug` logging will include processing details.

To configure the desired log level, set the environment variable `LOG_LEVEL` to one of the supported values listed above. Default log level is `info`.

Apart from log level, the operator can output messages to the logs in 2 different formats:

- `production` (default): each line is a parseable JSON object with properties `{"level":string, "ts":int, "msg":string, "logger":string, extra values...}`
- `development`: more human-readable outputs, extra stack traces and logging info, plus extra values output as JSON, in the format: `<timestamp-iso-8601>\t<log-level>\t<logger>\t<message>\t{extra-values-as-json}`

To configure the desired log mode, set the environment variable `LOG_MODE` to one of the supported values listed above. Default log level is `production`.
