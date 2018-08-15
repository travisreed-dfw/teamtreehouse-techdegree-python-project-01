import csv

# Teams are created with zero players and strings for team names
dragons = [0, 0, 'Dragons']
sharks = [0, 0, 'Sharks']
raptors = [0, 0, 'Raptors']
league_of_teams = [dragons, sharks, raptors]    # Oh my!


# Define function for assigning players to teams, with an even amount of exp
def assign_player(player):
    for team in league_of_teams:
        if player['Soccer Experience'] == 'YES':
            if team[0] < 3:
                team.append(player)
                team[0] += 1
                return
        else:
            if team[1] < 3:
                team.append(player)
                team[1] += 1
                return


# Use Dunder Name so that it only runs if the file is root
if __name__ == "__main__":
    # Open CSV file of players and assign each one to a team
    with open('soccer_players.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            assign_player(row)
    # loop through teams to create parent letters and team file
    for team in league_of_teams:
        team_name = team[2]
        team = team[3:]
        # create parent letter for each player's parent
        for player in team:
            file_name = player['Name'].split(" ")[0].lower() + "_" + \
                        player['Name'].split(" ")[1].lower() + ".txt"
            with open(file_name, "a") as file:
                file.write(
                        "Dear " + player[
                            'Guardian Name(s)'] + ":" + '\n' + '\n' +
                        "Welcome to a new season of soccer! \n"
                        "Your player " +
                        player['Name'] + " has been assigned to the " +
                        team_name + " team. \n"
                                    "The first practice is on July 9th "
                                    "at 6:00pm Central Time! See you then! "
                        )
        # Create file of teams.txt
        with open("teams.txt", "a") as file:
            file.write(team_name + "\n")
            for player in team:
                file.write(player['Name'] + ", " + player[
                    'Soccer Experience'] + ", " + player[
                               'Guardian Name(s)'] + '\n')
            file.write("\n")
