docker run --rm -ti \
	-v ${PWD}/.cache:/app/.cache \
	-v ${PWD}/OUTPUT:/app/dzcb/OUTPUT \
	-v ${PWD}/codeplug:/app/dzcb/codeplug \
	--entrypoint /app/dzcb/codeplug/generate_all.py \
	dzcb
