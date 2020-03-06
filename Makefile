VERSION=$(shell cargo metadata --format-version 1 --no-deps | jq '.packages' | jq '.[0]' | jq -r '.version')
DIST_FOLDER=.dist/$(VERSION)
WORKFLOWS_JSON=$(DIST_FOLDER)/workflows.json
ARTIFACTS_JSON=$(DIST_FOLDER)/artifacts.json
MAC_ARTIFACT=x86_64-apple-darwin
LINUX_ARTIFACT=x86_64-unknown-linux-musl
COMMIT=$(shell git rev-parse HEAD)

.PHONY: release
release:
	rm -rf $(DIST_FOLDER)
	mkdir -p $(DIST_FOLDER)
	@curl -H "Authorization: token $(GITHUB_TOKEN)" "https://api.github.com/repos/crflynn/soh/actions/workflows/ci.yml/runs?branch=master" > $(WORKFLOWS_JSON)
	@curl -H "Authorization: token $(GITHUB_TOKEN)" $$(jq '.workflow_runs' $(WORKFLOWS_JSON) | jq '.[0]' | jq -r '.artifacts_url') > $(ARTIFACTS_JSON)
	@curl -H "Authorization: token $(GITHUB_TOKEN)" $$(< $(ARTIFACTS_JSON) jq '.artifacts' | jq '.[0]' | jq -r '.archive_download_url') -L > "$(DIST_FOLDER)/$$(jq '.artifacts' $(ARTIFACTS_JSON) | jq '.[0]' | jq -r '.name').zip"
	@curl -H "Authorization: token $(GITHUB_TOKEN)" $$(< $(ARTIFACTS_JSON) jq '.artifacts' | jq '.[1]' | jq -r '.archive_download_url') -L > "$(DIST_FOLDER)/$$(jq '.artifacts' $(ARTIFACTS_JSON) | jq '.[1]' | jq -r '.name').zip"
	rm $(WORKFLOWS_JSON)
	rm $(ARTIFACTS_JSON)
	mv $(DIST_FOLDER)/$(MAC_ARTIFACT).zip $(DIST_FOLDER)/soh-$(VERSION)-$(MAC_ARTIFACT).zip
	mv $(DIST_FOLDER)/$(LINUX_ARTIFACT).zip $(DIST_FOLDER)/soh-$(VERSION)-$(LINUX_ARTIFACT).zip
	ghr -u crflynn -r soh -c $(COMMIT) -delete $(VERSION) "$(DIST_FOLDER)"
	echo $(VERSION)
	@sha256sum $(DIST_FOLDER)/soh-$(VERSION)-$(MAC_ARTIFACT).zip
	@sha256sum $(DIST_FOLDER)/soh-$(VERSION)-$(LINUX_ARTIFACT).zip
