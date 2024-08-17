import requests

# Remplacez par votre jeton d'accès personnel GitHub
token = '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'
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

# Création du dépôt GitHub
repo_name = 'ExamenFinal_OutilsVersioning'
data = {
    'name': repo_name,
    'description': 'Ce repo contient tous les elements de l\'evaluation finale d\'Outils Versioning ',
    'private': False,  # Définir sur True pour un dépôt privé
}
response = requests.post('https://api.github.com/user/repos', headers=headers, json=data)
if response.status_code == 201:
    print(f'Dépôt {repo_name} créé avec succès.')
else:
    print(f'Erreur lors de la création du dépôt: {response.status_code}')
    print(response.json())

# Ajout de deux tickets
repo_owner = 'kountak'
issues = [
    {'title': 'Ticket 1', 'body': 'Description du premier ticket'},
    {'title': 'Ticket 2', 'body': 'Description du deuxième ticket'}
]

for issue in issues:
    issue_response = requests.post(f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues', headers=headers, json=issue)
    if issue_response.status_code == 201:
        print(f'Ticket "{issue["title"]}" créé avec succès.')
    else:
        print(f'Erreur lors de la création du ticket: {issue_response.status_code}')
        print(issue_response.json())
