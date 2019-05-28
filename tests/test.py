from pyengine import Window, GameState, Entity, const, Controls, ControlType, StateCallbacks
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, MoveComponent, ControlComponent
from pyengine.Systems import EntitySystem
from pyengine.Utils import Colors


class Jeu:
    def __init__(self):
        # Création de la fenêtre de jeu de taille 800x400, de fond blanc et titre "Pong"
        self.window = Window(800, 400, Colors.WHITE.value)
        self.window.set_title("Pong")

        # Création et ajout de la GameState du jeu
        self.game = GameState("GAME")
        self.window.add_state(self.game)
        self.game.set_callback(StateCallbacks.OUTOFWINDOW, self.outofwindow)

        # Création de l'entité pour la barre du joueur à gauche avec :
        #  - Un PositionComponent avec les positions 10, 175
        #  - Un SpriteComponent avec le sprite texture.png que l'on redimensionne en 20, 50
        #  - Un ControlComponent avec un ControlType UPDOWN auquel on définit les touches à Z et S (azerty)
        #  - Un PhysicsComponent sans l'affection par la gravité
        self.j1 = Entity()
        self.j1.add_component(PositionComponent([10, 175]))
        spritej1 = self.j1.add_component(SpriteComponent("images/sprite0.png"))
        spritej1.set_size([20, 50])
        controlj1 = self.j1.add_component(ControlComponent(ControlType.UPDOWN))
        controlj1.set_control(Controls.UPJUMP, const.K_w)
        controlj1.set_control(Controls.DOWN, const.K_s)
        self.j1.add_component(PhysicsComponent(False))

        # Création de l'entité pour la barre du joueur à droite avec :
        #  - Un PositionComponent avec les positions 770, 175
        #  - Un SpriteComponent avec le sprite texture.png que l'on redimensionne en 20, 50
        #  - Un ControlComponent avec un ControlType UPDOWN auquel on définit les touches aux flèches haut et bas
        #  - Un PhysicsComponent sans l'affection par la gravité
        self.j2 = Entity()
        self.j2.add_component(PositionComponent([770, 175]))
        spritej2 = self.j2.add_component(SpriteComponent("images/sprite0.png"))
        spritej2.set_size([20, 50])
        controlj2 = self.j2.add_component(ControlComponent(ControlType.UPDOWN))
        controlj2.set_control(Controls.UPJUMP, const.K_UP)
        controlj2.set_control(Controls.DOWN, const.K_DOWN)
        self.j2.add_component(PhysicsComponent(False))

        # Création de l'entité pour la balle avec :
        #  - Un PositionComponent avec les positions 390, 190
        #  - Un SpriteComponent avec le sprite texture.png que l'on redimensionne en 20, 20
        #  - Un PhysicsComponent sans l'affection par la gravité dont on définit le callback de collision
        #  - Un MoveComponent avec comme direction 1, 1 (Haut droit)
        self.ball = Entity()
        self.ball.add_component(PositionComponent([390, 190]))
        spriteballe = self.ball.add_component(SpriteComponent("images/sprite0.png"))
        spriteballe.set_size([20, 20])
        physball = self.ball.add_component(PhysicsComponent(False))
        physball.set_callback(self.collision)
        self.ball.add_component(MoveComponent([1, 1]))

        # Ajout des entités au monde via l'EntitySystem
        entitysystem = self.game.get_system(EntitySystem)
        entitysystem.add_entity(self.j1)
        entitysystem.add_entity(self.j2)
        entitysystem.add_entity(self.ball)

        # Lancement du jeu
        self.window.run()

    # Callback de collision
    # Activé quand la balle rencontre un joueur (étant les seuls autre entités)
    def collision(self, obj, cause):
        # On récupère le MoveComponent de la balle pour inverser sa direction en x
        move = self.ball.get_component(MoveComponent)
        move.set_direction([-move.get_direction()[0], move.get_direction()[1]])

    # Callback OUTOFWINDOW
    # Activé quand un élément sort de l'écran
    def outofwindow(self, obj, pos):
        # Si notre objet est le joueur 1
        if obj == self.j1:
            # On récupère le PositionComponent du J1 pour le "bloquer" dans l'écran
            position = self.j1.get_component(PositionComponent)
            if pos[1] <= 0:
                position.set_position([10, 0])
            else:
                position.set_position([10, 350])

        # Si notre objet est le joueur 2
        elif obj == self.j2:
            # On récupère le PositionComponent du J2 pour le "bloquer" dans l'écran
            position = self.j2.get_component(PositionComponent)
            if pos[1] <= 0:
                position.set_position([770, 0])
            else:
                position.set_position([770, 350])

        # Si notre objet est la balle
        else:
            # Si la balle sort de l'écran sur les cotés
            if pos[0] < 10 or pos[0] > 790:
                # On replace la balle au centre
                position = self.ball.get_component(PositionComponent)
                position.set_position([390, 190])
            # Si la balle sort de l'écran par le haut
            else:
                # On inverse la direction y du movement de la base
                move = self.ball.get_component(MoveComponent)
                move.set_direction([move.get_direction()[0], -move.get_direction()[1]])


# Lancement du jeu
Jeu()