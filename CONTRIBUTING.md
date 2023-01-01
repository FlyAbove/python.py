# Contributing
This document describes how you can contribute to python.py. Please read it carefully.

**Table of Contents**

* [How to Contribute to the Project](#how-to-contribute-to-the-project)
* [How to get your Pull Request Accepted](#how-to-get-your-pr-accepted)

## How to Contribute to the project

There are a couple of ways on how you can contribute to the project:

* File [issues](https://github.com/FlyAbove/python.py/issues/new/choose) for missing content or specifically for the binaries here
* Create a [pull request](https://github.com/FlyAbove/python.py/pulls "Create a pull request"). This is a direct contribution to the project and may be merged after review. You should ideally [create an issue](https://github.com/FlyAbove/python.py/issues/new/choose "python.py Issues") for any pull request you would like to submit, as we can first review the merit of the PR and avoid any unnecessary work. This is of course not needed for small modifications such as correcting typos.
* Promote us by giving us a Star or share information via social media.

## How to get your Pull Request accepted

Your PR is valuable to us, and to make sure we can integrate it smoothly, we have a few items for you to consider. In short:
The minimum requirements for code contributions are:

1. The code _must_ be compliant with the configured best practices for the language.
2. All new and changed code _should_ have a corresponding unit and/or integration test.

Additionally, the following guidelines can help:

### Keep your pull requests limited to a single issue

Pull requests should be as small/atomic as possible. Large, wide-sweeping changes in a pull request will be **rejected**, with comments to isolate the specific code in your pull request. Some examples:

* If you are making spelling corrections in the docs, don't modify other files.
* If you are adding new functions don't '_cleanup_' unrelated functions. That cleanup belongs in another pull request.

### Write a good commit message

* Explain why you make the changes. [More infos about a good commit message.](https://betterprogramming.pub/stop-writing-bad-commit-messages-8df79517177d)

* If you fix an issue with your commit, please close the issue by [adding one of the keywords and the issue number](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) to your commit message.

  For example: `Fix #545` or `Closes #10`

## What not to do

Although we greatly appreciate any and all contributions to the project, there are a few things that you should take into consideration:

* The Wrongsecrets project should not be used as a platform for advertisement for commercial tools, companies or individuals. Write-ups should be written with free and open-source tools in mind and commercial tools are typically not accepted, unless as a reference in the security tools section.
* Unnecessary self-promotion of tools or blog posts is frowned upon. If you have a relation with on of the URLs or tools you are referencing, please state so in the PR so that we can verify that the reference is in line with the rest of the guide.

Please be sure to take a careful look at our [Code of Conduct](https://github.com/FlyAbove/python.py/blob/main/CODE_OF_CONDUCT.md)
