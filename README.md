Automated Content Bundler (bundler.py)
======================================
This script is responsible for generation of the core content ZIP. If you're not developing content, this utility probably does not interest you.

Usage
-----
### Step 1: Create Content
First, create your content (module, library, whatever). Place it in a Git repo along with a `manifest.xml` that describes your content.

### Step 2: Create Tags (Optional)
If you care about versioning, create a tag/release for the version (such as v1.0.1). You can use the `--latest` argument to pull the latest tag.

### Step 3: Run bundler.py on your Server
Finally, run the `bundler.py` script on your server. You can use `cron` if you'd like create nightly builds.

File Format
-----------
Your file that contains repo data should be a pipe (|) delimited file, with either 2 or 3 elements:

```
repo_name|repo_url|<option_tag_or_branch>
```
