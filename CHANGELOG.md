# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.7.2] - 2021-02-17
### Added
- A changelog following [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) convention.
- Automate release and Github page publication, based on Github Actions.
- A script to pepare and trigger the release+publish process (repo-admin/release.py)

### Fixed
- Fix Conan test_package executable location for multi-config generators
(made uniform with single-config generators).

## [0.7.1] - 2020-01-15
### Fixed
- Make the message clearer that it is not an ideal process, and provide some context.
- Fix minor issues with the inline CMake and Conan code samples.

### Changed
- Prefer the notion of correlation over the notion of orthogonality.

## [0.7.0] - 2020-01-09
### Added
- Initial release of the document

[Unreleased]: https://github.com/Adnn/ModernCppComponent/compare/v0.7.2...HEAD
[0.7.2]: https://github.com/Adnn/ModernCppComponent/compare/v0.7.1...v0.7.2
[0.7.1]: https://github.com/Adnn/ModernCppComponent/compare/v0.7.0...v0.7.1
[0.7.0]: https://github.com/Adnn/ModernCppComponent/releases/tag/v0.7.0
