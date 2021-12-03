import requests
import sys
if __name__ == '__main__':
    if str(sys.argv[1]) == "-r":
        (group, project) = ( str(sys.argv[2]).split('/')[0], str(sys.argv[2]).split('/')[1])
        repository_url = "http://{}.github.io/{}/".format(group, project)
    else:
        repository_url = str(sys.argv[1])
    data = requests.get(repository_url)
    if data.status_code == 404:
        print("[!] The GitHub Pages site", repository_url, "is not reachable")
        print("    Possible reasons include:")
        print("    - GitHub Pages are not enabled for the repository: check the repository settings")
        print("    - GitHub Pages are enabled but the 'gh-pages' branch is not selected or does not exist: check the repository settings and the content of the intended branch")
        print("    - GitHub Pages are correctly configured but the branch does not contain an 'index.html' file: build the site locally and check that the index is correctly generated and make sure that the content of the 'gh-pages' branch is up-to-date")
        sys.exit(1)
    else:
        print("[*] The GitHub Pages site", repository_url, "is reachable")
