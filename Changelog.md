# Changelog

## V 1.6.1 - XX/XX/19

    - Bug Fix : Physics Objects without gravity can't move

## V 1.6.0 - 24/08/19

    - Window : Add limit_fps property
    - WindowCallbacks : Add RUNWINDOW Callback
    - ControlComponent : Rework to work with physic engine
    - ControlComponent : Remove DOUBLEJUMP ControlType
    - SpriteComponent : Set origin of sprite to center
    - SpriteComponent-AnimComponent : Add flipx and flipy properties
    - PhysicsComponent : Rework with a physic engine (Pymunk)
    - Selector : Remove background by default
    
    - Optimization
    
    - Bug Fix : Check if object is a Vec2 doesn't work with operations
    - Bug Fix : OutOfWindow Callback return wrong object
    
    - Crash Fix : Crash in debug mode with Widgets added

## V 1.5.1 - 04/08/19

    - Unlock FPS
    - Font : Rework on Font System
    
    - Optimization

    - Bug Fix : Has_component doesn't work with custom component

Cette MAJ ne casse pas la combatilbilité avec la précédente.
    
## V 1.5.0 - 28/07/19

    - Entity-Tilemap : Move to "Entities" folder
    - ControlComponent : Add MOUSEFOLLOW ControlType
    - PhysicsComponent : Add MOUSEFOLLOW and MOUSECLICK CollisionCauses
    - Client : Send type, author and message. Packet are used only in PyEngine
    - Button : Add enabled property
    - Entry : Add Ctrl-C and Ctrl-V
    - Entry : Remove limit of caracters
    - Entry : Repeats the characters if the key is kept pressed
    - Console : Create console widget
    - MultilineLabel : Create Label widget for multiline
    - Label : Replace \n to void. Label doesn't support break lines
    - AnimatedImage : Create Image widget which support multiple images
    - Selector : Create selector widget
    - Others : Rename Maths to Others
    - Others : Add wrap_text and get_images_from_gif functions
    - Unit Tests : Fix Vec2 and Color tests
    - Unit Tests : Add Console and MultilineLabel tests
    
    - Optimization
    
    - Bug Fix : ControlComponent make weird movements with MOUSECLICK ControlType

    - Crash Fix : Crash when use show or hide
    - Crash Fix : Crash when Client doesn't have callback
	- Crash Fix : Crash when UISystem must show widgets without image or rect
    
## V 1.4.2 - 17/07/19

    - PhysicsComponent : Add callback parameters of constructor
    - Tilemap : place tile at bottom
    
    - Optimization
    
    - Bug Fix : OUTOFWINDOW doesn't work with CameraSystem
    - Bug Fix : Remove offset when change position
    - Bug Fix : Hide and Show doesn't spread to child in Widgets
    - Bug Fix : Focus stays when widget is hide

Cette MAJ ne casse pas la combatilbilité avec la précédente.

## V 1.4.1 - 14/07/19

    - Color : Add parameter to apply darker or lighter x times
    
    - Optimization

    - Bug Fix : Fix Diagonal movement from MoveComponent
    - Bug Fix : EntitySystem give wrong id to tiles of Tilemap
    - Bug Fix : Sprite is rescale at every change of sprite in SpriteComponent
    - Bug Fix : If tileset isn't in the same director than tilemap, sprites isn't found
    - Bug Fix : ControlComponent save the keypressed when change world

Cette MAJ ne casse pas la combatilbilité avec la précédente.

## V 1.4.0 : All Update - 13/07/19

    - AnimComponent : Add play attribute
    - AnimComponent : Use clamp function to set timer
    - PositionComponent : Offset is now a property
    - PositionComponent : position return the position without offset
    - SpriteComponent : Scale don't modify width and height
    - LifeComponent : Add callback which is trigger when entity has 0 pv
    - Network : If packet have "TOALL" as type, author will recieve the packet
    - Tilemap : Create basic tilemap (using Tiled)
    - Button-Image : size is now a Vec2
    - Button : Only Left Button of Mouse trigger Button
    - Button : Remove btn argument on command of Button
    - Checkbox : Create checkbox widget
	- ProgressBar : Create progressbar widget
	- Entry : Add accents letters in accepted and remove some weird symbol
	- Color : Use clamp function
	- Maths : Clamp function can be use without max or/and min value
	- Font : Add rendered_size function
    - Vec2 : Add divide operator
    - Vec2 : Add iterator
    - Vec2 : Change representation in string to "Vec2(X, Y)"
	- Unit Tests : Add Tilemap, Prefabs and Network tests
	- Unit Tests : Update Components and Widgets tests
    - Setup : Add numpy as dependances
    - README : Add version of pygame
    - README : Remove useless section
    
    - Optimization

    - Bug Fix : Button must be focused to be hover
    - Bug Fix : Rescale SpriteComponent can make weird result
    - Bug Fix : Shift-capitals must be typed twice in Entry to be writed
    - Bug Fix : Text can be more longer than the Entry
    - Bug Fix : Press an other key than the actuel break the movement with ControlComponent
    
    - Crash Fix : Crash sometimes to create hover button with sprite
    - Crash Fix : Crash when import Vec2 at first

## V 1.3.0 : Utils Update - 07/07/19

    - Window : Add is_running and update_rate property
    - Window : In debug, show fps in console (must be around 60)
    - Window-World : Rename and move WorldCallbacks to WindowCallbacks
    - WindowCallbacks : Add CHANGEWORLD and STOPWINDOW
    - Entity : Can't have the same type of component two times
    - EntitySystem-UISystem : Change debug color to blue for ui and red for entity
    - EntitySystem : Add get_all_entities function
    - PhysicsComponent : Create CollisionInfos
    - MoveComponent : Unlock diagonal movement
    - LifeComponent : Use clamp function to set life
    - AnimComponent : Create basic animator system
    - Entry : Add width and sprite property
    - Entry : Add color and front parameters
	- Entry : Define accepted letters
    - Network : Create basic network system
    - Vec2 : Add normalized function
    - Color : Add to_hex and from_hex function
    - Colors : Add new colors
    - loggers : Create logging System
    - Lang : Create translate system
    - Config : Create Config system
    - Maths : Create usefull functions (clamp)
	- Unit Tests : Add AnimComponent, loggers, config and lang tests
	- Unit Tests : Update Window, Color, Entry and World tests
	- Optimization and fix some little errors
	
	- Bug Fix : Entry is update without focus
    
    - Crash Fix : Crash when show id of Entity Texts
    - Crash Fix : Crash when use entity_follow of CameraSystem

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