clean:
	rm -irf .coverage ./cover/ ./dist ./hamqth.egg-info

prepare_release: clean test sdist
	echo "Have you bumped the version?"

sdist:
	pipenv run sdist

test:
	pipenv run tests
