# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- A naming convention for CMake packages and their components.
- Warning message if calling find_package() for a component within a CMake package
with exactly matching names.

### Changed
- A, B and C CMake targets are renamed alpha, beta and gamma respectively.
- Conan installer for CMake uses updated "Conan Center" reference (without `@conan/stable` suffix).

### Fixed
- Instruction to use `ARCH_INDEPENDENT` when producing a CMake version file for `INTERFACE`  targets.

## [0.7.4] - 2021-03-04
### Fixed
- ComponentPackageRootConfig.cmake uses a package name with capitalization
matching capitalization in find_package() invocation.
- Conan test package cpp source explicitly returns success from main function.
- Conan recipe revision is computed from commit ID instead of recipe hash,
because recipe hash is sensitive to line-endings.

## [0.7.3] - 2021-02-24
### Fixed
- Clarify the text in different locations after proofreading.
- Fix a few typos.

## [0.7.2] - 2021-02-17
### Added
- A changelog following [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) convention.
- Automate release and Github page publication, based on Github Actions.
- A script to pepare and trigger the release+publish process (repo-admin/release.py).

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

[Unreleased]: https://github.com/Adnn/ModernCppComponent/compare/v0.7.4...HEAD
[0.7.4]: https://github.com/Adnn/ModernCppComponent/compare/v0.7.3...v0.7.4
[0.7.3]: https://github.com/Adnn/ModernCppComponent/compare/v0.7.2...v0.7.3
[0.7.2]: https://github.com/Adnn/ModernCppComponent/compare/v0.7.1...v0.7.2
[0.7.1]: https://github.com/Adnn/ModernCppComponent/compare/v0.7.0...v0.7.1
[0.7.0]: https://github.com/Adnn/ModernCppComponent/releases/tag/v0.7.0
