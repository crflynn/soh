.PHONY: fmt
fmt:
	cargo fmt
	cargo clippy

.PHONY: release
release:
	sh bin/release.sh

.PHONY: setup
setup:
	brew install asdf || True
	asdf install
	rustup component add rustfmt
	rustup component add clippy

.PHONY: soh
soh: fmt
	cargo build
