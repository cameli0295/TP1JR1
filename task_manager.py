# Gestionnaire de tâches en Python

tasks = []  # Liste vide de tâches

while True:
    print("\nChoisissez une action :")
    print("1. Afficher les tâches")
    print("2. Ajouter une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Quitter")

    choice = input("> ")

    if choice == '1':
        print("Liste des tâches : ", tasks)
    elif choice == '2':
        task = input("Entrez une nouvelle tâche : ")
        tasks.append(task)
        print("Tâche ajoutée.")
    elif choice == '3':
        print("Fonction non implémentée.")
    elif choice == '4':
        break
    else:
        print("Choix invalide.")


def show_tasks():
    if not tasks:
        print("La liste des tâches est vide.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


if choice == '1':
    show_tasks()
