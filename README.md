# Python HamQTH

A [HamQTH] client library for Python.

> HamQTH provides a simple interface for application developers.

This library supports the [XML callbook search](https://www.hamqth.com/developers.php#xml_search) which provides search capability for:

 - callsign data
 - callsign bio
 - recent activity of any callsign

Usage requires [registration](https://www.hamqth.com/register.php) with the HamQTH service.

## Installation

Requests is also required, you made need to install it separately.

```
pip install hamqth
```

## Usage

```
>>> from hamqth import HamQTHClient
>>> client = HamQTHClient()
```

Check out the code and tests for more detailed information.

## Related Projects

These projects also target Python, but [others exist](https://github.com/search?q=hamqth) as well as probably more of which I am not aware.

- [sconklin/hamqthlib]
- [krisp/fauxqrz]

## References

- HamQTH Developer Documentation: [HamQTH | For application developers]
- GitLab Repository: [GitLab Repository]
- GitHub Repository: [GitHub Repository]

[HamQTH]: https://www.hamqth.com
[HamQTH | For application developers]: https://www.hamqth.com/developers.php
[GitLab Repository]: https://gitlab.com/ryanbalfanz/python-hamqth
[GitHub Repository]: https://github.com/RyanBalfanz/python-hamqth
[sconklin/hamqthlib]: https://github.com/sconklin/hamqthlib
[krisp/fauxqrz]: https://github.com/krisp/fauxqrz