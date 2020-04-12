prepare_release: test sdist
	echo "Have you bumped the version?"

sdist:
	pipenv run sdist

test:
	pipenv run tests
