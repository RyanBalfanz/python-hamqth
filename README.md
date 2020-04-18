# Python HamQTH

A [HamQTH] client library for Python.

> HamQTH provides a simple interface for application developers.

This library supports the [XML callbook search](https://www.hamqth.com/developers.php#xml_search) which provides search capability for:

 - callsign data
 - callsign bio
 - recent activity of any callsign

Usage requires [registration](https://www.hamqth.com/register.php) with the HamQTH service.

## Installation and Usage

For more detailed information check out the [Project Documentation] on GitHub Pages. Also check out the code and tests as the source of truth.

Requests is also required, you made need to install it separately.

```shell
pip install hamqth
```

```python
>>> from hamqth import HamQTHClient
>>> client = HamQTHClient()
>>> client.authenticate('username', 'password')
>>> client.search_callsign('callsign')
…
>>> client.logout()
```

## Related Projects

These projects also target Python, but [others exist](https://github.com/search?q=hamqth) as well as probably more of which I am not aware.

- [sconklin/hamqthlib]
- [krisp/fauxqrz]

## References

- HamQTH Website: [HamQTH]
- HamQTH Developer Documentation: [HamQTH For application developers]
- GitLab Repository: [GitLab Repository]
- GitHub Repository: [GitHub Repository]
- Project Documentation on GitHub Pages: [Project Documentation]

[GitHub Repository]: https://github.com/RyanBalfanz/python-hamqth
[GitLab Repository]: https://gitlab.com/ryanbalfanz/python-hamqth
[HamQTH For application developers]: https://www.hamqth.com/developers.php
[HamQTH]: https://www.hamqth.com
[krisp/fauxqrz]: https://github.com/krisp/fauxqrz
[Project Documentation]: https://ryanbalfanz.github.io/python-hamqth/
[PyPI Page]: https://pypi.org/project/hamqth/
[sconklin/hamqthlib]: https://github.com/sconklin/hamqthlib