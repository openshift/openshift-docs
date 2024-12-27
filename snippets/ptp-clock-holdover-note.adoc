:_mod-docs-content-type: SNIPPET
[NOTE]
====
During holdover, the T-GM or T-BC uses the internal system clock to continue generating time synchronization signals as accurately as possible based on the last known good reference.

You can set the time holdover specification threshold controlling the time spent advertising `ClockClass` values `7` or `135` to `0` so that the T-GM or T-BC advertises a degraded `ClockClass` value directly after losing traceability to a PRTC.
In this case, after initially advertising `ClockClass` values between `140–165`, a clock can still be within the holdover specification.
====

For more information, see link:https://www.itu.int/rec/T-REC-G.8275.1-202211-I/en["Phase/time traceability information", ITU-T G.8275.1/Y.1369.1 Recommendations].
