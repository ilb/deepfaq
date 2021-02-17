.PHONY: bootstrap clean lint test

test:
	#conda activate library && python -m unittest discover
	conda activate deeppavlov_faq_bot && python -m unittest discover
	# or another way

lint:
	# add some lint here

update:
	conda env update

bootstrap:
	conda env create -f environment.yml

publish:
	python setup.py sdist bdist_wheel
	# build result will be in /dist, upload them
