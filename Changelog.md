# Changelog

## V 1.3.0 : XXX Update - XX/XX/19

    - Window : Add is_running function
    - loggers : Create logging System
    - Lang : Create translate system
    - Config : Create Config system
    - Entity : Can't have the same type of component two times
    
    - Crash Fix : Crash when show id of Entity Texts

## V 1.2.0 : Property Update - 09/06/19

    - All : Use property decorator
	- All : Add annotation on function will be used by users
    - Window : Modify management of Worlds
    - Window : Created in middle of the screen
	- Window : Can modify size
    - GameState : Rename to World
	- World : Remove has system function
	- Entity-Exception : Replace WrongObjectError to TypeError
	- Entity : Can remove component
    - CameraSystem : Create basic camera
	- MoveComponent : Remove speed
	- TextComponent : Add background color
	- TextComponent : Add scale
	- TextComponent : Add rendered_size
	- Label : Add background color
	- Button : Add white filter when it is hovered
	- Button : Can change image
	- Vec2 : Create vector 2
	- Color : Can be add, substact and compared
	- Font : Can be compared
	- Unit Tests : Create
	
	- Bug Fix : Entity Text is not updated
	- Bug Fix : Entity Text is not count in get_entity
	- Bug Fix : MusicSystem return wrong volume
	- Bug Fix : Window return wrong title
	
	- Crash Fix : Crash when use Entry
	- Crash Fix : Crash when use length setter of Vec2
	- Crash Fix : Crash when use TextComponent
	- Crash Fix : Crash when we use size of SpriteComponent
	- Crash Fix : Crash when we use LifeComponent

## V 1.1.2 : Patch Update 2 - 01/06/19

    - UISystem : Add a show_debug function
    - Optimization
    - Bug Fix : EntitySystem give wrong id to Entities
    - Bug Fix : EntitySystem is render after UISystem
    - Bug Fix : Window is always in debug mode

Cette MAJ ne casse pas la combatilbilité avec la précédente.

## V 1.1.1 : Patch Update - 30/05/19

    - Create and add PyEngine Logo
    - Window : Add icon parameter
    - Window : Use Color class
    - TextComponent : Add text management
    
    - Bug Fix : OutOfWindow don't take sprite size
    - Critical Bug Fix : CollisionCallbacks is not defined in ControlComponent

Cette MAJ ne casse pas la combatilbilité avec la précédente.

## V 1.1.0 : General Update - 25/05/19

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

## V 1.0.2 : Fix Update 2 - 11/05/19

    - Entity : Can get custom component
    - Setup : Fix crash when pygame is not installed
    - Setup : Don't get PyGame2
    
Cette MAJ ne casse pas la combatilbilité avec la précédente.

## V 1.0.1 : Fix Update - 10/05/19

    - Enums : Add Controls in __all__
    - Entity : Can add custom component
    
Cette MAJ ne casse pas la combatilbilité avec la précédente.

## V 1.0.0 : First Update - 09/05/19

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

## V 0.2.0-DEV : Little Update - 25/04/19

    - Components/PhysicsComponent : Collision Callback return object
    - Systems/EntitySystem : Remove condition to add entity
    - Window : Add a function to end game
    - Setup.py : Add dependances (PyGame)

## V 0.1.0-DEV : Initial Update - 19/04/19

    - First Version