all:
	./_update_rest_api.py

.PHONY: all test

test-asciidoc-source:
	./scripts/check-asciidoctor-build.sh

test-portal-build:
	./scripts/get-updated-distros.sh && \
	while read -r filename; do \
		if [ "$$filename" = "_topic_maps/_topic_map.yml" ]; then \
			python3 build.py --distro openshift-enterprise --product "OpenShift Container Platform" --version 4.14 --no-upstream-fetch; \
		elif [ "$$filename" = "_topic_maps/_topic_map_osd.yml" ]; then \
			python3 build.py --distro openshift-dedicated --product "OpenShift Dedicated" --version 4 --no-upstream-fetch; \
		elif [ "$$filename" = "_topic_maps/_topic_map_ms.yml" ]; then \
			python3 build.py --distro microshift --product "Microshift" --version 4 --no-upstream-fetch; \
		elif [ "$$filename" = "_topic_maps/_topic_map_rosa.yml" ]; then \
			python3 build.py --distro openshift-rosa --product "Red Hat OpenShift Service on AWS" --version 4 --no-upstream-fetch; \
		elif [ "$$filename" = "_distro_map.yml" ]; then \
			python3 build.py --distro openshift-enterprise --product "OpenShift Container Platform" --version 4.14 --no-upstream-fetch; \
		fi; \
	done
	if [ -d "drupal-build" ]; then \
		python3 makeBuild.py; \
	fi

push-netlify:
	./autopreview.sh