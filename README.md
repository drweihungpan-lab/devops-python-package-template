### About

> **Course template.** `course_template/` is the version used in the 3R course: Python 3.12, a `device_limit` command-line tool (`--input`, `--output`), lint CI active, the pytest and semantic-release jobs commented out, and no AWS steps. Generate it with `cookiecutter course_template/`, or check it with `make test-course-template`.

This repository provides templates for setting up a Python development environment. Users have the option to choose from two templates: 
1. **Python Application Repository**: Contains setup for a Python application, including a Dockerfile and docker-related build steps.
2. **Python Library Repository**: A standard setup for developing a Python library.

### Prerequisites

Ensure `cookiecutter` is installed. If not, it can be installed within a virtual environment using:

```bash
pip install cookiecutter
```

### Usage

1. **Create a New Repository**:
   Set up a new repository on your organization's GitHub account. Instructions can be found in [the docs](https://github.com/your-org/your-repo-docs).

2. **Clone the New Repository**:
   Clone the new repository that you just created.

3. **Clone the Template Repository**:
   Clone the `devops-python-package-template` repository (this repo).

3. **Apply template to New Repository**:
   Use `cookiecutter` to generate the new project structure:

   ```bash
   cookiecutter -f /path/to/devops-python-package-template/package_template/
   ```

   During this process, you'll be prompted to provide values for several variables. If a value is not provided, `cookiecutter` will use the default value shown in brackets:
   Make sure to that `<your-repo-name>` matches the name of the new repository that you cloned earlier.

   ```bash
   [1/6] package_name (example): <your-package-name>
   [2/6] module_name (demo_module): <your-module-name>
   [3/6] repo_name (): <your-repo-name>
   [4/6] author (Jane Doe): <your-name>
   [5/6] author_email (jane.doe@example.com): <your-email>
   [6/6] Select project_type:
       1 - application
       2 - library
   Choose from [1/2] (1): 2
   ```

4. **Push the Repository to GitHub**:
   
   Navigate to the newly created template repo and run the following commands.
   ```bash
   git checkout <your-branch-name>
   git add .
   git commit -m 'Initial Commit'
   git remote add origin git@github.com:your-org/<your-repo-name>.git
   git push --set-upstream origin <your-branch-name>
   ```
   Replace `<your-repo-name>` with the name of the repo created in the earlier step:

 
### Guide to Using `python-semantic-release` with Commit Conventions

`python-semantic-release` automates the versioning and package release process based on the semantics of your commit messages. To make effective use of this tool, it's important to understand how to structure your commits for patches, minor changes, and major changes.


#### Commit Conventions

To ensure `python-semantic-release` correctly bumps versions, you need to structure your commit messages according to the Conventional Commits specification.

Prefixes in commit messages provide clear and consistent categorization of changes, enabling automated tools to determine versioning and changelogs accurately.

##### No-bump Prefixes
Prefixes that Typically Don't Trigger a Version Bump:
* `chore:`: Routine tasks or maintenance chores.
* `docs:`: Documentation changes, unless they're part of the published package/module.
* `style:`: Code style changes, like formatting.
* `test:`: Changes exclusively in tests, unless they're part of the published package/module.
* `refactor:`: Code changes that neither fix a bug nor add a feature. Even though refactoring might involve significant codebase changes, it doesn't introduce new features from an end-user's perspective.
* `build:`: Changes affecting the build system or external dependencies.
* `ci:`: Adjustments to the Continuous Integration configuration or scripts.
* `revert:`: Reverting a previous commit. The version bump is determined by the nature and impact of the reverted commit.

##### Patches (Bug Fixes)

For patches or bug fixes, use the `fix` prefix:

```bash
git commit -m "fix: corrected typo in user interface"
```

This will result in a patch version bump (e.g., `1.0.0` -> `1.0.1`).

Prefixes that Trigger a Patch Bump:

* `fix:`: Bug fixes typically result in a patch version bump.
* `perf:`: Performance improvements can result in a patch version bump if they don't introduce new features.

##### Minor Changes (New Features)

For new features that are backward-compatible, use the `feat` prefix:

```bash
git commit -m "feat: added dark mode support"
```

This will lead to a minor version bump (e.g., `1.0.0` -> `1.1.0`).


##### Major Changes (Breaking Changes)

For breaking changes, you need to include a prefix in the commit title and you need to include `BREAKING CHANGE:` in the commit message body. To provide both a title and a body in the commit message from the command line, you can use the `-m` flag twice:

###### Using CLI:
```bash
git commit -m "feat: revised authentication flow" -m "BREAKING CHANGE: new authentication method, old method deprecated"
```


The first `-m` provides the title (or header) of the commit, and the second `-m` provides the body, detailing the breaking change. This structure ensures that tools following the Conventional Commits specification can correctly detect and process the breaking change.

This will trigger a major version bump (e.g., `1.0.0` -> `2.0.0`).

It is worth noting that any commit can introduce a breaking change, and if it does (indicated by the BREAKING CHANGE: notation in the commit body), it will always trigger a major version bump, regardless of the prefix used, as long as there is a prefix in the title.

###### Using text editor:
***Before:***

When you first open the text editor after executing `git commit`, you might see:

```plaintext
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch [YOUR-BRANCH-NAME]
# Your branch is up to date with 'origin/[YOUR-BRANCH-NAME]'.
#
# Changes to be committed:
#	[LIST OF CHANGED FILES]
#
```

***After:***

After entering your commit message:

```plaintext
[PREFIX]: [SHORT DESCRIPTION]

[DETAILED DESCRIPTION]
BREAKING CHANGE: [BREAKING CHANGE DETAILS]

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch [YOUR-BRANCH-NAME]
# Your branch is up to date with 'origin/[YOUR-BRANCH-NAME]'.
#
# Changes to be committed:
#	[LIST OF CHANGED FILES]
#
```

- **[PREFIX]**: This is where you'd put `feat`, `fix`, `chore`, etc.
- **[SHORT DESCRIPTION]**: A concise summary of the change.
- **[DETAILED DESCRIPTION]**: An optional, more in-depth explanation of the change.
- **[BREAKING CHANGE DETAILS]**: A description of what makes this change a breaking one.

Remember to replace the placeholders (`[...]`) with your actual content. After entering your message, save and exit the editor to complete the commit.

#### Best Practices

- **Consistency**: Everyone should understand and follow the commit conventions. This ensures the automatic versioning works as expected.
- **Descriptive Messages**: While the commit type (e.g., `feat`, `fix`) is important for versioning, a descriptive message helps maintainers and other team members understand the change's purpose.
- **Understand Commit Structure**: Remember that using two `-m` flags allows you to provide both a title and a detailed body for the commit, ensuring clarity and adherence to conventions.

By following these conventions and practices, you can automate the versioning and release process, ensuring that the version numbers accurately reflect the nature of the changes in the codebase, and that the changelog is populated accordingly.
