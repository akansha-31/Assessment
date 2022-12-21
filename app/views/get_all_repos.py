from github import Github

def get_all_repos(request):
    github = Github('akansha-31', 'Siroliya@123')
    organization = github.get_organization('coindcx-official')

    repos = []
    for repo in organization.get_repos():
        repos.append(repo)
    return repos
