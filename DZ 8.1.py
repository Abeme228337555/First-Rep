import logging
import random
logging.basicConfig(level=logging.DEBUG,
                    filename='logs_example.log',
                    filemode='w',
                    format='NEW LOG - %(asctime)s - %(levelname)s: %(message)s')

class Beaver:
    def __init__(self, name="Beaver", job=None, home=None, board=None):
        self.name = name
        self.job = job
        self.home = home
        self.board = board
        self.reputation = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()

    def get_board(self):
        self.board = Board(materials_of_boardlist)

    def get_job(self):
        if self.board.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.searching("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.board.drive():
            pass
        else:
            if self.board.durability < 20:
                self.searching("durability")
                return
            else:
                self.to_repair()
                return
        self.reputation += self.job.gettingrespect
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def searching(self, manage):
        if self.board.drive():
            pass
        else:
            self.to_repair()
            return
        if manage == "durability":
            print("I searched board with more durability")
            self.reputation -= 100
            self.board.durability += 100
        elif manage == "food":
            print("I searched food")
            self.reputation -= 50
            self.home.food += 50
        elif manage == "berries":
            print("Yummy yummy!")
            self.reputation -= 15
            self.satiety += 2
            self.gladness += 10

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.board.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name} 's life "
        print(f"{day:=^50}", "\n")
        beaver_indexes = self.name + "'s indexes"
        print(f"{beaver_indexes:^50}", "\n")
        print(f"Reputation – {self.reputation}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        board_indexes = f"{self.board.materials_of_boardlist} board indexes"
        print(f"{board_indexes:^50}", "\n")
        print(f"Durability – {self.board.durability}")
        print(f"Strength – {self.board.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            logging.critical('depression')
            return False
        if self.satiety < 0:
            print("Dead…")
            logging.critical('dead')
            return False
        if self.reputation < -500:
            print("Lox")
            logging.critical('lox')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False

        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.board is None:
            self.get_board()
            print(f"I bought a board {self.board.materials_of_boardlist}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with gettingrespect {self.job.gettingrespect}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\n So I will clean the house ")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.reputation < 0:
            print("Start working")
            self.work()
        elif self.board.strength < 15:
            print("I need to repair my board")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.searching(manage="berries")


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


materials_of_boardlist = {
    "Wood": {"durability": 100, "strength": 100, "consumption": 6},
    "Metal": {"durability": 50, "strength": 40, "consumption": 10},
    "Plastic": {"durability": 70, "strength": 150, "consumption": 8},
    "Rubber": {"durability": 80, "strength": 120, "consumption": 14}

}


class Board:
    def __init__(self, materials_of_boardlist):
        self.materials_of_boardlist = random.choice(list(materials_of_boardlist))
        self.durability = materials_of_boardlist[self.materials_of_boardlist]["durability"]
        self.strength = materials_of_boardlist[self.materials_of_boardlist]["strength"]
        self.consumption = materials_of_boardlist[self.materials_of_boardlist]["consumption"]

    def drive(self):
        if self.strength > 0 and self.durability >= self.consumption:
            self.durability -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The board has broken")
            return False


job_list = {
    "Dam buider": {"gettingrespect": 50, "gladness_less": 10},
    "Food searcher": {"gettingrespect": 40, "gladness_less": 3},
    "Warrior": {"gettingrespect": 45, "gladness_less": 25},
    "Main Beaver": {"gettingrespect": 70, "gladness_less": 1}
}


class Job:
    def __init__(self, list_of_jobs):
        self.job = random.choice(list(list_of_jobs))
        self.gettingrespect = list_of_jobs[self.job]["gettingrespect"]
        self.gladness_less = list_of_jobs[self.job]["gladness_less"]


nick = Beaver(name="nick")

for day in range(1, 8):
    if nick.live(day) == False:
        break
