# PyEngine

A lib to build 2D Games.

## Dependencies

- Python 3.5+
- PyGame

## Other information

- Main Developer : LavaPower
- Contributors : X
- Develop on :
  - System :
    - Windows 10 (V 0.1.0-DEV --> Latest)
  - Version of Python :
    - 3.7.1 (V 0.1.0-DEV --> Latest)
  - Library :
    - PyGame (V 0.1.0-DEV --> Latest)

## Known bugs of the developing version

- X

## Changelog

### V 1.1.0 : General Update - 25/05/19

    - LifeComponent : Remove creation of sprite
    - LifeComponent : Add get_life and get_maxlife functions
    - Entity : Add get_system function
    - World : Remove world
    - Enums : Move Enums in classes
    - EntitySystem : Add function to remove entity
    - UISystem : Add function to remove widget
    - SoundSystem : Create
    - Widgets : You can hide and show widgets
    - Entry : You can use your own background
    - Color-Colors : Create color class and colors enums
    - Font : Create font class
    - Optimisation of lib
    
    - Bug Fix : Rotation of SpriteComponent don't work

### V 1.0.2 : Fix Update 2 - 11/05/19

    - Entity : Can get custom component
    - Setup : Fix crash when pygame is not installed
    - Setup : Don't get PyGame2
    
Cette MAJ ne casse pas la combatilbilité avec la précédente.

### V 1.0.1 : Fix Update - 10/05/19

    - Enums : Add Controls in __all__
    - Entity : Can add custom component
    
Cette MAJ ne casse pas la combatilbilité avec la précédente.

### V 1.0.0 : First Update - 09/05/19

    - Components : Create LifeBarComponent, MoveComponent
    - Components : Rework on system (Work with constructor)
    - World-Enums : Create WorldCallbacks (OUTOFWINDOW)
    - Components/SpriteComponent : Add set_size function
    - Components/PhysicsComponent-Enums : Add CollisionCauses in CollisionCallback
    - Components/PhysicsComponent : Add gravity management
    - Components/ControlComponent : Add speed management
    - Components/ControlComponent : Add controls management
    - Components/ControlComponent-Enums : Add LEFTRIGHT and UPDOWN ControlType
    - Components/ControlComponent-Enums : Add Controls Enums
    - GameState-Window-World : Create GameState System
    - Systems/UISystem : Create Wigets System
    - Widgets : Create Label, Image, Button, Entry widget
    - Window : Add title and background color management
    - Exceptions : Rework on system (rename and remove useless exceptions

### V 0.2.0-DEV : Little Update - 25/04/19

    - Components/PhysicsComponent : Collision Callback return object
    - Systems/EntitySystem : Remove condition to add entity
    - Window : Add a function to end game
    - Setup.py : Add dependances (PyGame)

### V 0.1.0-DEV : Initial Update - 19/04/19

    - First Version