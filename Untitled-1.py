
class Player:
    def __init__(self, jersey_number, name ,goals_scored):
        self.jersey_number = jersey_number, 
        self.name = name
        self.goals_scored = goals_scored
        self.category = self.categorize_player()

    def categorize_player(self):
        
        if self.goals_scored >= 100:
            return "Star"
        elif self.goals_scored >= 50:
            return "Regular"
        else:
            return "Beginner"

    def display(self):
        
        print(f"ID: {self.jersey_number} | Position: {self.name}")
        print(f"Matches: Goals: {self.goals_scored} | Category: {self.category}")
        print("-" * 55)

    def __str__(self):
        
        return (f"Player[{self.jersey_number} - "
                f"{self.category} | Matches:Goals{self.goals_scored}")


class Club:
    def __init__(self, club_name):
        self.club_name = club_name
        self.players = []

    def add_player(self, player):
       
        if isinstance(player, Player):
            self.players.append(player)
            print(f"Added {player.name} ({player.category}) to {self.club_name}.")
        else:
            print("Error: Invalid player record.")

    def display_all_players(self):
    
        print(f"\n{'=' * 55}")
        print(f" {self.club_name.upper()} - TEAM ROSTER")
        print(f"{'=' * 55}")
        
        if not self.players:
            print("No players currently registered in the club.")
            return

        for player in self.players:
            player.display()


if __name__ == "__main__":
   
    my_club = Club("Mumbai City FC")

    p1 = Player(101, "Sunil Chhetri", 85)
    p2 = Player(102, "Lallianzuala Chhangte", 30)
    p3 = Player(103, "vaibhav suryavanshi",129)
    my_club.add_player(p1)
    my_club.add_player(p2)
    my_club.add_player(p3)
    print("\nString Representation Check:")
    print(p1)

    my_club.display_all_players()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
