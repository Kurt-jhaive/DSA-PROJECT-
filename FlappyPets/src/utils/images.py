import random
from typing import List, Tuple

import pygame

from .constants import BACKGROUNDS, PIPES, PLAYERS


class Images:
    numbers: List[pygame.Surface]
    game_over: pygame.Surface
    welcome_message: pygame.Surface
    base: pygame.Surface
    background: pygame.Surface
    player: Tuple[pygame.Surface]
    pipe: Tuple[pygame.Surface]

    def __init__(self) -> None:
        self.numbers = list(
            (
                pygame.image.load(f"FlappyPets/assets/sprites/{num}.png").convert_alpha()
                for num in range(10)
            )
        )

        # game over sprite
        self.game_over = pygame.image.load(
            "FlappyPets/assets/sprites/gameover.png"
        ).convert_alpha()

        # welcome_message sprite for welcome screen
        # randomize between cat and dog
        # self.random_player_message = random.randint(0, 1)    
        with open("FlappyPets/current_pet.txt", "r") as f:
            self.random_player_message = int(f.read())
        if self.random_player_message == 0:
            self.welcome_message = pygame.image.load(
                "FlappyPets/assets/sprites/dog-message.png"
            ).convert_alpha()
            #change current pet to cat
            with open("FlappyPets/current_pet.txt", "w") as f:
                f.write("1")
        else:
            self.welcome_message = pygame.image.load(
                "FlappyPets/assets/sprites/cat-message.png"
            ).convert_alpha()
            #change current pet to dog
            with open("FlappyPets/current_pet.txt", "w") as f:
                f.write("0")

        # base (ground) sprite
        self.base = pygame.image.load("FlappyPets/assets/sprites/base.png").convert_alpha()
        self.randomize()

    def randomize(self):
        # select random background sprites
        rand_bg = random.randint(0, len(BACKGROUNDS) - 1)
        # select random pipe sprites
        rand_pipe = random.randint(0, len(PIPES) - 1)

        self.background = pygame.image.load(BACKGROUNDS[rand_bg]).convert()
        self.player = (
            pygame.image.load(PLAYERS[self.random_player_message][0]).convert_alpha(),
            pygame.image.load(PLAYERS[self.random_player_message][1]).convert_alpha(),
            pygame.image.load(PLAYERS[self.random_player_message][2]).convert_alpha(),
        )
        self.pipe = (
            pygame.transform.flip(
                pygame.image.load(PIPES[rand_pipe]).convert_alpha(),
                False,
                True,
            ),
            pygame.image.load(PIPES[rand_pipe]).convert_alpha(),
        )
