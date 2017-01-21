from argparse import ArgumentParser
from git import Repo, Git
import dtf.core.manifestparser as mp

parser = ArgumentParser(description='Bundle several repos to dtf export.')

parser.add_argument('repo_file_name', metavar="repo_file_name", type=str,
                    help='The file to pull repo data from.')
parser.add_argument('--tag', dest='tag', default=None,
                    help='The tag/branch to work off.')
parser.add_argument('--latest', dest='latest',
                    action='store_const', const=True, default=False,
                    help="Pull latest tag.")

args = parser.parse_args()

file_name = args.repo_file_name
tag = args.tag

export_zip = mp.ExportZip("export.zip")

for line in open(file_name).read().split("\n"):

    if line == "": continue

    repo_dir, git_url = line.split("|")

    print "Cloning %s to %s..." % (git_url, repo_dir)

    repo = Repo.clone_from(git_url, repo_dir)

    if tag:
        print "Checking out branch: %s, %s" % (tag, repo_dir)
        g = Git(repo_dir)
        g.checkout(tag)
    elif latest:
        print "Checking out latest tag: %s, %s" % (latest, repo_dir)
        latest = repo.tags[-1]
        g = Git(repo_dir)
        g.checkout(latest)

    print "Parsing manifest.xml.."
    manifest_name = "%s/manifest.xml" % repo_dir
    manifest = mp.parse_manifest_file(manifest_name)

    if manifest is None:
        print "Something went wrong!"
        continue

    for item in manifest.items:

        export_zip.add_item(item)

    print "All items added for: %s" % repo_dir

print "Finalizing ZIP..."
export_zip.finalize()

print "Done!"
