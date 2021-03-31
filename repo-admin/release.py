#!/usr/bin/env python3

import argparse
from datetime import date
from packaging import version
import os
import re
import subprocess


def filecontent(filepath):
    with open(filepath, "r") as file :
      return file.read()


def replace_content(filepath, filedata):
    with open(filepath, "w") as file:
      file.write(filedata)


def previous_version(content):
    matches = re.search("## \[(.+)] -", content)
    return version.Version(matches.group(1)) if matches else None


def comparison_url(previous, current=None):
    origin_remote = subprocess.check_output(["git", "remote", "get-url", "origin"]).decode('utf-8')
    match = re.search("git@github.com:(.+)\.git", origin_remote)
    if match is None:
        raise Exception("Remote '{}' does not have the expected format for a Github ssh url."
                            .format(origin_remote.rstrip(os.linesep)))
    base = match.group(1)
    current = "v{}".format(current) if current else "HEAD"
    if previous:
        return "https://github.com/{}/compare/v{}...{}".format(base, previous, current)
    elif current:
        return "https://github.com/{}/releases/tag/{}".format(base, current)
    else:
        raise Exception("Previous and current cannot both be 'None' at the same time")


def bump_changelog(v):
    filedata = filecontent("CHANGELOG.md")
    previous_v = previous_version(filedata)
    if previous_v and (v <= previous_v):
        raise Exception("Version numbers MUST increment")

    release_replacement = "## [Unreleased]\n\n## [{}] - {}".format(v, date.today())
    filedata = filedata.replace("## [Unreleased]", release_replacement)

    link_replacement = "[Unreleased]: {}\n[{}]: {}".format(comparison_url(v), v, comparison_url(previous_v, v))
    filedata = re.sub("^\[Unreleased]:.*$", link_replacement, filedata, flags=re.MULTILINE)

    replace_content("CHANGELOG.md", filedata)


def commit_and_tag(v, release_branch):
    subprocess.run(["git", "add", "CHANGELOG.md"], check=True)
    subprocess.run(["git", "commit", "-m", "Prepare release v{}".format(v)], check=True)
    subprocess.run(["git", "checkout", release_branch], check=True)
    subprocess.run(["git", "merge", "develop", "--no-ff", "--no-edit"], check=True)
    subprocess.run(["git", "tag", "-a", "v{}".format(v), "-m", "Release v{}".format(v)], check=True)
    subprocess.run(["git", "push", "--follow-tags"], check=True)
    subprocess.run(["git", "checkout", "develop"], check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepare a release by updating the changelog and commiting changes to current branch + tagging a new commit on the release branch.")
    parser.add_argument("version", help="The version to be released")
    parser.add_argument("releasebranch", help="The branch into which the releases are tagged")

    args = parser.parse_args()

    if subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True).stdout.decode('utf-8').rstrip() != "develop":
        print(subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True).stdout)
        raise Exception("Repository is not on develop branch")
    if subprocess.run(["git", "diff-index", "--quiet", "HEAD"]).returncode != 0:
        raise Exception("Repository has changes, please stash them first")

    v = version.Version(args.version)
    bump_changelog(v)
    commit_and_tag(v, args.releasebranch)
