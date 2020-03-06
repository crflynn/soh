export DIST_FOLDER=.dist
export WORKFLOWS_JSON=$(DIST_FOLDER)/workflows.json
export ARTIFACTS_JSON=$(DIST_FOLDER)/artifacts.json

.PHONY: release
release:
	mkdir -p $(DIST_FOLDER)
	curl "https://api.github.com/repos/crflynn/soh/actions/workflows/ci.yml/runs?branch=master" > $(WORKFLOWS_JSON)
	curl $$(jq '.workflow_runs' $(WORKFLOWS_JSON) | jq '.[0]' | jq -r '.artifacts_url') > $(ARTIFACTS_JSON)
	@curl -H "Authorization: token $(GITHUB_TOKEN)" $$(< $(ARTIFACTS_JSON) jq '.artifacts' | jq '.[0]' | jq -r '.archive_download_url') -L > "$(DIST_FOLDER)/$$(jq '.artifacts' $(ARTIFACTS_JSON) | jq '.[0]' | jq -r '.name').zip"
	@curl -H "Authorization: token $(GITHUB_TOKEN)" $$(< $(ARTIFACTS_JSON) jq '.artifacts' | jq '.[1]' | jq -r '.archive_download_url') -L > "$(DIST_FOLDER)/$$(jq '.artifacts' $(ARTIFACTS_JSON) | jq '.[1]' | jq -r '.name').zip"
	rm $(WORKFLOWS_JSON)
	rm $(ARTIFACTS_JSON)
	ghr -u crflynn -r soh -c $$(git rev-parse HEAD) -delete $$(cargo metadata --no-deps | jq '.packages' | jq '.[0]' | jq -r '.version') "$(DIST_FOLDER)"
